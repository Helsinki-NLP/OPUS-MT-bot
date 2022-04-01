# OPUS-MT Translation Bot

## Goal

Create translation bots that translate messages using OPUS-MT.
Currently the focus is on translation to Ukrainian. Additional language support will be added later.

This is a fork of the bots developed for translation between Czech and Ukrainian on various messaging platforms.

## Results

Status of the original Czech - Ukrainian bot:

- ✅ Telegram Bot: http://t.me/uk_cs_translation_bot
- ✅ Messenger Bot: https://m.me/uk.cs.translation.bot
- ⏳ WhatsApp Bot: waiting for accepting into beta program
- ⏳ Viber Bot: waiting for approval - https://www.viber.com/ukcstranslationbot

## API

The original Czech - Ukrainian translation bot uses the UFAL API - https://lindat.cz/translation/
OPUS-MT runs on https://translate.ling.helsinki.fi/ui/ukrainian

## Messaging Platforms

### Popularity

There are various websites with statistics:

- https://www.similarweb.com/apps/top/google/store-rank/ua/communication/top-free/
- https://www.statista.com/statistics/1188579/most-popular-messengers-in-ukraine/
- https://www.mobileaction.co/top-apps/social-networking-6005/ios/ua

It looks that Telegram is popular in Ukraine.

### API

#### Telegram

- https://github.com/python-telegram-bot/python-telegram-bot
- easy to use, does not require any approvals
- ✅ DONE - http://t.me/uk_cs_translation_bot

#### WhatsApp

- https://www.whatsapp.com/business/api
- requires approval
- ⏳ I have requested approval

#### Messenger

- https://developers.facebook.com/docs/messenger-platform/
- https://developers.facebook.com/docs/messenger-platform/webhook
- https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages
- ✅ DONE - https://fb.me/uk.cs.translation.bot
- ✅ DONE - https://m.me/uk.cs.translation.bot

#### Viber

- API: https://developers.viber.com/docs/api/rest-bot-api/
- ⏳I have requested for becoming public figure - https://www.viber.com/ukcstranslationbot

## Status:

- 2022-04-01: Adjustments to call OPUS-MT services
- 2022-03-31: Initial fork of the original implementation
