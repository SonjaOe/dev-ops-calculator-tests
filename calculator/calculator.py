def plus(luku1: float, luku2: float):
    if type(luku1) == str or type(luku2) == str:
        return "Please enter a number"
    return float(luku1 + luku2)

def minus(luku1: float, luku2: float):
    if type(luku1) == str or type(luku2) == str:
        return "Please enter a number"
    return float(luku1 - luku2)

def multiply(luku1: float, luku2: float):
    if type(luku1) == str or type(luku2) == str:
        return "Please enter a number"
    return float(luku1 * luku2)

def divide(luku1: float, luku2: float):
    if luku2 == 0:
        return "Cannot divide by zero"
    elif luku1 == 0:
        return 0
    elif type(luku1) == str or type(luku2) == str:
        return "Please enter a number"
    return float(luku1 / luku2)

