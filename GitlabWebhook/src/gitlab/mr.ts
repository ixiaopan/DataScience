import { GITLAB_PROJECT_LIST, MR_ACTION } from "../config/gitlab"
import { sendRichText } from "../utils/message"
import { fetchOpenedMRList, extractMRId, joinBranchUrl, getNameByGitId, replaceHost, getUserIdByGitId, getProjectNameById } from './service'

interface IAssignee {
  id: number,
  name: string,
  username: string
}

interface IMergeRequestEvent {
  object_kind: string
  user: {
    id: number
    name: string
    username: string
    avatar_url: string
    email: string
  }
  project: {
    id: number
    name: string
    description: string
    web_url: string
    avatar_url: string
    namespace: string
    homepage: string
    url: string
  }
  repository: {
    name: string
    url: string
    description: string
    homepage: string
  }
  object_attributes: {
    id: number
    target_branch: string
    source_branch: string
    author_id: number
    assignee_id: number
    title: string
    created_at: string
    updated_at: string
    state: string
    merge_status: string
    description: string
    source: {
      id: number
      name: string
      description: string
      path_with_namespace: string
      web_url: string
    }
    target: {
      name: string
      description: string
      path_with_namespace: string
      web_url: string
    }
    last_commit: {
      id: string
      title: string
      message: string
      timestamp: string
      url: string
      author: {
        name: string
        email: string
      }
    }
    url: string
    action: string,
  },
  changes: {
    assignees: {
      previous: IAssignee[],
      current: IAssignee[]
    },
  },
  assignees?: {
    id: number
    name: string
    username: string
  }[]
}

function difference(setA, setB) {
  if (setA.size == 0) return setB
  
  const _difference = new Set(setA)
  for (const elem of setB) {
    _difference.delete(elem);
  }
  return _difference;
}

export async function mergeRequestHook(data: IMergeRequestEvent) {
  console.log('merge request handler')

  const { project, object_attributes, user, assignees, changes } = data
  const { 
    action, state, last_commit,
    title, url, created_at, updated_at, description, source_branch, target_branch,
    author_id, assignee_id,
    source, target
  } = object_attributes

  const basicInfo = {
    url: replaceHost(url),
    id: extractMRId(url),
    title,
    state, // MR 的状态
    projectName: project.name,
    created_at,
    description, 
    source_branch, 
    source_branch_url: joinBranchUrl(source?.web_url, source_branch), 
    target_branch,
    target_branch_url: joinBranchUrl(target?.web_url, target_branch), 
    last_commit: {
      ...last_commit,
      url: replaceHost(last_commit.url),
    },
    author: {
      id: getUserIdByGitId(author_id),
      name: getNameByGitId(author_id),
    },
  }

  // 关闭
  if (action == MR_ACTION.close) {
    return {
      ...basicInfo,
      operator: {
        id: getUserIdByGitId(user.id),
        title: '执行人',
        name: user.name || getNameByGitId(user.id),
      },
    }
  }

  // 新开
  if (action == MR_ACTION.open || action == MR_ACTION.reopen) {
    // 没有指定 reviewer
    if (!assignee_id) {
      return {
        ...basicInfo,
        state: 'opened 未指定CR负责人',
      }
    }

    // 指定了
    return {
      ...basicInfo,
      operator: {
        id: getUserIdByGitId(assignee_id),
        title: 'CR负责人',
        name: assignees?.find(o => o.id == assignee_id)?.name || getNameByGitId(assignee_id),
      },
    }
  }

  // 更新：
  // - 更新了 CR 负责人
  if (action == MR_ACTION.update) {
    const { previous, current } = changes.assignees || {}
    const prev = new Set(previous?.map(o => o.id))
    const cur = new Set(current?.map(o => o.id))

    // 存在变化
    if (difference(prev, cur).size) {
      return {
        ...basicInfo,
        state: `updated ${assignee_id ? '已指定CR负责人' : '未指定CR负责人'}`,
        operator: assignee_id ? {
          id: getUserIdByGitId(assignee_id),
          title: 'CR负责人',
          name: assignees?.find(o => o.id == assignee_id)?.name || getNameByGitId(assignee_id),
        } : null,
      }
    }
  }


  // 合并了
  if (action == MR_ACTION.merge) {
    return {
      ...basicInfo,
      operator: {
        id: getUserIdByGitId(user.id),
        title: '合并人',
        name: user.name || getNameByGitId(user.id),
      },
    }
  }

  console.log(`MR action [${action}] is not supported`)
}


// 创建 MR 未处理 定时提醒
interface IMergeRequest {
  id: number,
  title: string
  project_id: number,
  description: string
  state: string
  created_at: string
  updated_at: string
  user_notes_count: number
  author: {
    id: number,
    name: string
    username: string
  },
  assignee: {
    id: number,
    name: string
    username: string
  },
  web_url,
}

export async function createMRMention() {
  try {
    const allP = await Promise.all(GITLAB_PROJECT_LIST.map(async (p) => {
      const res = await fetchOpenedMRList(p.id)
      return res.data
    }))
    
    console.log('fetch opened mr done');
    
    const authorMRWoReviewer = {}
    const reviewerMR = {}
    allP?.forEach((data: IMergeRequest[]) => {
      data.forEach((res: IMergeRequest) => {        
        const o = {
          projectName: getProjectNameById(res.project_id),
          author: res.author,
          referenceId: extractMRId(res.web_url),
          url: replaceHost(res.web_url),
        }
  
        // 没有 CR 负责人
        if (!res.assignee) {
          if (!authorMRWoReviewer[res.author.id]) {
            authorMRWoReviewer[res.author.id] = []
          }
          authorMRWoReviewer[res.author.id].push(o)
        }
        
        // 有 CR 负责人
        else {
          if (!reviewerMR[res.assignee.id]) {
            reviewerMR[res.assignee.id] = []
          }
          reviewerMR[res.assignee.id].push(o)
        }
      })
    })

    // 
    let content = []
    if (Object.keys(authorMRWoReviewer).length) {
      // @ts-ignore
      const list = Object.keys(authorMRWoReviewer).reduce((memo: any, id: string |number) => {
        const uid = getUserIdByGitId(id)
        const at = uid ? {
          tag: 'at',
          user_id: uid,
        } : {
          tag: 'text',
          text: `@${getNameByGitId(id)}`,
        }
        
        memo = memo.concat([
          [
            at,
            {
              tag: 'text',
              text: `以下MR缺少CR负责人`,
            },
          ],
          ...(authorMRWoReviewer[id].map((o) => {
            return [
              {
                tag: 'a',
                href: o.url,
                text: `${o.projectName}#${o.referenceId}`
              },
            ]
          })),
          [
            {
              tag: 'text',
              text: '',
            }
          ],
        ])
        return memo
      }, [])

      content = content.concat(list)
    }

    if (Object.keys(reviewerMR).length) {
      // @ts-ignore
      const list = Object.keys(reviewerMR).reduce((memo: any, id: number) => {
        const uid = getUserIdByGitId(id)
        const at = uid ? {
          tag: 'at',
          user_id: uid,
        } : {
          tag: 'text',
          text: `@${getNameByGitId(id)}`,
        }
        
        const data = reviewerMR[id]
        memo = memo.concat([
          [
            at,
            {
              tag: 'text',
              text: `你有${data.length}个MR待评审`,
            },
          ],
          ...(data.map((o) => {
            return [
              {
                tag: 'a',
                href: o.url,
                text: `${o.projectName}#${o.referenceId}`
              }
            ]
          })),
          [
            {
              tag: 'text',
              text: '',
            }
          ],
        ])
  
        return memo
      }, [])

      content = content.concat(list)
    }
    
    if (content?.length) {
      sendRichText('MR 处理提醒', content)
    }
  }
  catch (e) {
    console.log('fetchOpenedMRList', e)
  }
}

// dev 本地 debug
// if (process.env.NODE_ENV == 'dev') {
//   console.log('🔨 debugging MR...')
//   createMRMention()
// }
