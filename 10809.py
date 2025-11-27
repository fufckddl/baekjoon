ans = [-1] * 26
str = input()
for i in range(len(str)):
    char = str[i]
    idx = ord(char) - ord('a')
    if ans[idx] == -1:  # 처음 등장하는 경우만
        ans[idx] = i

for i in range(len(ans)):
    print(ans[i], end = ' ')