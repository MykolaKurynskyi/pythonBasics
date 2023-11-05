# n1 = 150
# n2 = 156
# n3 = 160

n1 = int (input("Введіть n1:: "))
n2 = int (input("Введіть n2:: "))
n3 = int (input("Введіть n3:: "))

if n1 >= n2 >= n3:
    print(n1)
    print(n2)
    print(n3)

elif n2 >= n1 >= n3:
    print(n2)
    print(n1)
    print(n3)

elif n3 >= n2 >= n1:
    print(n3)
    print(n2)
    print(n1)

elif n3 >= n1 >= n2:
    print(n3)
    print(n1)
    print(n2)

elif n1 >= n3 >= n2:
    print(n1)
    print(n3)
    print(n2)

elif n2 >= n3 >= n1:
    print(n2)
    print(n3)
    print(n1)



