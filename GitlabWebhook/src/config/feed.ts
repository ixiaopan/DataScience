/**
 * @file weekly rss feed
 */

export interface I_FEED_META {
  name: string,
  url: string
}

export const FEED_LIST: I_FEED_META[] = [
  {
    name: 'CSS Tricks',
    url: 'https://css-tricks.com/feed/',
  },
  {
    name: 'Frontend Focus',
    url: 'https:/frontendfoc.us/rss/'
  },
  {
    name: 'JavaScript Weekly',
    url: 'https://javascriptweekly.com/rss/'
  },
  {
    name: 'CSS Weekly',
    url: 'https://feeds.feedburner.com/CSS-Weekly'
  },
  {
    name: 'web.dev',
    url: 'https://web.dev/feed.xml'
  },
  {
    name: '阮一峰的网络日志',
    url: 'https://www.ruanyifeng.com/blog/atom.xml',
  },
  {
    name: 'David Walsh Blog',
    url: 'https://davidwalsh.name/feed',
  },
  {
    name: '少数派',
    url: 'https://sspai.com/feed'
  },
  {
    name: '知乎每日精选',
    url: 'https://www.zhihu.com/rss',
  },
  {
    name: '豆瓣最受欢迎的书评',
    url: 'https://www.douban.com/feed/review/book',
  },
]
