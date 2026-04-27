def watermelon(weight):
    if weight < 0 or weight >100:
        return "NO"
    if weight > 2 and weight % 2 == 0:
        return "YES"
    else:
        return "NO"
    
print(watermelon(8))