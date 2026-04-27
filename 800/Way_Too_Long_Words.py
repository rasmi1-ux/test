


def abbreviate(n):
    if n>100 or n<1:
        return "Invalid input"
    for i in range(n):
        s = input()

        if len(s)>10:
            print(s[0]+str(len(s)-2)+s[-1])
        else:
            print(s)

n = int(input())
abbreviate(n)