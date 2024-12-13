import math

def log(n, m):
    return math.log(n) / math.log(m)

def main():
    while True:
        n = double(input())
        m = double(input())
        print(log(n, m))

if __name__ == "__main__":
    main()
