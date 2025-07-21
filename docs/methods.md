# Sample Methods

Each example assumes that you have import the CIMEmoji library

```
from cim_emoji import CIMEmoji as cim
```

### Find Emojis

A simple search for emojis within a string
```
test_string = 'We 😊 want 😅 to  emojis '
emojis = cim().find_all_emoji (test_string)
```
Emojis should present a dictionary along the lines of:
```
{'😅': 'grinning face with sweat', '😊': 'smiling face with smiling eyes'}
```

### Collocations with Emojis

find_emoji_collocation() has a paramter called direction. This is set to "after" but can be set to "before" to search before the emoji. 

##### Please note: very much in development

Building on the concept of collocations in digital methods.

```
test_string = 'We 😊 want 😅 to 😏 extract 😁 these 😀 emojis '
pos = cim().find_emoji_collocation(test_string, '😊')
```
would return a list of words, such as ```["want"]``` or if the direction parameter is set to before ```["We"]```

### Historical Emojis

##### Please note: very much in development

While the code focuses on the current dataset, it is possible to override this to get earlier ones. The list of them is at https://unicode.org/Public/emoji/.

```
version=16.0
download(version)
```
This will replace the existing codes for use. 