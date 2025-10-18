import { defineConfig } from "vite";

export default defineConfig({
  build: {
    outDir: "../backend/static/dist",
    emptyOutDir: true,
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