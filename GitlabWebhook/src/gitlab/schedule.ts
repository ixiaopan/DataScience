import { createMRMention } from './mr'

const later = require('@breejs/later')

later.date.localTime()
const s = later.parse.text('at 5:00 pm')
later.setInterval(createMRMention, s)
