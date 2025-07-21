'''
Functions to read emoji
'''
import json
import re

from helpers import CIMEmojiHelpers

class CIMEmoji():

    def __init__(self):
        cim = CIMEmojiHelpers()
        self.codes = cim._get_codes()
        self.patterns = cim._create_regex_string(self.codes)


    def find_all_emoji (self, text_string):
        '''
        Find all emojis in string
        '''
        return {f: self.codes[f] for f in set(self.patterns.findall(text_string))}

    def find_single_emoji_code (self, text_string, emojicode):
        '''
        Find emoji by code in string
        '''
        return {f: self.codes[f] for f in set(self.patterns.findall(text_string)) if f == emojicode}

    def find_single_emoji_pattern (self, text_string, emojicode):
        '''
        Find emoji by pattern in string
        '''
        return {f: self.codes[f] for f in set(self.patterns.findall(text_string)) if codes[f] == emojicode}

    def find_emoji_collocation (self, text_string, emojicode, direction="after"):
        '''
        Find emoji by pattern in string
        '''
        found = []
        list_of_words = text_string.split()
        if direction == "before":
            #[m.start() for m in re.finditer(emoji, text_string)]
            found.append(list_of_words[list_of_words.index(emojicode) - 1])
        else:
            found.append(list_of_words[list_of_words.index(emojicode) + 1])

        return found
    
