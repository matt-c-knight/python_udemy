def sentence_maker(phrase):
    interrogatives = ("how","what","why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}".format(capitalized)


results = []
while True:
    user_input = input("Say Something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))


print(results)

temps = [221, 234, 340, 230]

new_temps = []
for temp in temps:
        new_temps.append(temp / 10)

print(new_temps)

# list comprehensions 
newer_temps = [temp / 10 for temp in temps]

print(newer_temps)


   