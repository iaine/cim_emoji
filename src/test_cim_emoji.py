import unittest
#sys.path.insert(1, '../src')
from cim_emoji import CIMEmoji as cim

class TestEmojiMethods(unittest.TestCase):

    def test_load_codes(self):
        self.assertGreater(len(cim().codes), 0)

    def test_string_find_emoji(self):
        test_string = 'We 😊 want 😅 to  emojis '
        emojis = cim().find_all_emoji (test_string)
        self.assertEqual({'😅': 'grinning face with sweat', '😊': 'smiling face with smiling eyes'}, emojis)

    #def test_string_find_emoji_position(self):
    #    test_string = 'We 😊 want 😅 to 😏 extract 😁 these 😀 emojis '
    #    emojis = cim().find_all_emoji(test_string)
    #    self.assertEqual({2,5,7,8,9}, emojis)

    def test_emoji_collocation(self):
        test_string = 'We 😊 want 😅 to 😏 extract 😁 these 😀 emojis '
        pos = cim().find_emoji_collocation(test_string, '😊')
        self.assertEqual(["want"], pos)

    def test_emoji_collocation_before(self):
        test_string = 'We 😊 want 😅 to 😏 extract 😁 these 😀 emojis '
        pos = cim().find_emoji_collocation(test_string, '😊', direction="before")
        self.assertEqual(["We"], pos)

    def test_emoji_collocation_many(self):
        test_string = 'We 😊 want 😅 to 😏 have all 😊 cake'
        pos = cim().find_emoji_collocation(test_string, '😊')
        self.assertEqual(["want", "cake"], pos)

    def test_emoji_collocation_many_before(self):
        test_string = 'We 😊 want 😅 to 😏 have all 😊 cake'
        pos = cim().find_emoji_collocation(test_string, '😊', direction="before")
        self.assertEqual(["We", "all"], pos)

        
if __name__ == '__main__':
    unittest.main()