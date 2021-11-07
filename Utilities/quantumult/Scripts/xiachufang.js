// 下厨房feed流去广告

let body=JSON.parse($response.body)

// recipe, ad
body['cells'] = body['cells'].filter(elem => elem['impression_sensor_events'].some(elem => (elem.properties || {}).target_type != 'ad') || elem['click_sensor_events'].some(elem => (elem.properties || {}).target_type != 'ad'))

// reset noisy data
body['cells'].forEach(elem => elem.title_3rd = '')

$done({ body: JSON.stringify(body) })
