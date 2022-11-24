# https://www.hackerrank.com/challenges/python-print

if __name__ == '__main__':
    n = int(input())

    #while n is in range of 1 to 151
    while n in range (1,151):
        #print the numbers from 1 to n
        for i in range(1,n+1):
            #print range from 1 to n as consecutive numbers
            print(i, end='')
        break