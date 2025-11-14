def average(array):
    arr=list(set(array))
    c=sum(arr)/len(arr)
    return c
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
