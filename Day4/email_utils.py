import re
import email.utils

n = int(input())
pattern = r"[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}"
for _ in range(n):
    mail = email.utils.parseaddr(input())
    if re.fullmatch(pattern, mail[1]):
        print(email.utils.formataddr((mail[0], mail[1])))

#https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true
