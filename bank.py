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

