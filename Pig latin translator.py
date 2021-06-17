# pig latin translator

switch = "on"

while switch == "on" :

# ask for words or sentence to be translated
    english = input("What would you like to translate?: ").strip().lower()

# split sentence into individual words
    words = english.split()

# loop throughwords and convert to pig latin
    new_words = [] # initialize empty list for translated words
    for myword in words :
        if myword[0] in "aeiou" :
            new_word = myword + "yay"
            new_words.append(new_word)
        else :
            vowel_pos = 0
            for letter in myword :
                if letter not in "aeiou" :
                    vowel_pos = vowel_pos + 1
                else :
                    break
            cons = myword[:vowel_pos]
            rest = myword[vowel_pos:]
            new_word = rest + cons + "ay"
            new_words.append(new_word)

# stick words back together
    piglatin = " ".join(new_words)

# output the final string
    print("TRANSLATION:")
    print(piglatin)

# ask whether the user would like to continue translating
    answer = input("Would you like to translate some more (yes/no)? ").strip().lower()
    if answer == "no" :
        switch = "off"
        print("Thank you and goodbye!")


