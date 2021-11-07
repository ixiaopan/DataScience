// B站

let body = JSON.parse($response.body)

// HomePage - Feed
if ($request.path.indexOf('feed') > -1) {
  body['data']['items'] = (body['data']['items'] || []).filter(elem => !(
    elem.hasOwnProperty('ad_info') || 
    elem.hasOwnProperty('banner_item') || 
    elem['card_type'] != 'small_cover_v2')
  )
}

// 我的
else if ($request.path.indexOf('account/mine') > -1) {
  Object.keys(body['data']).forEach(k => {
    if (k in ['mall_home'] || k.indexOf('vip') > -1) {
      body['data'][k] = {}
    }
  })

  // 离线、历史、收藏、稍后、创作、稿件、客服、设置
  const whiteIconList = [396, 397, 398, 399, 171, 172, 407, 410]
  body['data']['sections_v2'] = (body['data']['sections_v2'] || []).filter(section => {
    section.items = (section.items || []).filter(elem => whiteIconList.indexOf(elem.id) > -1)
    return section.items.length
  })
}


// splash ads
else if ($request.path.indexOf('splash') > -1) {
  body['data']['max_time'] = 0
  body['data']['min_interval'] = 365*24*60*60
  body['data']['pull_interval'] = 365*24*60*60
  body['data']['list'].forEach(elem => {
    elem['duration'] = 0
    elem['begin_time'] = Date.now() - 864e5
    elem['end_time'] = Date.now() - 864e5
  })
}

// 标签页处理 - 去除底部发布、会员购
else if ($request.path.indexOf('resource/show/tab') > -1) {
  const whiteList = {
    tab: [40, 41, 545, 151], // 推荐、热门、追番、影视
    top: [176], // 消息
    bottom: [177, 179, 181] // 首页、动态、我的
  };

  ['tab', 'top', 'bottom'].forEach(key => {
    body['data'][key] = (body['data'][key] || []).filter(item => whiteList[key].indexOf(item.id) > -1)
  })
}

$done({ body: JSON.stringify(body) })
