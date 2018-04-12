import argparse
from collections import Counter, defaultdict
import re

from pprint import pprint

def process_emojis(emoji_dict, common):
    '''
    Return most common emojis
    '''
    common_emojis_per_person = {}
    for name, emoji_list in emoji_dict.items():
        common_emojis = dict(Counter(emoji_list).most_common(common))
        total = len(emoji_list)
        common_emojis_per_person[name] = {'total': total,
                                          'top': common_emojis}
    return common_emojis_per_person


def process_words(words_dict, common):
    '''
    Return most common words
    '''
    common_words_per_person = {}
    for name, words_list in words_dict.items():
        common_words = dict(Counter(words_list).most_common(common))
        total = len(words_list)
        common_words_per_person[name] = {'total': total,
                                         'top': common_words}
    return common_words_per_person


def process_line(line, min_word_limit, ignore_words):
    '''
    Filter words for short ones and unwanted words
    '''
    words = line.split()
    ignore_words = ignore_words or set()
    return map(lambda x: x.lower(), filter(lambda x: len(x) >= min_word_limit and x.lower() not in IGNORE_WORDS, words))


if __name__ == "__main__":

    IGNORE_WORDS = {'<media', 'omitted>'}
    EMOJI_REGEX = re.compile(r'([\u263a-\U0001f645])')

    parser = argparse.ArgumentParser(description='Process whatsapp messages')
    parser.add_argument('--filename', action='store', required=True)
    parser.add_argument('--app', choices=['whatsapp', 'hike'],
                        help='Name of the app. E.g. whatsapp or hike', default='whatsapp')
    parser.add_argument('--entity', choices=['word', 'emoji'],
                        help='Entity to count. E.g. word or emoji', default='emoji')
    parser.add_argument('--min-word-limit', action='store', type=int,
                        help='Minimum word limit for processing', default=4)
    parser.add_argument('--common', action='store', type=int,
                        help='Number of top items', default=10)

    args = parser.parse_args()

    words_dict = defaultdict(list)
    emoji_dict = defaultdict(list)
    message_count = 0

    app = args.app
    entity = args.entity
    filename = args.filename
    min_word_limit = args.min_word_limit
    common = args.common

    if app == "whatsapp":
        MATCH_REGEX = re.compile(
            r"(?P<date>.*?), (?P<time>.*?) - (?P<name>\w+): (?P<text>.*)")
    elif app == "hike":
        MATCH_REGEX = re.compile(
            r"(?P<date>.*?) (?P<time>.*?):(?P<name>\w+)- (?P<text>.*)")

    with open(filename) as f:
        for index, line in list(enumerate(f)):
            line = line.strip()
            match = MATCH_REGEX.match(line)
            if match:
                message_count += 1
                name, message = match.group('name'), match.group('text')
                words_dict[name].extend(process_line(
                    message, min_word_limit, ignore_words=IGNORE_WORDS))
                emojis = EMOJI_REGEX.findall(line)
                if emojis:
                    emoji_dict[name].extend(emojis)

    if message_count:
        print("Analyzed {} messages ".format(message_count))
        if entity == "emoji":
            pprint(process_emojis(emoji_dict, common))
        elif entity == "word":
            pprint(process_words(words_dict, common))
    else:
        print("Hmm! No messages found. Did you pass wrong name of the app?")
