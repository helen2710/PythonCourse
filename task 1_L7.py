# Aceasta este sarcina pentru lecția 7 legată de comentarii, continuarea liniilor și instrucțiuni condiționale.

# Creați o variabilă numită number și atribuiți-i o valoare întreagă.

# CODUL TĂU VINE MAI JOS:
number = 78
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este pozitiv și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number > 0:
   print("The number is pozitive")
elif number < 0:
   print("The number is negative")
else:
   print("The number is equal zero")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este par și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number % 2 == 0:
   print("The number is even")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este impar și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number % 2 != 0:
   print("The number is odd")
# CODUL TĂU VINE MAI SUS:

# Creați o variabilă text și atribuiți-i un șir de caractere.

# CODUL TĂU VINE MAI JOS:
text = ("Smile and the world will smile with you!")
print(text)
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Python" in text:
   print("The text contains the word 'Python'")
else:
   print("The text doesn't contain the word 'Python'")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Java" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Java" in text:
   print("The text contains the word 'Java'")
else:
   print("The text doesn't contain the word 'Java'")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
# în cazul în care nu conține, verificați dacă conține cuvântul "Java" și afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Python" in text:
   print("The text contains the word 'Python'")
elif "Java" in text:
   print("The text contains the word 'Java'")
else:
   print("The text contains neither word 'Python' nor 'Java'")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și cuvântul "Java" și afișați un mesaj corespunzător.
# În cazul în care conține doar unul dintre ele, afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Python" and  "Java" in text:
   print("The text contains both words: 'Python' and 'Java'")
elif "Java" or "Python" in text:
   print("The text contains just one of the words 'Java' or 'Python")
else:
   print("The text contains neither word 'Python' nor 'Java'")
# CODUL TĂU VINE MAI SUS:
"""
Extrageți de la tastatură utilizând funcția input un număr de la 1 la 5 și atribuiți-l variabilei number.
Folosiți o instrucțiune condițională pentru a printa un mesaj corespunzător în funcție de numărul introdus.
pentru 1 - printați "Unu"
pentru 2 - printați "Doi"
pentru 3 - printați "Trei"
pentru 4 - printați "Patru"
pentru 5 - printați "Cinci"
"""
# CODUL TĂU VINE MAI JOS:
print("Enter the number from 1 to 5 :")
number =input()
match number:
    case '1':
        print("\"Unu\"")
    case '2':
        print('"Doi"')
    case '3':
        print("\"Trei\"")
    case '4':
        print("\"Patru\"")
    case '5':
        print('"Cinci"')
    case _:
         print("The number is not correct")
# CODUL TĂU VINE MAI SUS:
