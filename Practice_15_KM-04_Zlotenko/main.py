from factorial import factorial
import exp_root
from exp_root import exponentiation, root
from logarithm import logarithm


if __name__ == '__main__':
    print("Please choose one of the following functions: factorial(1), exp_root(2) or logarithm(3)")
    while True:
        try:
            user_input = int(input("Enter number 1, 2 or 3: "))
            break
        except ValueError:
            continue

    if user_input == 1:
        while True:
            try:
                n = int(input("Enter natural number: "))
                if n < 0:
                    continue
                print("Factorial is", factorial.fact(n))
                break
            except ValueError:
                continue
    elif user_input == 2:
        print("Choose if you want to raise a number to a power(1) or find number's root(2)")
        while True:
            try:
                user_input2 = int(input("Enter number 1 or 2: "))
                break
            except ValueError:
                continue
        if user_input2 == 1:
            print("Choose if you want to raise a number to the second power(2) or to the third(3).")
            while True:
                try:
                    user_input21 = int(input("Enter number 2 or 3: "))
                    break
                except ValueError:
                    continue
            if user_input21 == 2:
                while True:
                    try:
                        n = int(input("Enter a number: "))
                        print("The number is", exp_root.exponentiation.exp2(n))
                        break
                    except ValueError:
                        continue
            elif user_input21 == 3:
                while True:
                    try:
                        n = int(input("Enter a number: "))
                        print("The number is", exp_root.exponentiation.exp3(n))
                        break
                    except ValueError:
                        continue
        elif user_input2 == 2:
            print("Choose if you want to find square root(2) or cubic(3).")
            while True:
                try:
                    user_input22 = int(input("Enter number 2 or 3: "))
                    break
                except ValueError:
                    continue
            if user_input22 == 2:
                while True:
                    try:
                        n = int(input("Enter a number: "))
                        if n < 0:
                            continue
                        print("The number is", exp_root.root.root2(n))
                        break
                    except ValueError:
                        continue
            elif user_input22 == 3:
                while True:
                    try:
                        n = int(input("Enter a number: "))
                        print("The number is", exp_root.root.root3(n))
                        break
                    except ValueError:
                        continue
    elif user_input == 3:
        print("Choose if you want to find normal(1), natural(2) or decimal(3) logarithm.")

        while True:
            try:
                user_input3 = int(input("Enter number 1, 2 or 3: "))
                break
            except ValueError:
                continue
        if user_input3 == 1:
            while True:
                try:
                    a = float(input("Enter base a(a>0, а!=1): "))
                    b = float(input("Enter b(b>0): "))
                    if a < 0 or a == 1 or b<0:
                        continue
                    print("The logarithm is", logarithm.log(a,b))
                    break
                except ValueError:
                    continue
        elif user_input3 == 2:
            while True:
                try:
                    b = float(input("Enter b(b>0): "))
                    if b<0:
                        continue
                    print("The logarithm is", logarithm.ln(b))
                    break
                except ValueError:
                    continue
        elif user_input3 == 3:
            while True:
                try:
                    b = float(input("Enter b(b>0): "))
                    if b<0:
                        continue
                    print("The logarithm is", logarithm.lg(b))
                    break
                except ValueError:
                    continue

