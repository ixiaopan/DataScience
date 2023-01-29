import { GITLAB_WEBHOOK_TOKEN, GITLAB_EVENT_TYPE, GITLAB_PROJECT_LIST } from '../config/gitlab'
import { mergeRequestHook } from './mr'
import { commentHook } from './comment'
import { sendMR } from '../utils/message'

export async function gitlabHookHandler(ctx) {
  console.log('gitlab hooks invoked')

  const responseError = (msg: string) => {
    ctx.res.setHeader('Content-Type', 'text/plain')
    ctx.status = 500
    ctx.body = msg

    console.log('response error:', msg)
  }
  const responseSuccess = (msg = 'ok') => {
    ctx.res.setHeader('Content-Type', 'text/plain')
    ctx.status = 200
    ctx.body = msg

    console.log('response success: ', msg)
  }
  
  const { headers, body } = ctx.request

  // Token Validation
  const token = headers['X-Gitlab-Token'] || headers['x-gitlab-token']
  if (!token || token != GITLAB_WEBHOOK_TOKEN) {
    return responseError('invalid Secret Token')
  }

  // Empty Body
  if (!body) {
    return responseError('Empty Response')
  }

  const eventType = body.object_kind
  // Check Event Type
  if (!Object.values(GITLAB_EVENT_TYPE).includes(eventType)) {
    return responseError(`${eventType} event is not supported`)
  }
  
  // Project Validation
  const { id, name } = body.project || {}
  if (!id || !GITLAB_PROJECT_LIST.find(p => p.id == id)) {
    return responseError(`Project [${name}] does not exist`)
  }

  let handler
  if (eventType == GITLAB_EVENT_TYPE.MERGE_REQUEST) {
    handler = mergeRequestHook
  } 
  else if (eventType == GITLAB_EVENT_TYPE.COMMENT) {
    handler = commentHook
  }

  try {
    const data = await handler(body)
    sendMR(data)
    responseSuccess()
  } catch (e) {
    responseError(e.message)
  }
}
