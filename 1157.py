s = input().lower() #A : 65, a : 97
ans = [0] * 26
for i in range(len(s)):
    idx = ord(s[i]) - ord('a')
    ans[idx] += 1

max_values = max(ans)
if ans.count(max_values) > 1:
    print("?")
else:
    max_idx = ans.index(max_values)
    print(chr(ord('A') + max_idx))
