import json
import urllib.request
import re
#fix context
import ssl
context = ssl._create_unverified_context()

class CIMEmojiHelpers():


    URL = "https://unicode.org/Public/draft/emoji/emoji-test.txt"

    VERSION_URL="https://unicode.org/Public/emoji/{}/emoji-test.txt"

#@todo: add exception for the version issue. 
    def __init__(self):
        pass

    def _get_codes(self):
        '''
        Helper to load into memory
        '''
        with open("codes.json", "r") as f:
            return json.loads(f.read())
        
    def _create_regex_string (self, codes):
        escaped = (re.escape(c) for c in sorted(codes, key=len, reverse=True))
        return re.compile(r"|".join(escaped))

    #download functions below

    def parse_file(data, code):
        '''
        Parse the incoming data
        '''

        if data.strip() != "" and not data.startswith("#"):
            codes, desc = data.split(';', 1)
            _, desc = desc.split('#', 1)
            desc = desc.split(" ", 3)[-1]
            #yield(codes.strip(), desc.strip())
            if ".." in codes.strip():
                for cp in self.parse_unicode_range(codes):
                    code[cp] = desc.replace("\n","")
            else:
                code[self.parse_unicode_sequence(codes)] = desc.replace("\n","")
        return code

    def parse_unicode_sequence(string):
        return "".join((chr(int(i.zfill(8), 16)) for i in string.split()))


    def parse_unicode_range(string):
        start, _, end = string.partition("..")
        start, end = map(lambda i: int(i.zfill(8), 16), (start, end))
        return (chr(i) for i in range(start, end + 1))

    def _write_data (codes):
        with open("./codes.json", "w") as f:
            json.dump(codes, f, separators=(",", ":"))

    def download(version=""):
        """
        Download the correct chart
        """
        target_url = URL
        if version != "":
            VERSION=version
            target_url = VERSION_URL.format(VERSION)

        code={}
        for line in urllib.request.urlopen(target_url, context=context):
            code = self.parse_file(line.decode('utf-8'), code)

        _write_data(code)
