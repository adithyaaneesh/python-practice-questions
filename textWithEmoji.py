#5. Create a Python program that replaces certain words in a text with emojis.

emoji = {
    "happy" : "😀",
    "sad" : "😒",
    "super" : "👌",
    "ok" : "👍"
}
def textreplace():
    text = "are you happy now? if no, then why are you so sad ? nothig!! so you are super cool ok"
    text = str(input("Enter the text you want to replace: "))
    # text = "I am super happy today, but my friend is sad. It's ok, we will still have a super day!"
    for word,emj in emoji.items():
        text = text.replace(word,emj)
        text = text.replace(word.capitalize(),emj)
        text = text.replace(word.upper(),emj)
        text = text.replace(word.lower(),emj)
    return text
print("Converted text : ",textreplace())

