import sys

stack = []
# 백준 시간초과 우회
n = int(sys.stdin.readline())

for i in range(n):
    k = sys.stdin.readline().split()
    command = k[0]
    
    if command == "push":
        stack.append(int(k[1]))
    elif command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])