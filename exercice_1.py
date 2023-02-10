class Calculator:
    #[MODIF] Added to every function the 'self' argument to use tests class
    def __init__(self):
        self.name = "Calculator"

    def add(self, x, y):
        #[MODIF] Added try statement for max limit value reached
        try:
            #[MODIF] Added integer/float validation before returning add function value and raise value error statement
            if(isinstance(x, (int, float)) and isinstance(y, (int, float))):
                return x + y
            else:
                raise ValueError("Wrong parameter type")
        except UnboundLocalError as ule:
            raise UnboundLocalError("Max value limit reached")
        
    
    def subtract(self, x, y):
        #[MODIF] Added try statement for max limit value reached
        try:
            #[MODIF] Added integer/float validation before returning substract function value and raise value error statement
            if(isinstance(x, (int, float)) and isinstance(y, (int, float))):
                return x - y
            else:
                raise ValueError("Wrong parameter type")
        except UnboundLocalError as ule:
            raise UnboundLocalError("Max value limit reached")
        
    def multiply(self, x, y):
        #[MODIF] Added try statement for max limit value reached
        try:
            #[MODIF] Added integer/float validation before returning multiply function value and raise value error statement
            if(isinstance(x, (int, float)) and isinstance(y, (int, float))):
                return x * y
            else:
                raise ValueError("Wrong parameter type")
        except UnboundLocalError as ubl:
            print("Raised !!!!! Multiply" + x + y)
            raise UnboundLocalError("Max value limit reached")
    
    def divide(self, x, y):
        #[MODIF] Added try statement for max limit value reached
        try:
            #[MODIF] Added integer/float validation before returning divide function value and raise value error statement
            if(isinstance(x, (int, float)) and isinstance(y, (int, float))):
                return x / y
            else:
                raise ValueError("Wrong parameter type")
        except UnboundLocalError as ubl:
            raise UnboundLocalError("Max value limit reached")
    
    def power(self, x, y):
        #[MODIF] Added try statement for max limit value reached
        try:
            #[MODIF] Added integer/float validation before returning power function value and raise value error statement
            if(isinstance(x, (int, float)) and isinstance(y, (int, float))):
                result = 1       
                for i in range(y):
                    result *= x
                return result
            else:
                raise ValueError("Wrong parameter type")
        except UnboundLocalError as ubl:
            raise UnboundLocalError("Max value limit reached")

    def square_root(self, x):
        #[MODIF] Added try statement for max limit value reached
        try:
            #[MODIF]Added integer validation before returning square root function value and raise value error statement
            #       + verify that given value is higher than 0
            if(isinstance(x, (int, float)) and x >= 0) :
                if x == 0 or x == 1:
                    return x
                val = x
                precision = 0.0000001
                while abs(val - x / val) > precision:
                    val = (val + x / val) / 2
                    
                return val
            else:
                raise ValueError("Wrong parameter type")
        except UnboundLocalError as ubl:
            raise UnboundLocalError("Max value limit reached")

def calculate(operation, x, y):
    calculator = Calculator()

    if operation == "add":
        result = calculator.add(x,y)
    elif operation == "substract":
        result = calculator.subtract(x,y)
    elif operation == "multiply":
        result = calculator.multiply(x,y)
    elif operation == "divide":
        result = calculator.divide(x,y)
    elif operation == "power":
        result = calculator.power(x,y)
    elif operation == "square_root":
        result = calculator.square_root(x)
    return result

operation = input("Enter the operation you would like to perform (add, subtract, multiply, divide, square_root, power): ")
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the secod number : "))

print(calculate(operation, num1, num2))

num3 = input("Program continues ?")