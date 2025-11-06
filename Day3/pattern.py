# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())


char = ".|."
welcome = "WELCOME"
count = 1             

def insert_char(num): 
    return char*num
    
#create a nxm grid
for a in range(n):      
    if n // 2 == a:     
        print(welcome.center(m, "-"))   
    else:
        print(insert_char(count).center(m, "-"))    
        if (n//2-1) > a:
            count += 2
        elif n//2 < a:
            count -= 2
        else:
            pass


#https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
