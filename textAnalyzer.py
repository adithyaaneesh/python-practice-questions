#2. Create a Text Analyzer that counts words, characters, and sentences in a paragraph.

import re
def textAnalyzer(paragraph):
    character = len(paragraph)
    word = len(paragraph.split())
    sentence = len(re.split(r'[.?!]', paragraph))-1
    print("characters", character)
    print("words", word)
    print("Sentences",sentence)

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s."
textAnalyzer(text)
