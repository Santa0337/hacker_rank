if __name__ == '__main__':
    l=[]
    s=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        s.append(score)
        l.append([name,score])
    l.sort()
    s=sorted(set(s))
    t=s[1]
    for i,j in l:
        if j==t:
            print(i)

#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
