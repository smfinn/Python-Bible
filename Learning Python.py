## Learning Python

#******************************************************************************#
#******************************************************************************#
# 1. Basics
#******************************************************************************#
#******************************************************************************#

print(1 + 1)
## Won't show result on IDLE without print command.

two = 1 + 1
print(two)
## 'two' is now a variable

message = "Great job, this is the end of section 2!"
print(message)

## Examine variable type or class by using type command
type(two)
type(message)

#******************************************************************************#
#******************************************************************************#
# 2. Numbers
#******************************************************************************#
#******************************************************************************#

type(1)
## integers are of type 'integer'

type(1.1)
## any other numbers are of type 'float'

10 % 2
11 % 2
## modulo function (%) outputs the remainder of a division

print(round(1.4))
print(round(1.8))
## round to the closest integer

import math
print(math.floor(1.5))
## math module floor command rounds down to next lowest integer

print(math.ceil(1.2))
## math module ceil (for ceiling) command rounds up to next integer

math.pi
math.e
math.sin(0)
math.cos(0)
math.tan(1)
math.pow(2, 2)
math.pow(81, 1)
math.log(math.e)
math.exp(1)
## math module stores some important numbers, functions, and constants


#******************************************************************************#
##### PROJECT 1: Crafting a Health Potion #####

import random
## use import fcn for new module; this one generates random numbers
## use F1 to pull up Python help book

health = 50
potion_health = random.randint(25, 50)
## must use the name of the module before the module's command
## randint takes the lower and upper ends of the draw pool (integers)

health = health + potion_health
print(health)

difficulty = 1
## 1 is easy, 2 is medium, 3 is hard

potion_health = random.randint(25, 50) / difficulty
## when Python divides, it always produces a float type

potion_health = int(potion_health)
## convert potion_health variable to integer; this is called "casting"

## The health potion provides a lower amount of health, on average, depending
## the player's difficult level.




#******************************************************************************#
#******************************************************************************#
# 3. Strings
#******************************************************************************#
#******************************************************************************#

name = "Sean"
print(type(name))

message = 'John said to me, "I will see you later."'
## Strings can be opened with single or double quotes

longmessage = """Out of the night that covers me
Black as the pit from pole to pole,
I thank whatever gods may be
For my unconquerable soul.

In the fell clutch of circumstance
I have not winced nor cried aloud.
Under the bludgeonings of chance
My head is bloody, but unbowed.

Beyond this place of wrath and tears
Looms but the Horror of the shade,
And yet the menace of the years
Finds and shall find me unafraid.

It matters not how strait the gate,
How charged with punishments the scroll,
I am the master of my fate,
I am the captain of my soul."""
## Multi-line strings can be opened with triple quotes

hello = "Hello world!"
print(hello)


#******************************************************************************#

##### PROJECT 2: Hello You! #####

## Ask user for their name
name = input("What is your name?: ")

## Ask user for their age
age = input("What is your age?: ")

## Ask user for their city
city = input("What city do you live in?: ")

## Ask user what they enjoy doing
hobby = input("What do you like to do?: ")

## Create output text
sentence = name + " is " + age + " years old, lives in " + city + ", and likes to " + hobby

## Print output to screen
print(sentence)

## Do again usin format command
new_sentence = "{} is {} years old, lives in {}, and likes to {}."
output = new_sentence.format(name, age, city, hobby)
print(output)



#******************************************************************************#
# String methods

### "string".method()
text = "happy birthday"
text.count("a")
text.count("happy")
## count the number of the string component in the preceding string

x = "Happy Birthday"
print(x.lower())
print(x.upper())
## transform string to all upper- or lower-case

print(x.capitalize())
## capitalize the first letter of the string

print(x.title())
## capitalize each word in the string

x.islower()
x.isupper()
x.istitle()
## logic checks for capitalization

x.isalpha()
"abc".isalpha()
## logic check for whether string is all letters

x.isdigit()
"123".isdigit()
## logic check for whether stirng is all numbers

x.isalnum()
"Happy24thBirthday".isalnum()
## logic check for whether string is all letter or numberic

x.index("Birthday")
x.index("y")
## returns place in string where specified value is found (case-sensitive)

x.find("Birthday")
x.find("lalala")
## similar, but returns -1 if specified value isn't found (instead of error)

string = "00 BY16092 00"
string.strip("0")
## strip zeros from string (or any other specified value)

string.rstrip("0")
string.lstrip("0")
## strip zeros from left or right side of string only

string = string.strip("0")
plate = string.strip()
print(plate)
## strip blank spaces from beginning or end of string

lngth = len(plate)
print(type(lngth))
## returns the length of the string, as an integer

word = "supercalifragilisticexpialidocious"
word[0]
## return the 0th index of the string - the first element

## HOW TO SLICE: stringvar[start:end(not inclusive):step]
word[0:5:1]
word[5:9:1]
word[5:]
## leave start or end blank to indicate beginning or end of string



#******************************************************************************#
##### PROJECT 3: Email Slicer #####

## Ask user for email
email = input("What is your email address?: ").strip()

## Slice up parts of email address
username = email[:email.index("@")]
domain = email[email.index("@")+1:]

## Output the email address pieces
print("Your username is {} and domain name is {}".format(username,domain))



#******************************************************************************#
#******************************************************************************#
# 4. Logic and Conditional Flow
#******************************************************************************#
#******************************************************************************#

B = True
C = False
print(type(B))
## Must use these capitalizations -- neither TRUE nor false will work

print(2 > 3)
print(2 >= 2)
print(45 < 49)
print(1 <= -11)
print(17 != 17)
print(99 == 100 - 1)
## Normal rules of logic apply

## if [condition]: [command]
if True: ## will execute the command anytime the condition after if is True
    print(2 + 2)

num1 = 100
num2 = 150
if num1 > num2 :
    print("The first number is bigger")
else :
    print("The second number is bigger than or equal to the first")

## What if the two numbers are equal?
if num1 > num2 :
    print("The first number is bigger")
elif num2 > num1 :
    print("The second number is bigger")
else :
    print("Both numbers are equal")
## can have any number of conditions through elif commands

print(not True)
print(not False)
## gives the reverse

if not num1 < 0 :
    print("it worked!")
## not operator reverses the veracity of the following statement

if num1 > 0 and num2 > 0 :
    print("both numbers are positive")
## and operator works as expected

if num1 > 0 or num2 > 0 :
    print("at least one of the numbers is positive")
## so does the or operator

if num1 < 0 or num2 < 0 :
    print("at least one of the numbers is negative")
## no output

if not (num1 < 0 and num2 < 0) :
    print("we did the reverse and still found the numbers are positive!")
## can use parentheses to compartmentalize logic statements

False or True
## returns True

False or (True or False)
## returns True



#******************************************************************************#
#******************************************************************************#
# 5. Data structures
#******************************************************************************#
#******************************************************************************#

#******************************************************************************#
# Lists

our_list = [1,2,3,4,5]
new_list = [-5, 17, 99, -4, -25]
print(type(our_list))

jackson = ["A", "B", "C", 1, 2, 3, "Do", "Rey", "Mi", True, False]
## can combine data types in the same list

jackson[1]
## returns first element of the list

jackson[-1]
## returns the last element of the list

jackson_letters = jackson[0:3:1]
jackson_letters = jackson[:3]
## these are equivalent

new_list = new_list + jackson_letters
## combine lists together using the addition operator

nested_list = [1, 2, [3.1, 3.2, 3.3, 3.4], 4, 5]
print(nested_list[3])
## gives the third element of the list, which is another list!
print(nested_list[3][0])
## gives first element of the nested list

table = [[1,2,3], [4,5,6], [7,8,9]]
print(table[0], table[1], table[2])
print(table[1][1])
## helpful for manipulating tables sometimes

## table = table + 1
## can't add non-lists to lists

table = table + [1]
## this works to make 1 a list

table = table + list("table")
print(table)
## each element of the string "table" will be added as list elements

table = table + [list("table")]
print(table)
## enters the string "table" as its own nested list

basic = [1,2,3,4,5]
basic.insert(3,"After 3")
## insert elements into list, instead of adding to the end
## NOTE that you do NOT set list equal to itself to edit, like variables



#******************************************************************************#
##### PROJECT 4: Travis the Ridiculous Security System #####

users = ["Sean", "Nolan", "Dan", "Ziyad"]
print(len(users))

switch = True

while (switch == True) :
    answer = 'yes'
    print("Hi! My name is TRAVIS.")
    name = input("What is your name?: ").strip().capitalize()
    
    if (name in users) :
        print("Hello, {}!".format(name))
    else :
        print("Hi, {}. You are not a recognized user.".format(name))
        answer = input("Add user to list (yes/no)? ").strip().lower()
        
    if (answer == 'yes') :
        print("SECURITY CHECKPOINT PASSED. Welcome to your system!")
        if name not in users :
            users.append(name)
        print("User list: ", users)
    else :
        print("Goodbye!")

    keep_going = input("Would you like to continue with another sign-in (yes/no)? ").strip().lower()
    if keep_going == 'no' :
        print("Goodbye!")
        switch = False



#******************************************************************************#
# Tuples

## immutable data type; they are like lists, but can't be changed once created
our_tuple = (1,2,3,'A','B','C')
type(our_tuple)

our_tuple[0:3]
## slicing rules apply the same for tuples

our_list = [1,2,3]
our_list[0] = 77
print(our_list)
## can change elements of list, but this code doesn't work for tuples

(A,B,C,D,E,F,G) = [1,2,3,4,5,6,7]
## assigns each tuple element the corresponding list value (works for any iterable data type)

new_tuple = tuple(our_list)
## can easily convert lists to tuples, which ensures they don't get edited



#******************************************************************************#
# Dictionaries

students = {"Sean":24, "Dan":25, "Nolan":30}
## made up of comma-separated items, each item has a key followed by its value(s)

print(students["Dan"])
## return the value associated with that key

students["Guinness"] = 8
## adds new key and associated value to dictionary

del students["Sean"]
## remove key and associated values from dictionary

students.keys()
## look at keys in dictionary

student_names = list(students.keys())
student_ages = list(students.values())
## converts these into lists that can be used and manipulated
## this is helpful because dictionaries aren't indexed - can't slice them

student_records = list(students.items())
## creates tuple of each item in dictionary, compiled into list

students = {
    "Sean":["ID0094", 24, 'A+'],
    "Dan":["ID0069", 25, 'C-'],
    "Nolan":["ID0420", 30, 'B']
    }
print(students["Dan"])
## store multiple values in each key; these become (indexed!) lists
print(students["Dan"][2])
## prints just the grade, since it is the third list item under "Dan"


students = {
    "Sean":  {"ID": "ID0094", "Age" :24, "Grade" :'A+'}, ## NOTE change [] to {}
    "Dan":   {"ID": "ID0069", "Age" :25, "Grade" :'C-'},
    "Nolan": {"ID": "ID0420", "Age" :30, "Grade" :'B'}
    }
## create sub-dictionaries to make elements easier to grab
print(students["Dan"]["Age"])
print(students["Sean"]["ID"], students["Sean"]["Grade"])



#******************************************************************************#
##### PROJECT 5: Cinema Simulator #####

films = {
    "Finding Dory" : {"Min. age": 0,    "Tickets": 5},
    "Bourne" :       {"Min. age": 13,   "Tickets": 5},
    "Tarzan" :       {"Min. age": 6,    "Tickets": 5},
    "Ghostbusters" : {"Min. age": 6,    "Tickets": 5}
    }

while True :

    choice = input("What film are you interested in seeing? ").strip().title()
    age = int(input("How old are you? ").strip())

    if choice in films :
        pass
    else :
        print("That film is not currently available for viewing")
        break

    if age >= films[choice]["Min. age"] :
        pass ## just move on
    else :
        print("Sorry, you are not old enough to view the chosen film")
        break
    
    if films[choice]["Tickets"] > 0 :
        print("Your ticket is reserved! Enjoy the movie.")
        films[choice]["Tickets"] = films[choice]["Tickets"] - 1
    else :
        print("Sorry, there are no tickets left for that film.")




#******************************************************************************#
#******************************************************************************#
# 6. Loops
#******************************************************************************#
#******************************************************************************#

#******************************************************************************#
# While loops

while False :
    print("Hello")
## nothing will happen because the command only execute when the condition is True

number = 1
while number <= 10 :
    print(number)
    number = number + 1
## print the numbers 1 through 10, because it increases by 1 each time

while number <= 100 :
    if number % 2 == 0 :
        print(number)
    number = number + 1
## print only even numbers between 0 and 100



#******************************************************************************#
##### PROJECT 6. Baby Conversation Simulator #####

import random
from random import choice
## this allows use of random() directly instead of needing to write random.choice()

questions = ["Why is the sky blue? ",
             "How do fish sleep? ",
             "Where do babies come from? ",
             "Why do people fight each other? ",
             "How does a car go? ",
             "How does a duck stay floating? "
             ]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because" :
    answer = input("Why? ").strip().lower()

print("Oh... okay!")



#******************************************************************************#
# For loops

numbers = range(1, 11, 1)
print(numbers)
## but what if I want to print the numbers separately

for number in range(1, 11):
    print(number)
## print numbers 1 through 10

for letter in "title":
    print(letter)
## print each character in the string

word = input("Please type any word: ").strip()
vowels = 0
consonants = 0

for letter in word :
    if letter.lower() in "aeiou" :
        vowels = vowels + 1
    elif letter.lower() == "":
        pass
    else :
        consonants = consonants + 1
        
print("There are {} vowels and {} consonants in the word {}".format(vowels, consonants, word))


students = {
    "human": ["Sean", "Nolan", "Dan"],
    "cat": ["Guinness", "Harp", "Belle"]
    }

for key in students.keys():
    print(key)
## output the name of each key in the above dictionary

for key in students.keys() :
    for name in students[key] :
        if "n" in name :
            print(name)
## print all the names that have the letter n in them, starting with humans then cats

even_numbers = [x for x in range(1,101) if x % 2 == 0]
## creates list of even numbers between 1 and 100

words = ["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog"]
answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer)
## putting the for loop inside the list makes it repeat over the inner list



#******************************************************************************#
##### PROJECT 7. Pig Latin Translator #####

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



#******************************************************************************#
#******************************************************************************#
# 7. Functions
#******************************************************************************#
#******************************************************************************#

def add(x,y):
    return x + y
## 'def' initiates function definition; 'add' is name of function;
## 'x' and 'y' are the parameters the function will take

print(add(5,10))
## this function will now give the summation of its two inputs

def reverser(text):
    return text[::-1]
print(reverser("awesome"), reverser([1,2,3,4,5,6,7,8,9]))
## make the input string go backwards

#******************************************************************************#
# Variable scope
a = 100
## defined globally - accessible from anywhere

def f1():
    print(a)

def f2():
    a = 50
    b = 4
    print(a)

print(f1())
print(f2())
print(a)
print(b)
## things created within the function are local - can't be used elsewhere

def f1():
    global a ## must a separate line
    a = 101
    print(a)
## have to tell Python that a will be written as global in its own line
## when working with lists and dictionaries, items can be edited/overwritten
## inside the function without the global keyword


#******************************************************************************#
# Keyword arguments and default parameters

def about(name,age,likes):
    sentence = "Meet {}, they are {} years old, and they like {}".format(name,age,likes)
    return sentence

about("Jeff", 24, "peanuts")
about(likes = "peanuts", age = 24, name = "Jeff")
## positional arguments follow the order of the defined function
## while keyword arguments use the names of the parameters to define the input

def about(name, age, likes = "Python"):
    sentence = "Meet {}, they are {} years old, and they like {}".format(name,age,likes)
    return sentence
## this adds a default into the function parameters
## any number of the input parameters can have defaults, but default values must
## be listed last in the parameter list

about("Jeff", 24)
## this uses the default for "likes"

def about(name = "Anon", age = 99, likes = "Python"):
    sentence = "Meet {}, they are {} years old, and they like {}".format(name,age,likes)
    return sentence
print(about())
## fully default version of this function


#******************************************************************************#
# Packing and unpacking variables

print(1,2,3,4,5)
numbers = [1,2,3,4,5]
print(numbers)
print(*numbers)
## this * effect is called unpacking - works on any iterable data

print("love")
print(*"love")
## separates out each component of the iterable data type

def add(*numbers):
    total = 0
    for number in numbers :
        total = total + number
    return(total)

add(1,3,5,7,9,11)
## this is packing - any quantity of inputs can be given, and they will be packed
## into a tuple for use in the function

scores = [99, 82, 77, 90, 89]
add(*scores)
## must unpack this list to input it into the function, where it gets added up

def about(name, age, likes):
    sentence = "Meet {}, they are {} years old, and they like {}".format(name,age,likes)
    return sentence

dictionary = {"name": "Sean", "age" : 24, "likes": "Python"}
print(about(**dictionary))
## one star for normal positional arguments, and two stars for keyword arguments
## the key in the dictionary becomes the keyword for the parameters

def foo(**kwargs): ## Python standard: kwargs = keyword arguments
    for key, value in kwargs.items():
        print("{}:{}".format(key,value))
foo(Harp = "orange", Guinness = "black")
## pack down keyword arguments into a dictionary



#******************************************************************************#
##### PROJECT 8. Tic Tac Toe #####

board = [" " for i in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])  
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()
    
print_board()
# here's our empty board!

def player_move(icon):
    if icon == "X" :
        number = 1
    elif icon == "O" :
        number = 2
    
    print("It is Player {}'s turn".format(number))
    print()
    
    choice = int(input("Where would you like to play (1-9)?: ").strip())
    if board[choice - 1] == " " :
        board[choice - 1] = icon
    else :
        print("That space is already taken! Try again.")
        print()

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon or \
        board[3] == icon and board[4] == icon and board[5] == icon or \
        board[6] == icon and board[7] == icon and board[8] == icon or \
        board[0] == icon and board[3] == icon and board[6] == icon or \
        board[1] == icon and board[4] == icon and board[7] == icon or \
        board[2] == icon and board[5] == icon and board[8] == icon or \
        board[0] == icon and board[4] == icon and board[8] == icon or \
        board[2] == icon and board[4] == icon and board[6] == icon) :
        return True
    else:
        return False

def is_draw() :
    if " " not in board :
        return True
    else :
        return False

while True : ## "game loop"
    print_board()
    player_move("X")
    print_board()
    if is_victory("X") :
        print("Condragulations, X wins!")
        break
    elif is_draw() :
        print("It's a draw!")
        break
    player_move("O")
    if is_victory("O") :
        print("Condragulations, O wins!")
        break
    


#******************************************************************************#
#******************************************************************************#
# 8. Object-Oriented Programming
#******************************************************************************#
#******************************************************************************#

# Objects and classes

## classes are the templates, and objects are the items/instances that come from them
## each class has features composed of states and methods

class Penny:
    value = 1.00
    color = "bronze"
    num_edges = 1
    diameter = 22.5
    thickness = 3.15
    heads = True
## these are all states

coin1 = Penny()
print(type(coin1))
print(coin1.value)
print(coin1.color)

coin1.color = "greenish"
print(coin1.color)
coin2 = Penny()
print(coin2.color)
## new objects from same class will keep default states, but objects can be edited

class Penny:

    def __init__(self, rare = False): ## constructor: refers to the specific object of this class

        self.rare = rare
        if self.rare :
            self.value = 1.25
        else :
            self.value = 1.00

        self.color = "bronze"
        self.num_edges = 1
        self.diameter = 22.5
        self.thickness = 3.15
        self.heads = True    

    def rust(self): ## define a new method; this is a Penny-specific method
        self.color = "greenish"

    def clean(self):
        self.color = "bronze"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __del__(self): ## destructor: gives conditions for destroying object
        print("Coin spent!")

coin1 = Penny()
print(coin1.color)
coin1.rust()
print(coin1.color)
coin1.clean()
print(coin1.color)
## We can rust and clean the coin to see the changes in color

print(coin1.heads)
coin1.flip()
print(coin1.heads)
## We can flip the coin and see whether the result is heads

del coin1
## And we can spend the coin by using the del method




#******************************************************************************#
##### PROJECT 9. Making Currency and a Bank! #####


class Coin:

    def __init__(self, rare = False, clean = True, heads = True, **kwargs):

        for key,value in kwargs.items() :
            setattr(self,key,value) # flexible way of initializing long list of arguments

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else :
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else :
            self.color = self.rusty_color

    def rust(self): 
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __del__(self):
        print("Coin spent!")

    def __str__(self):
        return "${} Coin".format(float(self.original_value))

class Penny(Coin): ## this lets us inherit all the features from class Coin

    def __init__(self):

        data = {
            "original_value": 0.01,
            "clean_color": "bronze",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        }

        super().__init__(**data)
        ## packs the data by keywords into init function

class Nickel(Coin):

    def __init__(self):

        data = {
            "original_value": 0.05,
            "clean_color": "nickel",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 24.5,
            "thickness": 4.15,
            "mass": 12.5
        }

        super().__init__(**data)

class Dime(Coin):

    def __init__(self):

        data = {
            "original_value": 0.10,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges": 1,
            "diameter": 12.5,
            "thickness": 2.15,
            "mass": 4.5
        }

        super().__init__(**data)

        def rust(self):
            self.color = self.clean_color

        def clean(self):
            self.color = self.clean_color

        ## these override the inherited methods from Coin class
                
class Quarter(Coin):

    def __init__(self):

        data = {
            "original_value": 0.25,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges": 1,
            "diameter": 26.5,
            "thickness": 3.15,
            "mass": 11.5
        }

        super().__init__(**data)

        def rust(self):
            self.color = self.clean_color

        def clean(self):
            self.color = self.clean_color



coins = [Penny(), Nickel(), Dime(), Quarter()]
            
for coin in coins :
    arguments = [coin, coin.color, coin.value, coin.diameter, coin.thickness]
    string = "{}: color: {}, value: {}, diameter (mm): {}, thickness (mm): {}".format(*arguments)
    print(string)




class Account:

    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
        
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else :
            print("Not enough funds")

    def statement(self):
        print("Account balance: ${}".format(self.balance)) 


class Checking(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)

    def __str__(self):
        return "{}'s checking account: ${}".format(self.name, self.balance)

class Savings(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 25)

    def __str__(self):
        return "{}'s savings account: ${}".format(self.name, self.balance)



