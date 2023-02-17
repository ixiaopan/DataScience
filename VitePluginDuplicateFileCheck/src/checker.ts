import type { ViteDevServer } from 'vite'
import { parse } from 'path'
import fg from 'fast-glob'

import { debug, filterFileByExt } from './util'

type IOption = {
  root: string
  ext: string
  dirs: string[],
  logLevel?: LOG_LEVEL
}

enum LOG_LEVEL {
  WARNING = '1',
  ERROR = '2',
}

const PLUGIN_NAME = 'vite-plugin-duplicate-file-check'

export default class Context {
  private _server
  
  private _compMap = {}
  
  root = ''
  ext = ''
  dirs = []
  
  logLevel = LOG_LEVEL.ERROR

  setupConfig(cfg: IOption) {
    this.root = cfg.root
    
    this.dirs = cfg.dirs
    this.ext = cfg.ext
    
    this.logLevel = cfg.logLevel || LOG_LEVEL.ERROR
    
    this.searchComp()
  }
  setupServer(server: ViteDevServer) {
    if (this._server) return
    
    debug('start watching file changes...')

    this._server = server
    
    server.watcher
      .on('unlink', (path) => {
        if (!filterFileByExt(this.ext, path)) return
        
        this.removeCompByPath(path)
      })
      .on('add', (path) => {
        if (!filterFileByExt(this.ext, path)) return
        
        this.addCompByPath(path)
      })
  }

  private add2Map(name: string, path: string) {
    if (!this._compMap[name]) {
      this._compMap[name] = []
    }

    this._compMap[name].push(path)

  }
  private removeFromMap(name: string, path: string) {
    this._compMap[name] = this._compMap[name]?.filter((p: string) => p != path) || []
  }
  private hasInMap(name: string) {
    return !!this._compMap[name]?.length
  }

  removeCompByPath(path: string) {
    debug(`removed comp, ${path}`)
    
    const name = this.getNameFromPath(path)
    this.removeFromMap(name, path)
  }
  
  addCompByPath(path: string) {
    debug(`add comp, ${path}`)
    
    const name = this.getNameFromPath(path)
    
    if (this.hasInMap(name)) {
      if (this.logLevel == LOG_LEVEL.ERROR) {
        throw new Error(`[${PLUGIN_NAME}] naming conflicts: ${path}`)
      }
      else if (this.logLevel == LOG_LEVEL.WARNING) {
        return console.warn('\x1B[31m%s\x1B[0m', `[${PLUGIN_NAME}] naming conflicts: ${path}`)
      }
    }

    this.add2Map(name, path)
  }
  
  private getNameFromPath(path: string) {
    const parsedPath = parse(path)
    
    let filename = parsedPath.name
    // 兼容 Hello/index.vue
    if (filename == 'index') {
      const folders = parsedPath.dir.split('/').filter(Boolean)
      filename = folders && folders[folders.length - 1] || 'unknown'
    }

    return filename
  }
  
  searchComp() {
    debug(`started with ${this.root}/${this.dirs.join(',')}`)
    
    const patterns = this.dirs.map((d: string) => `${d}/**/*.${this.ext}`)
    const entries = fg.sync(patterns, {
      cwd: this.root,
      ignore: ['node_modules'],
      onlyFiles: true,
    })
    
    entries.forEach((f: string) => {
      this.addCompByPath(f)
    })
  }
}
