def neverDecrease(n):
    num = [int(x) for x in str(n)]
    for i,j in zip(num, num[1:]):
        if i > j:
            return False
    return True
    # return all(int(a[x])<=int(a[x+1]) for x in range(len(a)-1))  

def hasTwoAdjacents(n):
    num = [int(x) for x in str(n)]
    if num[0] == num[1] and num[1] != num[2] or num[-1] == num[-2] and num[-2] != num[-3]:
        return True
    for i, j, k, l in zip(num, num[1:], num[2:], num[3:]):
        if i != j and j == k and k != l:
            return True
    return False

def countPassword(min, max):
    count = 0
    for password in range(min, max):
        if neverDecrease(password) and hasTwoAdjacents(password):
            count += 1
    return count

count = countPassword(206938, 679128)
print("There is " + str(count) + " passwords meeting those criterias.")
