if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i,j in student_marks.items():
        if i ==query_name:
            student_marks[query_name]=sum(j)/len(j)
    print(f"{student_marks[query_name]:.2f}")

#https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
