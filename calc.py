# Author: Mitch Allen

# -----------------------
# calc class

class Calc:
    
    # Constructor
    def __init__(self):
        self.acc = 0

    def showTotal(self):
        print(f"total: {self.acc:.2f}")

    def add(self,value):
        self.acc += value
        self.showTotal()

    def sub(self,value):
        self.acc -= value
        self.showTotal()

    def run(self):

        while True:

            line = input("Enter a command (add, sub, quit):\n:> ")
            
            args = line.split()

            if len(args) < 1:
                return
            
            command = args[0]

            if len(args) > 1:
                strValue = args[1]
                try: 
                    value = float(strValue)
                except ValueError:
                    print(f"{strValue} must be a floating point value!")
                    return
                
            match command:
                case 'add':
                    self.add(value)
                case 'sub':
                    self.sub(value)
                case 'quit':
                    print("Bye!")
                    return
                
            print()  # new line to keep things clean