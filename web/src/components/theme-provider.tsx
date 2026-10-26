import { ScriptOnce } from "@tanstack/react-router";
import { createContext, type ReactNode, use, useEffect, useState } from "react";

export type Theme = "light" | "dark" | "system";

const STORAGE_KEY = "gha-practice:theme";

// Runs before first paint so a stored dark theme never flashes light.
const themeScript = `(() => {
	try {
		const t = localStorage.getItem(${JSON.stringify(STORAGE_KEY)});
		const dark = t === "dark" || (t !== "light" && matchMedia("(prefers-color-scheme: dark)").matches);
		document.documentElement.classList.toggle("dark", dark);
	} catch {}
})()`;

interface ThemeContextValue {
	theme: Theme;
	setTheme: (theme: Theme) => void;
}

const ThemeContext = createContext<ThemeContextValue | null>(null);

function readStoredTheme(): Theme {
	try {
		const stored = window.localStorage.getItem(STORAGE_KEY);
		return stored === "light" || stored === "dark" ? stored : "system";
	} catch {
		return "system";
	}
}

export function ThemeProvider({ children }: { children: ReactNode }) {
	// Starts as "system" on both server and client; the stored choice loads after hydration.
	const [theme, setThemeState] = useState<Theme>("system");

	useEffect(() => {
		setThemeState(readStoredTheme());
	}, []);

	useEffect(() => {
		const media = window.matchMedia("(prefers-color-scheme: dark)");
		const apply = () => {
			const dark = theme === "dark" || (theme === "system" && media.matches);
			document.documentElement.classList.toggle("dark", dark);
		};
		apply();
		if (theme !== "system") return;
		media.addEventListener("change", apply);
		return () => media.removeEventListener("change", apply);
	}, [theme]);

	function setTheme(next: Theme) {
		setThemeState(next);
		try {
			if (next === "system") window.localStorage.removeItem(STORAGE_KEY);
			else window.localStorage.setItem(STORAGE_KEY, next);
		} catch {
			// Storage unavailable: the choice lasts for this page view only.
		}
	}

	return (
		<ThemeContext value={{ theme, setTheme }}>
			<ScriptOnce>{themeScript}</ScriptOnce>
			{children}
		</ThemeContext>
	);
}

export function useTheme(): ThemeContextValue {
	const context = use(ThemeContext);
	if (!context) throw new Error("useTheme must be used inside <ThemeProvider>");
	return context;
}
