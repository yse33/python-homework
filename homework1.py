a = [5, 12, 34, 65, 97, 106]
i = 0
smallest = a[i]
biggest = a[i]
while i < len(a): 
    if a[i] < smallest:
        smallest = a[i]
    if a[i] > biggest:
        biggest = a[i]
    i += 1
result = biggest-smallest
print(result)
