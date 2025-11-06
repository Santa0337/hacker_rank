def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        s = string[i:i+k]                   
        l = []
        for ch in s:                      
            if ch not in l:
                l.append(ch)
        print(''.join(l))    
    
    
        
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
