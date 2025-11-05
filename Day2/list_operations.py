if __name__ == '__main__':
    N = int(input())
    l = []      

    def performOperation(cmdList):
        match cmdList[0]:
            case 'insert': l.insert(int(cmdList[1]),int(cmdList[2]))                            
            case 'append': l.append(int(cmdList[1]))
            case 'remove': l.remove(int(cmdList[1]))
            case 'sort': l.sort()
            case 'pop': l.pop()
            case 'reverse': l.reverse()
            case 'print': print(l)
            case _: return

    for i in range(N):
        cmd = input()        
        performOperation(cmd.split(" "))

#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
