def diagonalDifference(arr):
    # Write your code here
    r=0
    l=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i==j:
                r+=arr[i][j]
        for k in range(len(arr[i])-1,-1,-1):
            if k == (len(arr[i]) - 1 - i):
                l+=arr[i][k]
    return abs(r-l)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
#https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
