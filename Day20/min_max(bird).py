#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def migratoryBirds(arr):
    d={}
    for i in arr:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    m=[]
    ma=max(d.values())
    for k,v in d.items():
        if v==ma:
            m.append(k)
    return min(m)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
#https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true
