# (Section - D (DSA))

# ANSWER - 19
a=[4,2,4,3,2,4,1]
d={}
for x in a:
    d[x]=d.get(x,0)+1
print(d)

# ANSWER - 16
arr = [2, 4, 6, 8, 10, 12]
d = arr[1] - arr[0]
num = True
for i in range(1, len(arr)):
    if arr[i] - arr[i-1] != d:
        num = False
print(num)

# ANSWER - 17
arr = [2, 1, 5, 1, 3, 2]
t = 3
s = sum(arr[:t])
m = s
for i in range(t, len(arr)):
    s = s + arr[i] - arr[i-t]
    m = max(m, s)

# ANSWER  - 18
arr = [1, 2, 4, 6, 8, 9]
target = 10

left = 0
right = len(arr) - 1
while left < right:
    s = arr[left] + arr[right]
    if s == target:
        print(arr[left], arr[right])
        break
    elif s < target:
        left += 1
    else:
        right -= 1
# time complexity = O(n)
# spac complec=xity = O(1)

# ANSWER - 20
arr = [3, 1, 4, 2, 5, 1, 6]
k = 3

s = sum(arr[:k])
m = s

for i in range(k, len(arr)):
    s = s + arr[i] - arr[i-k]
    m = max(m, s)

print("Maximum Sum:", m)
# time complexity = O(n)