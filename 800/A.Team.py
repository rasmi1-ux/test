
def team(n):
    counter = 0
    if n <1 or n > 1000:
        return "Invalid input. n must be between 1 and 1000."
    for i in range(n):
        a,b,c= map(int, input().split())
        if a+b+c >= 2:
            counter += 1
    return counter







n=int(input())
print(team(n))