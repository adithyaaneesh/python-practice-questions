#5. Create a Python program that replaces certain words in a text with emojis.

emoji = {
    "happy" : "😀",
    "sad" : "😒",
    "super" : "👌",
    "ok" : "👍"
}

def textreplace():
    text = "are you happy now? if no, then why are you so sad ? nothig!! so you are super cool ok"
    for word,emj in emoji.items():
        text = text.replace(word,emj)
    return text
print(textreplace())
