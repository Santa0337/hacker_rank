s=input()
if(len(s)<= 1000) and s.isalnum():
    string_list = list(s)
    conditions = [any(st.lower() for st in string_list), any(st.upper() for st in string_list), any(st.isnumeric() for st in string_list)]
    if any(conditions):
        lower = sorted([st for st in string_list if st.islower() == True])     
        upper = sorted([st for st in string_list if st.isupper() == True])     

        odd = sorted([str(num) for num in string_list if num.isdigit() and int(num)%2 == 1])
        even = sorted([str(num) for num in string_list if num.isdigit() and int(num)%2 == 0])

        print(''.join(lower + upper + odd + even))

#https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true
