end = ""

while True:
    n = input()
    if n == "0":
        break
    end = ""
    for i in range(len(n)-1, -1, -1):
        end += n[i]
    if n == end:
        print("yes")
    else:
        print("no")