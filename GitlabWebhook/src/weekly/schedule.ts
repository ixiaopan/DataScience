import { crawRSS } from './index'

const later = require('@breejs/later')

later.date.localTime()
const s = later.parse.text('at 11:00 am on Mon')
later.setInterval(crawRSS, s)
