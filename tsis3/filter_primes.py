import math


def main():
    n = int(input())
    nums = list(filter(lambda x: all(x%i != 0 for i in range(2, x)), range(2,n+1)))
    print(nums)


if __name__ == "__main__":
    main()
