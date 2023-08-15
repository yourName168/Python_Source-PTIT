import math

def solve_quadratic(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        x = -b / (2*a)
        return x, x
    else:
        return None
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
solutions = solve_quadratic(a, b, c)

if solutions is None:
    print("Phương trình vô nghiệm.")
elif len(solutions) == 1:
    print("Phương trình có nghiệm kép x =", solutions[0])
else:
    print("Phương trình có 2 nghiệm phân biệt:")
    print("x1 =", solutions[0])
    print("x2 =", solutions[1])
