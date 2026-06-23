import sys

from satings import hello

if __name__ == '__main__':
    if len(sys.argv) == 2:
        hello(sys.argv[1])
    else:
        print("Usage: python say.py <name>")