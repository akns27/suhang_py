"""
a = [1, 2, 3, 4, 5]
b = sum(a)

print(b)

c = input().split()
sum = int(0)

for i in range(5):
  a[i] = int(a[i])

for i in range(5):
  sum += a[i]

print(sum)
"""
def out(a):
  if a.length == 0:
    return 0
  num = a.pop()
  return num + out(a)
  
b = list(map(int,input().split()))
result = out(b)
print(result)
