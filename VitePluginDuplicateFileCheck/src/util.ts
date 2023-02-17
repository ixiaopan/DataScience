export function debug(...rest) {
  if (process.env.NODE_ENV == 'dev') {
    console.log('Debug: ', ...rest)
  }
}

export function isVueFile(id) {
  return /\.vue$/.test(id)
}

export function filterFileByExt(ext: string, path: string) {
  return new RegExp(`\\.${ext}$`).test(path)
}
