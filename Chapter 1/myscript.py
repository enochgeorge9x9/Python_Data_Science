def square(x):
    return x**2

for n in range(1,4):
    print(f'{n} squared is {square(n)}')

def sum_of_lists(n):  #Typing in the file mprun_dumo.py
    total = 0
    for i in range(5):
        l = [j^(j>>i) for j in range(n)]
        total += sum(l)
        del l #remove referece to l
    return total 