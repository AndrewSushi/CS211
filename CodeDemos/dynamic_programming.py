memo = {}
def factorial(k):
    if k < 2: return 1
    if k not in memo:
        memo[k] = k * factorial(k - 1)
    return memo[k]

def factorial2(k):
    if k < 2: return 1
    return k * factorial2(k - 1)

print(factorial(5))
print(factorial2(5))