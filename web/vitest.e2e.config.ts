import { defineConfig } from "vitest/config";

/** End-to-end suite: run `bun run test:e2e`, which builds first. */
export default defineConfig({
	test: {
		include: ["e2e/**/*.test.ts"],
		globalSetup: ["e2e/server.ts"],
		testTimeout: 15_000,
	},
});
