class Glassware:
    def __init__(self, name):
        self.name = name

class Beaker(Glassware):
    def __init__(self, name, amount, status="not lost"):
        super().__init__(name)
        self.amount = amount
        self.status = status

class Tray:
    def __init__(self, name):
        self.name = name
        self.Beaker = Beaker("beaker", 5)

    def user_choice(self):
        choice = input("Do you want to delete the beaker? (yes/no): ")
        self.choice = choice
        if choice.lower() == "yes":
            self.Beaker.status = "lost"
            self.status = "deleted"
            self.Beaker.amount = 0
        else:
            self.Beaker.status = "not lost"
            self.status = "not deleted"

tray = Tray("My Tray")

tray.user_choice()
print(f"the tray is {tray.status}.")
print(f"the beaker is {tray.Beaker.status}.")