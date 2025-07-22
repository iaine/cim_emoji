"""
Helper functions for CIM Emoji. Download and caching code. 
"""
import json
import pathlib
import re
import ssl
import urllib.request
from urllib.error import URLError, HTTPError

from .exception import CIMException

context = ssl._create_unverified_context()

class CIMEmojiHelpers():
    """
    Helper classes
    """

    def __init__(self):
        self.url = "https://unicode.org/Public/emoji/latest/emoji-test.txt"
        self.version_url="https://unicode.org/Public/emoji/{}/emoji-test.txt"
        self.codes_cache = pathlib.Path(__file__).parent.parent.resolve() / "cim_emoji"

    def _get_codes(self):
        '''
        Helper to load into memory
        '''
        with open(self.codes_cache / "codes.json", "r", encoding="utf-8") as f:
            return json.loads(f.read())

    def _create_regex_string (self, codes):
        '''
        Creates the regex string for parsing later
        '''
        escaped = (re.escape(c) for c in sorted(codes, key=len, reverse=True))
        return re.compile(r"|".join(escaped))

    def parse_file(self, data, code):
        '''
        Parse the incoming data
        '''

        if data.strip() != "" and not data.startswith("#"):
            codes, desc = data.split(';', 1)
            _, desc = desc.split('#', 1)
            desc = desc.split(" ", 3)[-1]

            if ".." in codes.strip():
                for cp in self.parse_unicode_range(codes):
                    code[cp] = desc.replace("\n","")
            else:
                code[self.parse_unicode_sequence(codes)] = desc.replace("\n","")
        return code

    def parse_unicode_sequence(self, string):
        """
          Parse Unicode sequence.
        """
        return "".join((chr(int(i.zfill(8), 16)) for i in string.split()))


    def parse_unicode_range(self, string):
        """
          Parse Unicode range.
        """
        start, _, end = string.partition("..")
        start, end = map(lambda i: int(i.zfill(8), 16), (start, end))
        return (chr(i) for i in range(start, end + 1))

    def _write_data (self, codes):
        """
          Parse Unicode sequence.
        """
        with open(self.codes_cache / "codes.json", "w", encoding="utf-8") as f:
            json.dump(codes, f, separators=(",", ":"))

    def download(self, version="", store="true"):
        """
        Download the correct chart
        """
        target_url = self.url
        if version != "":
            target_url = self.version_url.format(version)

        code={}
        openurl = None
        try:
            openurl = urllib.request.urlopen(target_url, context=context)
        except HTTPError:
            if version != "":
                CIMException(f"{str(target_url)} could not be opened {str(openurl.code)}")
            else:
                CIMException(str(URLError))
        except URLError:
            if version != "":
                CIMException(f"{str(target_url)} could not be opened ")
            else:
                CIMException(str(URLError))


        for line in openurl:
            code = self.parse_file(line.decode('utf-8'), code)

        if store:
            self._write_data(code)
        else:
            return code
