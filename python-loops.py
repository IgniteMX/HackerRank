# https://www.hackerrank.com/challenges/python-loops/

if __name__ == '__main__':
    n = int(input())

    while n in range(1,20):
        for i in range(0,n):
            print(i**2)
        break