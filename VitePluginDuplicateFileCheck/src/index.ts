import type { ResolvedConfig, ViteDevServer } from 'vite'

import CompChecker from './checker'

const defaultOptions = {
  dirs: ['src/components'],
  ext: 'vue',
}

type IOption = {
  dirs: string[],
  ext: string
}

export default function duplicateFileCheck(options: IOption) {
  return {
    name: 'duplicate-file-check',

    configResolved(config: ResolvedConfig) {
      CompChecker.setupConfig({
        ...defaultOptions,
        ...options,
        root: config.root,
      })
    },

    configureServer(server: ViteDevServer) {
      CompChecker.setupWatcher(server.watcher)
    },
  }
}
