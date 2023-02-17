import { defineBuildConfig } from 'unbuild'

export default defineBuildConfig({
  entries: [
    'src/index',
  ],
  clean: false,
  rollup: {
    emitCJS: true,
    inlineDependencies: true,
  },
})
