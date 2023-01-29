/**
 * @file 飞书消息格式
 * @doc 
 * - https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/create_json
 * - https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN
 */

import axios from 'axios'
import { NPM_WEBHOOK } from '../config/robot'

export function sendPlainText(text: string) {
  axios.post(NPM_WEBHOOK, {
    msg_type: 'text',
    content: {
      text,
    }
  })
}

export function sendRichText(title: string, content: ({ tag: string, text: string, href?: string, user_id?: string }[])[]) {
  axios.post(NPM_WEBHOOK, {
    msg_type: 'post',
    content: {
      post: {
        zh_cn: {
          title,
          content,
        }
      }
    }
  })
}

export function sendRSS(rssList: ({ title: string, link?: string } | undefined)[]) {
  const cardElements = rssList?.filter(o => o?.link).map((f, idx) => ({
    tag: 'div',
    text: {
      content: `[${idx + 1} ${f?.title}](${f?.link})`,
      tag: 'lark_md',
    }
  }))

  if (!cardElements?.length) return console.error('no latest feed')
  
  axios.post(NPM_WEBHOOK, {
    msg_type: 'interactive',
    card: {
      header: {
        template: 'green',
        title: {
          content: '💡 Frontend Weekly',
          tag: 'plain_text',
        }
      },
      elements: cardElements,
    }
  })
}


export function sendMR(f: { 
  url: string,
  id: string,
  title: string
  state: string, 
  projectName: string,
  created_at: string,
  description: string,
  source_branch: string, 
  source_branch_url: string, 
  target_branch: string,
  target_branch_url: string, 
  last_commit: {
    title: string,
    url: string,
    author: { name: string, }
  },
  
  // 发起 MR 的人
  author: {
    id: string,
    name: string
  },
  
  // 其他人 可选
  operator?: {
    id: string,
    title: string,
    name: string
  },
}) {
  if (!f) return

  const elements = [
    {
      "tag": "column_set",
      "flex_mode": "none",
      "columns": [
        {
          "tag": "column",
          "width": "weighted",
          "weight": 1,
          "vertical_align": "top",
          "elements": [
            {
              "tag": "markdown",
              "content": `**📝 标题**\n${f.title}`,
            }
          ]
        },
        {
          "tag": "column",
          "width": "weighted",
          "weight": 1,
          "vertical_align": "top",
          "elements": [
            {
              "tag": "markdown",
              "content": `**📝 说明**\n${f.description || '无'}`,
            }
          ]
        }
      ]
    },


    {
      "tag": "column_set",
      "flex_mode": "none",
      "background_style": "default",
      "columns": [
        {
          "tag": "column",
          "width": "weighted",
          "weight": 1,
          "vertical_align": "top",
          "elements": [
            {
              "tag": "markdown",
              "content": `**👷 发起人**\n<at id=${f.author.id}></at>${f.author.id ? '' : f.author.name}`
            }
          ]
        },
        {
          "tag": "column",
          "width": "weighted",
          "weight": 1,
          "vertical_align": "top",
          "elements": [
            {
              "tag": "markdown",
              "content": `**📆 创建时间**\n${f.created_at}`,
            }
          ]
        }
      ]
    },

    {
      "tag": "column_set",
      "flex_mode": "none",
      "background_style": "default",
      "columns": [
        {
          "tag": "column",
          "width": "weighted",
          "weight": 1,
          "vertical_align": "top",
          "elements": [
            {
              "tag": "markdown",
              "content": `**🐈 源/目标分支**\n[${f.source_branch}](${f.source_branch_url})\n  ↓  \n[${f.target_branch}](${f.target_branch_url})`
            }
          ],
        },
        {
          "tag": "column",
          "width": "weighted",
          "weight": 1,
          "vertical_align": "top",
          "elements": [
            {
              "tag": "markdown",
              "content": `**👨‍💻 最近一次提交**\n提交信息：[${f.last_commit?.title}](${f.last_commit?.url})\n提交人: ${f.last_commit.author?.name}`,
            }
          ]
        }
      ]
    },

    // 
    {
      "tag": "hr"
    },

    {
      "tag": "action",
      "actions": [
        {
          "tag": "button",
          "text": {
            "tag": "plain_text",
            "content": "👀 点击查看"
          },
          "type": "primary",
          "multi_url": {
            "url": f.url,
          }
        }
      ]
    }
  ]

  // 存在执行者 多种角色（比如审阅人、合并者、close mr 的执行人）
  if (f.operator) {
    const operatorColumn = {
      "tag": "column_set",
      "flex_mode": "none",
      "background_style": "default",
      "columns": [
        {
          "tag": "column",
          "width": "weighted",
          "weight": 1,
          "vertical_align": "top",
          "elements": [
            {
              "tag": "markdown",
              "content": `**✅ ${f.operator?.title}** <at id=${f.operator.id}></at>${f.operator.id ? '' : f.operator.name}`
            }
          ],
        },
        {
          "tag": "column",
          "width": "weighted",
          "weight": 1,
          "vertical_align": "top",
          "elements": []
        }
      ]
    }
    elements.splice(3, 0, operatorColumn)
    elements.splice(3, 0, { "tag": "hr" })
  }

  axios.post(NPM_WEBHOOK, {
    msg_type: 'interactive',
    card: {
      header: {
        template: 'red',
        title: {
          "tag": "plain_text",
          "content": `⚠️ ${f.projectName}#${f.id} ${f.state}`,
        },
      },
      elements,
    }
  })
}
