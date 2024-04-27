# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
list_num=[ i+1 for i in range(10)]
print(list_num)
print()   
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for number in list_num:
    if number % 2 == 0:
        print(number,' ', end='')
print()        
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while i < 6:
    print(i,' ', end='')
    i +=1
print()
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
print()   
person_in = {"name": "Melissa", "age": "29", "city": "Monterey"}
for key, values in person_in.items():
    print(key,values)
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
print()   
matrix_rand = [[25, 14, 26, 16], [17, 32, 84, 45], [98, 75, 86, 9]]
for row, num in enumerate(matrix_rand, 1):  # begin from 1
    print(f"Row: {row} Numbers: {num}", end='')
    # for num in row:
    #     print(num,' ', end='')
    print('')       
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
print()   
secventa = range(12)
for i in secventa:
    print(i,' ', end="")
print()
# print(list(range(2,10,1)))
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
# for i in enumerate(list1):
#     print(f"{i} ", end="")
print()   
list_color = ["red","white", "blue", "brown", "black"]   
list_color = [x.capitalize() for x in list_color] 
for i, color in enumerate(list_color):
    print(f"Index {i}: {color}")
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
print()   
list_item = ["skirt", "blouse", "shirt", "umbrella"]
for good, color in zip(list_item,list_color):
    print(color, good)
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
print()   
list_num1=[ i+1 for i in range(10)]
print(list_num1)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
print()   
first_el = list_num1[0]
while first_el < 51:
    for i in range(len(list_num1)):
      list_num1[i] *= 2   
    first_el =  list_num1[0]  
print(list_num1)
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
# list_patrat = []
# for i in range(10):
#     list_patrat[i] = (i + 1) ** 2
#     if list_patrat[i] > 99:
#         break
# print(list_patrat)
print()   
i = 1
while i ** 2 <= 100:
    print(i ** 2, end=' ')
    i += 1
print("")
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
print()   
for i in range(1,11):
    print(f'{i} * 7 = {i*7}')

# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.
 
# CODUL TĂU VINE MAI JOS:
print()   
matrix = [] 
for i in range(1,6):
    # row = []
    for j in range(1,6):
        row = []
        row.append(i)
        row.append(j)
        matrix.append(row)
print(matrix) 
"""   Variant II
for i in range(len(matrix)):
 for j in range(len(matrix[i])):
     print(f"{matrix[i][j]}", end=' ')
     if j == 1 and (i +1) % 5 == 0:
         print() 
"""                 
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
print()   
for i in range(len(matrix)):
    for j in range(1,2):
        if matrix[i][j-1] < matrix[i][j]:
            print(f"{matrix[i][j-1],matrix[i][j]} ", end="")
print()
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
print()   
random_list = [3, 2, 27, 9, -5]
sign = 0
for i in random_list:
    if i >10:
        print(f"{i} is the first number in the list greater than 10")
        sign = 1
        break
if sign == 0:
     print("There are no values greater than 10")

# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
print()   
# n = 3
n = int(input("Enter the size of the square : "))
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
i = 1
while i < 8:
    for j in range(1,i):
        print(j, end="")
    print()   
    i += 1
print()

# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
i = 6
while i > 0:
    for j in range(5, 6-i,-1):
        print(j, end="")
    print()   
    i -= 1
# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i in range(len(letters)):
    j = i
    while j < len(letters):
         print(letters[j], end="")
         j += 1
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
# string_oper = ["+", "-"]
print()   
for i in range(1,9):
    for j in range(1,9):
        if i % 2 != 0:
            print("+-",end="")
        else:
            print("-+",end="")
    print()    
print()       
# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
i = 1
exponentiation = 5
while i <= exponentiation:
    for j in range(1,i+1):
        print(3**j, end=" ")
    i +=1
    print()
while i > 0:
    for j in range(8-i, exponentiation + 1):
         print(3**j, end=" ")
    i -=1
    print()
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.