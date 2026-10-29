import tailwindcss from "@tailwindcss/vite";
import { devtools } from "@tanstack/devtools-vite";

import { tanstackStart } from "@tanstack/react-start/plugin/vite";

import viteReact from "@vitejs/plugin-react";
import { defineConfig } from "vite";

const config = defineConfig({
	resolve: { tsconfigPaths: true },
	// Bundle every dependency into the server build, so the runtime image needs no node_modules.
	ssr: { noExternal: true },
	plugins: [devtools(), tailwindcss(), tanstackStart(), viteReact()],
});

export default config;
