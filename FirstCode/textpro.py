def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()

    if phrase.startswith(interrogatives):
        capitalized = capitalized + "?"
    return capitalized + ". "

results = []

while True:
    newText = input("Say something: ")
    if newText == '\end':
        break
    else:
        results.append(sentence_maker(newText))

print("".join(results))