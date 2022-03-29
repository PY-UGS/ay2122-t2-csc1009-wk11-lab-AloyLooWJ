class calculator:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        print("A = " + str(self.input1) + ", B = " + str(self.input2))
    
    def adder(self):
        value = self.input1 + self.input2
        print("A + B = " + str(value))
    
    def subtractor(self):
        value = self.input1 - self.input2
        print("A - B = " + str(value))
    
    def multiplier(self):
        value = self.input1 * self.input2
        print("A * B = " + str(value))
    
    def divider(self):
        if self.input2 < 1:
            print("Division not possible")
            return
        value = self.input1 / self.input2
        print("A / B = " + str(value))

    def clear(self):
        print("\nClearing values...")
        self.input1 = 0
        self.input2 = 0
        print("A = " + str(self.input1) + ", B = " + str(self.input2))
        
while 1:
    A = 0
    B = 0
    try:
        A = int(input("Enter value of A: "))
        B = int(input("Enter value of B: "))
    except:
        print("Invalid input")
        break
    test = calculator(A,B)

    print()
    test.adder()
    test.subtractor()
    test.multiplier()
    test.divider()
    test.clear()
    a = input("Exit? (y): ")
    if a == 'y' or 'Y' or 'yes' or 'Yes':
        break


