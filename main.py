#Dictionary  is a key value pair data structure in python. It is mutable and unordered. It is defined by using curly braces {} and key-value pairs are separated by a colon (:).

#computer - Something i use to write code and run programs.
#Word                 Meaning
#key                  Value

freinds = {
    "Daneil":"A good friend who is always there for me.",
    "Finley":"A friend who is always ready to help me.",
    "Scarlett":"A friend who is always there to listen to me.",
}
print(freinds["Scarlett"])

print(freinds["Daneil"])


print("Hello there,Enter your name or your friend you want to know .")
print(f"({freinds.keys()})")

name = input("Enter your name ")

value = freinds[name]

print(f" here's what i like about {name} : {value}")



#homework
#create a languge translator
#with a differnt language
#ask the user what the word they want to translate
# the translatged word can be in any language


















translations = {
    "hello": {
        "french": "bonjour",
        "spanish": "hola",
        "german": "hallo",
        "yoruba": "bawo"
    },
    "goodbye": {
        "french": "au revoir",
        "spanish": "adios",
        "german": "auf wiedersehen",
        "yoruba": "odabo"
    },
    "thank you": {
        "french": "merci",
        "spanish": "gracias",
        "german": "danke",
        "yoruba": "e se"
    }
}

word = input("What word do you want to translate? ").lower()

language = input(
    "What language do you want to translate it into? "
    "(French, Spanish, German or Yoruba): "
).lower()

if word in translations:
    if language in translations[word]:
        print("The translated word is: " + translations[word][language])
    else:
        print("Sorry, that language is not available.")
else:
    print("Sorry, that word is not in the translator.")