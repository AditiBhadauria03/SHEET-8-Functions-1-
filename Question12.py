# Pythagoras Theorem

def pythagoras(a, b):
    return (a*a + b*b) ** 0.5

a = float(input("Enter base: "))
b = float(input("Enter height: "))

hyp = pythagoras(a, b)
print("Hypotenuse =", hyp)
