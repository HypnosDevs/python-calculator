class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        negativeA = 0
        negativeB = 0
        if a == 0 or b==0:
            return 0
        if a < 0:
            tmp = a
            a -= a
            a -= tmp
            negativeA = 1
        if b < 0:
            tmp = b
            b -= b
            b -= tmp
            negativeB = 1
        
        for i in range(b):
            result = self.add(result, a)
        if (negativeA == 1 and negativeB == 0) or (negativeA == 0 and negativeB == 1):
            tmp = result
            result -= result
            result -= tmp
        return result

    def divide(self, a, b):
        if b == 0:
            return "Error can't divide by zero"
        if a == 0:
            return 0
        result = 0

        negativeFlag = False
        if (a<0 and b>0) or (b<0 and a>0):
            negativeFlag = True
        
        if a < 0:
            tmp = a
            a -= a
            a -= tmp
         
        if b < 0:
            tmp = b
            b -= b
            b -= tmp

        while a >= b:
            a = self.subtract(a, b)
            result += 1
        
        if negativeFlag:
            tmp = result
            result -= result
            result -= tmp
        return result
    
    def modulo(self, a, b):
        if b == 0:
            return "Error: can't perform modulo by zero"
        
        negativeFlag = False
        
        if (a<0 and b>0) or (a<0 and b<0):
            negativeFlag = True
        if a < 0:
            tmp = a
            a -= a
            a -= tmp

        if b < 0:
            tmp = b
            b -= b
            b -= tmp


        while a >= b:
            a = self.subtract(a, b)
        
        if negativeFlag:
            tmp = a
            a -= a
            a -= tmp

        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))