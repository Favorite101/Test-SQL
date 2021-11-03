x = int(input("введите тип сортировки (1 - возрастание, 2 - убывание): "))
a = list(map(int, input("введите числа через пробел: ").split()))
n = 1
if x == 1:
    while n < len(a):
        for i in range(len(a)-n):
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
        n += 1
    print(a)
elif x == 2:
    while n < len(a):
        for i in range(len(a)-n):
            if a[i] < a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
        n += 1
    print(a)
else:
    print("выберите только один из двух способов")

