if __name__ == '__main__':
    s = input()
    has_alnum = bool()
    has_alpha = bool()
    has_digit = bool()
    has_lower = bool()
    has_upper = bool()

    for ch in s:
        if ch.isalnum(): has_alnum = True
        if ch.isalpha(): has_alpha = True
        if ch.isdigit(): has_digit = True
        if ch.islower(): has_lower = True
        if ch.isupper(): has_upper = True

    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)

#https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
