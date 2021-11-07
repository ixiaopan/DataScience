// 中国银行信用卡APP开屏广告

let body=JSON.parse($response.body)

body['body']['list'] = []
body['body']['picUpdate'] = ''

$done({ body: JSON.stringify(body) })
