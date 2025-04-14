arr = [10, 2, 14, 7, 8, 12, 15, 11, 0, 4, 1, 13, 3, 9, 6, 5]

for firstNum in arr:
    edx = 0
    secondNum = 0
    eax = firstNum
    
    while edx != 15:
        edx += 1
        eax = arr[eax]
        secondNum += eax
        
        if eax == 15 and edx == 15:
            print(f"firstNum = {firstNum} secondNum = {secondNum}")
            exit(0)