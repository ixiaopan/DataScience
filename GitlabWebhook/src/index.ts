import Koa from 'koa'
import KoaRouter from '@koa/router'
import { gitlabHookHandler } from './gitlab/handler'
import koaBody from 'koa-body'

const app = new Koa()
const router = new KoaRouter()

router
.get('/', () => {
  console.log('hello world')
})
.post('/mr', gitlabHookHandler)

app.use(koaBody())
app.use(router.routes())

app.listen(3000)