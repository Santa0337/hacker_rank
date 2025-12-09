#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    arr=ar
    ans=[]
    arr=list(set(arr))
    for i in arr:
        ans.append(ar.count(i)//2)
    return sum(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
#https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true
