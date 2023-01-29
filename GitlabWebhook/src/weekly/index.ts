import Parser from 'rss-parser'

import { I_FEED_META,  FEED_LIST } from '../config/feed'
import { sendRSS } from '../utils/message'

const parser = new Parser({
  headers: {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
  },
})

async function fetchFeed(f: I_FEED_META): Promise<{
  title: string,
  link?: string,
} | undefined> {
  try {
    const feed = await parser.parseURL(f.url)
    const latest = feed.items && feed.items[0]
    
    console.log('✅ ', f.name, '>>>', latest?.title)

    return {
      title: latest?.title + ' >>> ' + f.name,
      link: latest?.link,
    }
  } catch (e) {
    console.error('❌', f.name);
  }
}

export function crawRSS(withNotification = true) {
  Promise.all(FEED_LIST.map((f) => fetchFeed(f))).then(allRes => {
    if (withNotification) {
      sendRSS(allRes)
    }
    console.log('⭐ All Done.')
  })
}

// dev 本地 debug
if (process.env.NODE_ENV == 'dev') {
  console.log('🔨 debugging Weekly...')
  crawRSS(false)
}
