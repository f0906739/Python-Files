# Decorator Tutorial
class memify():
    message = "HELLO WORLD"

    def xdec(self, func, num_of_xs):
        def wrapper(*args):
            print("X"*num_of_xs)
            print(func(*args))
            print("X"*num_of_xs)
        return wrapper

    def meme(self, string):
        string = string.lower()
        indices = list(range(0, len(string)))
        enumerated = tuple(zip(string, indices))
        return "".join([letter.capitalize() if index % 2 == 0 else letter for letter, index in enumerated])

    def tax(self, item, cost):
        return f"Cost for {item}: ${cost}.\nTaxes: {cost*0.05}"

    def run(self):
        self.xdec(self.meme, len(self.message))(self.message)
        item = "bear"
        self.xdec(self.tax, len(item))(item, 5)


memify().run()
