from math import sqrt

def fibonacci(n):
    sqrt_5 = sqrt(5)
    result = ((1 + sqrt_5) / 2) ** n
    result -= ((1 - sqrt_5) / 2) ** n
    result /= sqrt_5
    return result

def  main():
    n = int(input().strip())
    print('%.1f' % fibonacci(n))

if __name__ == '__main__':
    main()