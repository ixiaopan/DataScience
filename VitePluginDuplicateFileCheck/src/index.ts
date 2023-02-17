import type { ResolvedConfig, ViteDevServer } from 'vite'

import Context from './checker'

const defaultOptions = {
  dirs: ['src/components'],
  ext: 'vue',
}

type IOption = {
  dirs: string[],
  ext: string
}

export default function duplicateFileCheck(options: IOption) {
  const ctx = new Context()

  return {
    name: 'duplicate-file-check',

    configResolved(config: ResolvedConfig) {
      ctx.setupConfig({
        ...defaultOptions,
        ...options,
        root: config.root,
      })
    },

    configureServer(server: ViteDevServer) {
      ctx.setupServer(server)
    },
  }
}
