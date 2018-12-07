# Code to handle argument using argparse

import argparse

def fibn(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return b

def Main():
    parser = argparse.ArgumentParser(description="This is simple parser")
    parser.add_argument("num", help="number input for fibonachi", type=int)
    args = parser.parse_args()
    print("fibn({0})= {1}".format(args.num, fibn(args.num)))

if __name__ == "__main__":
    Main()