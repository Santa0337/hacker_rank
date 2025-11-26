def wrapper(f):
    def fun(l):
        # complete the function
        new = []
        for number in l:
            num = number[-10:]
            new.append("+91 " + num[:5] + " " + num[-5:])
        return f(new)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

#https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem?isFullScreen=true
