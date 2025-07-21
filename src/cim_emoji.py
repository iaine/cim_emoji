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
        return {f: self.codes[f] for f in set(self.patterns.findall(text_string)) if self.codes[f] == emojicode}

    def find_emoji_collocation (self, text_string, emojicode, direction="after"):
        '''
        Find emoji by pattern in string
        '''
        found = []
        list_of_words = text_string.split()
        patter = re.compile(emojicode, re.UNICODE)
        if direction == "before":
            #locs = [m for m in patter.finditer(text_string)]
            #print(locs)
            found = [list_of_words[k-1] for k in range(len(list_of_words)) if list_of_words[k] == emojicode]
            #found.append(list_of_words[list_of_words.index(emojicode) - 1])
        else:
            #found.append(list_of_words[list_of_words.index(emojicode) + 1])
            found = [list_of_words[k+1] for k in range(len(list_of_words)) if list_of_words[k] == emojicode]

        return found
    
