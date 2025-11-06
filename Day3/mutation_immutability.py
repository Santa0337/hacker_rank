def mutate_string(string, position, character):
    stri=list(string)
    stri[position]=character
    stri=''.join(stri)
    return stri

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
