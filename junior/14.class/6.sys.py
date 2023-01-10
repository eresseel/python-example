import sys

def osszeg(a, b):
    return a+b

if len(sys.argv) > 1:
    print(osszeg(int(sys.argv[1]), int(sys.argv[2])))

print("Siker")