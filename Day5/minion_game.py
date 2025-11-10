def minion_game(string): 
    vowels = ('A', 'E', 'I', 'O', 'U') 
    kevin_score = 0 
    stuart_score = 0 
    len_str = len(string)
    for i in range(len_str):
        if string[i] in vowels:
            kevin_score += (len_str - i)
        else:
            stuart_score += (len_str - i)

    if kevin_score > stuart_score:
        print(f'Kevin {kevin_score}')
    elif stuart_score > kevin_score:
        print(f'Stuart {stuart_score}')
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)

#https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
