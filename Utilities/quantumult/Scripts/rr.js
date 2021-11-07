
let body=JSON.parse($response.body)

body['data']['sections'] = []

$done({ body: JSON.stringify(body) })
