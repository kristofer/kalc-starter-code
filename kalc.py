# kalc.py
class Kalc:
    def __init__(self):
        self.done = False
        self.input = ""
        self.welcome()

    def welcome(self):
        print("Welcome to Kalc")

    def run(self):
        while not self.done:
            self.input = input()
            if self.input == "exit":
                self.done = True
        print("Goodbye!")


if __name__ == "__main__":
    kalc = Kalc()
    kalc.run()
