import axios from 'axios'

import { USER_LIST } from "../config/user"
import { GITLAB_PERSONAL_ACCESS_TOKEN, GITLAB_API_V4, GITLAB_HOST, GITLAB_PROJECT_LIST } from '../config/gitlab'

// ----
const request = axios.create({
  baseURL: GITLAB_API_V4,
  timeout: 10 * 1000,
  headers: { 'Private-Token': GITLAB_PERSONAL_ACCESS_TOKEN }
})

export function fetchCommentsByMRId(projectId: number, mrId: number) {
  return request.get(`/projects/${projectId}/merge_requests/${mrId}/notes`)
}

export function fetchOpenedMRList(projectId: number) {
  return request.get(`/projects/${projectId}/merge_requests?state=opened`)
}

// ------
// 获取IM的用户id
export function getUserIdByGitId(id: string | number) {
  const m = USER_LIST.find(o => o.id == id)
  return m?.userId || ''
}

// 获取git的用户名
export function getNameByGitId(id: string | number) {
  const m = USER_LIST.find(o => o.id == id)
  return m?.username || ''
}

// ----
// 从 url 读取 mr id
export function extractMRId(url: string) {
  const d = url?.match(/\/(\d+)$/)
  return d && d[1] || ''
}

function ensureHostSuffix(host = GITLAB_HOST) {
  return /\/$/.test(host) ? host : host + '/'
}

export function replaceHost(url: string, host = GITLAB_HOST) {
  return url.replace(/^https?:\/\/([\d|\.:]+)\//, () => ensureHostSuffix(host))
}

export function joinBranchUrl(url: string, branch: string) {
  return `${ensureHostSuffix(replaceHost(url))}-/commits/${branch}`
}

// ----
export function getProjectNameById(id: number) {
  const p = GITLAB_PROJECT_LIST.find(p => p.id == id)
  return p?.name || ''
}
