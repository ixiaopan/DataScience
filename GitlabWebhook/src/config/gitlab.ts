/**
 * gitlab configuration
 */

// TODO: Security Risk
export const GITLAB_HOST = ''

export const GITLAB_API_V4 = `${GITLAB_HOST}/api/v4/`

// TODO: Security Risk
export const GITLAB_PERSONAL_ACCESS_TOKEN = ''

// X-Gitlab-Token HTTP header
export const GITLAB_WEBHOOK_TOKEN = ''

// 支持的事件类型
export enum GITLAB_EVENT_TYPE {
  // a new comment is made on commits, merge requests, issues, and code snippets
  COMMENT = 'note',
  // 
  MERGE_REQUEST = 'merge_request',
}

export enum MR_ACTION {
  open = 'open',
  reopen = 'reopen',
  update = 'update',

  merge = 'merge',
  close = 'close',

  approved = 'approved',
  unapproved = 'unapproved',
}

export enum MR_STATUS {
  OPENED = 'opened',
  CLOSED = 'closed',
}

// 需要MR通知的项目
export const GITLAB_PROJECT_LIST = [
  {
    name: 'your project name',
    id: 1,
  },
]
