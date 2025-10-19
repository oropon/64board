import { defineConfig } from "vite";

export default defineConfig({
  build: {
    outDir: "../backend/static/dist",
    emptyOutDir: true,
    manifest: true,

    rollupOptions: {
      input: {
        main: "src/main.ts",
      },
    },
  },
  server: {
    port: 5173,
    proxy: {
      "/api": "http://localhost:5000"
    }
  },
  css: {
    devSourcemap: true,
  }
});