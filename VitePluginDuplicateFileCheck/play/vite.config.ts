import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import Inspect from 'vite-plugin-inspect'
import DuplicateFileCheck from 'vite-plugin-duplicate-file-check'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    
    DuplicateFileCheck({
      dirs: ['src/components', 'src/partials'],
      logLevel: '1',
    }),
    
    Inspect({
      // build: true,
    }),
  ],
})