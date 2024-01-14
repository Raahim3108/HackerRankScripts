input() # skip first input line
arr = map(int, input().split())
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

score = sum(map(
    lambda x: 1 if x in setA else -1 if x in setB else 0, arr))
print(score)