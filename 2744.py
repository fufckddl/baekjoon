n = input()
result = ""
for i in range(len(n)):
    if n[i].islower():
        result += n[i].upper()
    else:
        result += n[i].lower()
print(result)