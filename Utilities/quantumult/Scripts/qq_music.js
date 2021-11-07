// QQ Music

let body = JSON.parse($response.body)

if ($request.path.indexOf('posconfig') > -1) {
  // no idea what they exactly are is
  body['period'] = 24 * 60 * 60 // 24*60*60
  body['pos']['adVertiShowTime'] = 0 
  body['pos']['adShowSongOverTime'] = 0 
  body['pos']['adShowAfterTime'] = 0
  body['pos']['adShowTime'] = 0
  body['pos']['adMaxImpressionTimes'] = 0
  body['pos']['requestAd'] = false
}

else if ($request.path.indexOf('ad/strategies') > -1) {
  body['period'] = 0 // 24*60*60
  Object.keys(body['flowStrategies']).forEach(k => {
    ad = body['flowStrategies'][k]
    
    ad['period'] = 24 * 60 * 60 // 24*60*60
    ad['isValid'] = false
    ad['adPlatforms'].forEach(o => {
      o['enable'] = false
      o['requestAdTimeout'] = 0
    })
  })
}

else if ($request.path.indexOf('config') > -1) {
  body['config'].forEach(ad => {
    ad.adPlayingInMobileNet = false
    ad.adPlayingInWifi = false
    
    ad.adPreloadMaximum = 0
    ad.adPreloadRequestTimeout = 0
    ad.adPreloadTime = 0

    ad.voiceOpenUnderScreenDark = false
    ad.voiceOpenDuringAdPlaying = false

    ad.requestAd = false
    ad.requestAdTimeout = 0
    ad.requestAdPeriod = 24 * 60 * 60 // 24 * 60 * 60
    ad.firstAdPeriod = 0
    ad.otherAdPeriod = 0
    ad.adShowTime = 0
    ad.showAdLogo = false

    ad.enableFrequencyControls = false
    ad.frequencyControls = []
    ad.iconKeepaliveTime = 0
    ad.showAppLogo = false
    ad.adCreativeShowInterval = 0
    ad.maxShowTimesPeriod = 365 * 24 * 60 * 60 // the default value is 24 * 60 * 60 
  })
}

$done({ body: JSON.stringify(body) })
