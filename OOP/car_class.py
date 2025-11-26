class Car:
    wheeels = 4

    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def Drive(self):
        print(f"Drive the {self.model}")

    def Park(self):
        print(f"Park the {self.model}")
