def print_rangoli(size):
    # your code goes here
        w = 4*n-3
        chars = []
        line = ""
        lines = []
        for i in range(n):
            chars.append(chr(96+(n-i)))
            line = "-".join(chars + chars[-2::-1])
            lines.append(line.center(w,"-"))

        print("\n".join(lines + lines[-2::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
