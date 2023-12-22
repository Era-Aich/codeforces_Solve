
# Read input
s = input()
t = input()

# Check if t is the reverse of s
if s == t[::-1]:
    print("YES")
else:
    print("NO")
