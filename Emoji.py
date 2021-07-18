message = input("> ")

emojis = {
    ":)": "🙂",
    ":(": "☹"
}

words = message.split(' ')
output = "";
for word in words:
    output += emojis.get(word, word) + " "

print(output)