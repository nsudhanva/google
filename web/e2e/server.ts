import { type ChildProcess, spawn } from "node:child_process";
import { mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import type { TestProject } from "vitest/node";

const PORT = 3999;

declare module "vitest" {
	export interface ProvidedContext {
		baseUrl: string;
	}
}

async function waitFor(url: string, server: ChildProcess) {
	for (let i = 0; i < 100; i++) {
		if (server.exitCode !== null) throw new Error("Server exited early");
		try {
			if ((await fetch(url)).ok) return;
		} catch {
			// Not listening yet.
		}
		await new Promise((r) => setTimeout(r, 100));
	}
	throw new Error(`Server did not start: ${url}`);
}

/** Starts the production build on a throwaway database for the end-to-end suite. */
export default async function setup(project: TestProject) {
	const dir = mkdtempSync(join(tmpdir(), "leetcode-cards-e2e-"));
	const server = spawn(
		"node_modules/.bin/srvx",
		[
			"serve",
			"--prod",
			"--entry",
			"dist/server/server.js",
			"--static",
			"../client",
			"--port",
			String(PORT),
		],
		{
			env: {
				...process.env,
				DATA_DIR: resolve("../data"),
				DATABASE_PATH: join(dir, "e2e.db"),
			},
			// Keep server errors, drop its request log.
			stdio: ["ignore", "ignore", "inherit"],
		},
	);
	const baseUrl = `http://localhost:${PORT}`;
	await waitFor(`${baseUrl}/api/report`, server);
	project.provide("baseUrl", baseUrl);
	return () => {
		server.kill();
		rmSync(dir, { recursive: true, force: true });
	};
}
