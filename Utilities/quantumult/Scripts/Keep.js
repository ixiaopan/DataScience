
let body = JSON.parse($response.body)

// HomePage - the second tab area, floating ad
if ($request.path.indexOf('homepage') > -1) {
  body['data']['sections'] = (body['data']['sections'] || []).filter(elem => ['quickEntrance', 'smallCardAcross', 'user_stats', 'recommendCourse'].some(v => (elem.sectionId || elem.contentStyle).indexOf(v) > -1))
}

// HomePage - tab layout
else if ($request.path.indexOf('config') > -1 ) {
  const whiteTabList = {
    bottomBarControl: ['home', 'entry', 'personal'],
    homeTabs: ['homeRecommend']
  }  
  if (body['data']['bottomBarControl']) {
    body['data']['bottomBarControl']['tabs'] = (body['data']['bottomBarControl']['tabs'] || []).filter(elem => 
      (whiteTabList.bottomBarControl.indexOf(elem.tabType) > -1)
    )
  }
  if (body['data']['homeTabs']) {
    body['data']['homeTabs'] = (body['data']['homeTabs'] || []).filter(elem => whiteTabList.homeTabs.indexOf(elem.type) > -1)
  }

  body['data']['trainingReminders'] = []
  body['data']['splash.warm.boot.interval'] = 1000*60*60*24
  body['data']['splash.ad.load.max.timeout'] = 0
  body['data']['splash.api.max.timeout'] = 0
}

// Profile Page
else if ($request.path.indexOf('athena') > -1) {
  ['courseTabList', 'myCourseInfo', 'seriesCourseInfo', 'tags'].forEach(key => body['data'][key] = [])  
}

$done({ body: JSON.stringify(body) })
