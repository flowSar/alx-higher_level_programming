#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys as syst
    argc = len(syst.argv)
    if argc < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        if syst.argv[2] == '+':
            a = int(syst.argv[1])
            b = int(syst.argv[3])
            print("{} + {} = {}".format(a, b, calc.add(a, b)))
        elif syst.argv[2] == '-':
            a = int(syst.argv[1])
            b = int(syst.argv[3])
            print("{} - {} = {}".format(a, b, calc.sub(a, b)))
        elif syst.argv[2] == '*':
            a = int(syst.argv[1])
            b = int(syst.argv[3])
            print("{} * {} = {}".format(a, b, calc.mul(a, b)))
        elif syst.argv[2] == "/":
            a = int(syst.argv[1])
            b = int(syst.argv[3])
            print("{} / {} = {}".format(a, b, calc.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            syst.exit(1)
