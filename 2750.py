n = int(input())
array = []
for i in range(n):
    k = int(input())
    array.append(k)

#간단한 방법
#array.sort()
# 반복문 기반 퀵 정렬 (스택 사용)
def quick_sort_iterative(array):
    if len(array) <= 1:
        return array
    
    stack = [(0, len(array) - 1)]
    
    while stack:
        start, end = stack.pop()
        
        if start >= end:
            continue
        
        pivot = array[start]
        left = start + 1
        right = end
        
        while left <= right:
            while left <= end and array[left] <= pivot:
                left += 1
            while right > start and array[right] > pivot:
                right -= 1
            
            if left < right:
                array[left], array[right] = array[right], array[left]
        
        array[start], array[right] = array[right], array[start]
        
        stack.append((start, right - 1))
        stack.append((right + 1, end))
    
    return array

array = quick_sort_iterative(array)

for i in range(n):
    print(array[i])