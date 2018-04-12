# Chat analyzer

A simple script to analyze WhatsApp and Hike chats. You can export chat as text file through email chat option.

## Usage

```
➜  chat-analyzer git:(master) ✗ python3 analyze.py -h
usage: analyze.py [-h] --filename FILENAME [--app {whatsapp,hike}]
                  [--entity {word,emoji}] [--min-word-limit MIN_WORD_LIMIT]
                  [--common COMMON]

Process whatsapp messages

optional arguments:
  -h, --help            show this help message and exit
  --filename FILENAME
  --app {whatsapp,hike}
                        Name of the app. E.g. whatsapp or hike
  --entity {word,emoji}
                        Entity to count. E.g. word or emoji
  --min-word-limit MIN_WORD_LIMIT
                        Minimum word limit for processing
  --common COMMON       Number of top items
```

## Demo

Print top 5 words in the chat

```
➜  chat-analyzer git:(master) ✗ python3 analyze.py --filename sample.txt --entity word --common 5
Analyzed 31 messages
{'Bar': {'top': {'free?': 1, 'good': 2, 'howdy': 1, 'well,': 1, 'you?': 1},
         'total': 18},
 'Foo': {'top': {'good': 2, 'happy': 1, 'hello,': 1, 'now?': 1, 'yes?': 1},
         'total': 11}}
```

Print top 5 emojis in the chat

```
➜  chat-analyzer git:(master) ✗ python3 analyze.py --filename sample.txt --entity emoji --common 5
Analyzed 31 messages
{'Bar': {'top': {'👆': 1, '😁': 4, '😂': 3}, 'total': 8},
 'Foo': {'top': {'🏻': 5, '💦': 1, '😁': 2}, 'total': 8}}
```

Print top 5 emojis in the chat for hike

```
➜  chat-analyzer git:(master) ✗ python3 analyze.py --filename sample-hike.txt --entity emoji --common 5 --app hike
Analyzed 31 messages
{'Bar': {'top': {'👆': 1, '😁': 4, '😂': 3}, 'total': 8},
 'Me': {'top': {'🏻': 5, '💦': 1, '😁': 2}, 'total': 8}}
 ```

## TODO

* Response times
* Message count distribution through years and time of the day
* Messages sent to reply received ratio
* Amazing docs
* Tests

## Thanks

This was written to tell my friend how basic analysis of chats would look when done by companies. I also took motivation from [facebook_data_analyzer](https://github.com/Lackoftactics/facebook_data_analyzer)

## LICENSE

MIT license Copyright (c) 2018 Karthikeyan S
