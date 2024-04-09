# Aceasta este a doua ta sarcină legată a leciei legate de stringuri în python

# Creează o variabilă numită `name` și seteaz-o la numele tău

# CODUL TĂU VINE MAI JOS:
name = 'Elena'
# CODUL TĂU VINE MAI SUS:

# Acum afișează valoarea variabilei `name` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(name)
# CODUL TĂU VINE MAI SUS:

# Acum creează o nouă variabilă numită `name2` și seteaz-o la valoarea variabilei `name` și afișează valoarea variabilei `name2` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
name2 = name
print(name2)
# CODUL TĂU VINE MAI SUS:

# Acum printează ultimul caracter al variabilei `name` folosind indexarea

# CODUL TĂU VINE MAI JOS:
print(name[-1])
# CODUL TĂU VINE MAI SUS:

# Acum printează primele 3 caractere ale variabilei `name` folosind slicing

# CODUL TĂU VINE MAI JOS:
print(name[:3])
# CODUL TĂU VINE MAI SUS:

# Acum printează valoarea variabilei `name` în majuscule folosind metoda `upper`

# CODUL TĂU VINE MAI JOS:
print(name.upper())
# CODUL TĂU VINE MAI SUS:

# Acum printează valoarea variabilei `name` în minuscule folosind metoda `lower`

# CODUL TĂU VINE MAI JOS:
print(name.lower())
# CODUL TĂU VINE MAI SUS:

# Acum printează concatenarea variabilelor `name` și `name2`

# CODUL TĂU VINE MAI JOS:
print(name+name2)
# CODUL TĂU VINE MAI SUS:

# Creează o variabilă `text` și setează-i un text la alegere, cu restricția ca acesta să conțină mai multe rânduri

# CODUL TĂU VINE MAI JOS:
text = "Peace is more than the absence of war."
# print(text)
# CODUL TĂU VINE MAI SUS:

# Verifică dacă variabila `text` conține cuvântul `python`

# CODUL TĂU VINE MAI JOS:
print("python" in text)
# CODUL TĂU VINE MAI SUS:

# Folosește metoda replace pentru a înlocui litera `a` din variabila `text` cu litera `e`

# CODUL TĂU VINE MAI JOS:
print(text.replace('a','e'))
# CODUL TĂU VINE MAI SUS:

# Folosește metoda split pentru a transforma variabila `text` într-o listă de cuvinte

# CODUL TĂU VINE MAI JOS:
print(text.split())
# CODUL TĂU VINE MAI SUS:

# Creează un f-string care să conțină variabilele `name` și `name2`

# CODUL TĂU VINE MAI JOS:
f_string = f'My name is {name} and  my friend\'s name is {name2}. They are the same. So funny!'
print(f_string)
# CODUL TĂU VINE MAI SUS:

# Verifică dacă string-ul creat se termină cu `!`

# CODUL TĂU VINE MAI JOS:
print(f_string.endswith('!'))
# CODUL TĂU VINE MAI SUS:

# Verifică dacă string-ul creat începe cu `Hello`

# CODUL TĂU VINE MAI JOS:
print(f_string.startswith('Hello'))
# CODUL TĂU VINE MAI SUS:

# Identifică indexul unde se află `!` în string-ul creat

# CODUL TĂU VINE MAI JOS:
print(f_string.find('!'))
# CODUL TĂU VINE MAI SUS:

# Identifică indexul unde se află `o` în string-ul creat folosind altă metodă

# CODUL TĂU VINE MAI JOS:
print(f_string.index('o'))
# CODUL TĂU VINE MAI SUS:

# Utilizând format string-uri, creează un string care să conțină variabilele `name` și `name2`

# CODUL TĂU VINE MAI JOS:
string2 ='It is quite common to find women with the name {}. \nIt is unlikely for {} to be a name commonly given to men.'.format(name,name2)
print(string2)
# CODUL TĂU VINE MAI SUS:

# Concatenează string-ul creat cu string-ul `text`

# CODUL TĂU VINE MAI JOS:
string_sum = text +'\n' +string2
print(string_sum)
# CODUL TĂU VINE MAI SUS:

# Afișează lungimea string-ului creat

# CODUL TĂU VINE MAI JOS:
print(len(string_sum))
# CODUL TĂU VINE MAI SUS:

# Aceasta a fost tot pentru această sarcină

