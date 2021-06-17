# Vowel and consonant counter

switch = "on"

print("Welcome to the vowel and consonant counter!")

while switch == "on" :

    word = input("What word would you like to ask about?: ").strip()
    vowels = 0
    consonants = 0

    for letter in word :
        if letter.lower() in "aeiou" :
            vowels = vowels + 1
        elif letter.lower() == "":
            pass
        else :
            consonants = consonants + 1
        
    print("There are {} vowel(s) and {} consonant(s) in the word {}".format(vowels, consonants, word))

    answer = input("Would you like to ask about another word (yes/no)? ").strip().lower()
    if answer == "no" :
        print("Okay, bye!")
        switch = "off"
