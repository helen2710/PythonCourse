# Aceasta este sarcina pentru lecția despre polimorfism, metode speciale și compoziție a claselor în Python.

from sigmoid_check.python_odyssey.lesson_15.lesson_15 import Lesson15

# Această temă pentru acasă necesită instalarea librăriei `sigmoid_check` cu versiunea cel puțin 0.0.8
# Pentru a instala această librărie, rulați următorul cod în terminal:
# pip install sigmoid_check==0.0.8

# VERIFICATION PROCESS
session = Lesson15()
# VERIFICATION PROCESS

"""
ISTORIA DIN SPATE
După toată munca depusă pentru proiectul de la DARWIN și TechSolutions, ai primit o ofertă de la cei de la Microsoft, 
aceștia lucrează la crearea unui algoritm care le va permite procesarea a unor cantități mari de date.
"""

"""
Primul pas în crearea algoritmului este implementarea unor containere de date care va permite stocarea și manipularea datelor într-un mod mai simplu
și eficient. Trebuie să creezi o clasă nouă `DataContainer`. Pentru a manipula datele vom folosi metodele speciale ale clasei.

Clasa va primi ca parametru o listă de numere integer.
- __init__ initializează clasa cu lista de numere.
- __str__ va returna lista de numere sub formă de string.
- __len__ va returna numărul de elemente din listă.
- __getitem__ va permite accesarea elementelor din listă folosind indexul (e.g., container[0]).
- __setitem__ va permite modificarea elementelor din listă folosind indexul (e.g., container[0] = 5).
- __add__ va permite combinarea a două instanțe de `DataContainer` într-o singură instanță.
"""

# CODUL TĂU VINE MAI JOS:
class DataContainer:
    def __init__(self,list_num1):
        self.list_numbers=list_num1
    def __str__(self) :
        return f"{','.join(str(j) for j in self.list_numbers)}"
    def __len__(self):
        return len(self.list_numbers)
    def __getitem__(self, ind):
        return self.list_numbers[ind]
    def __setitem__(self, ind, value):
        self.list_numbers[ind] = value
    def __add__(self, list_num2):
        for i in list_num2:
            self.list_numbers.append(i)
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_1(DataContainer))
# VERIFICATION PROCESS

"""
Acum avem nevoie de o modalitate de a calcula suma și produsul containerului de date. Pentru aceasta creează două clase noi care vor moșteni clasa `DataContainer`.
- `SumaContainer` va calcula suma elementelor din listă.
- `ProdusContainer` va calcula produsul elementelor din listă.
Ambele clase vor avea metoda `calculate` care va returna suma sau produsul elementelor.
"""

# CODUL TĂU VINE MAI JOS:
class SumaContainer(DataContainer):
    def __init__(self, list_num1):
        super().__init__(list_num1)
    def calculate(self):
        return sum(self.list_numbers)
    
class ProdusContainer(DataContainer):
    def __init__(self, list_num1):
        super().__init__(list_num1)
    def calculate(self):
        multipl = 1
        for j in self.list_numbers:
            multipl = multipl * j 
        return multipl
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_2(SumaContainer, ProdusContainer, DataContainer))
# VERIFICATION PROCESS

"""
Pentru ca instrumentul pe care îl folosim să fie complet vom mai avea nevoie de careva adiții.
Creează o clasă `DataAnalysis` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `__call__` va returna o listă cu valorile maxime ale fiecărui container.
"""

# CODUL TĂU VINE MAI JOS:
class DataAnalysis:
    def __init__(self, *lista_obiect: DataContainer):
        self.list_obj = lista_obiect
    def add_container(self, nou_cont):
        self.list_obj += (list(nou_cont),)
        print(self.list_obj)

    def __call__(self) :
        list_max =[]
        list1 = list(self.list_obj)
        for i in range(len(list1)):
            list_max.append(max(list1[i]))
        return list_max
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_3(DataAnalysis, DataContainer))
# VERIFICATION PROCESS

"""
Pe lângă elementul de analiză a datelor, Microsoft a mai cerut și un element de statistică.
Creează o clasă `DataStatistics` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `mean` va returna media aritmetică a elementelor din toate containerele.
- `median` va returna mediana elementelor din toate containerele.
- `min` va returna valoarea minimă din toate containerele.
- `sum` va returna suma elementelor din toate containerele.
"""

# CODUL TĂU VINE MAI JOS:
class DataStatistics:
    def __init__(self, *list_obj: DataContainer):
        self.list_obj = list_obj
        
    def add_container(self, nou_cont):
        self.list_obj += (list(nou_cont),)
        # print(self.list_obj)

    def mean(self):
        sum = 0
        count = 0
        list_us = list(self.list_obj)
        for i in range(len(list_us)):
            for j in range(len(list_us[i])):
                sum += list_us[i][j]
                count +=1
        print(f"Average of all values is {sum/count}")
        return (sum/count)
    
    def median(self):
        count = 0
        list_us = list(self.list_obj)
        list_total =[]
        for i in range(len(list_us)):
            for j in range(len(list_us[i])):
                list_total.append(list_us[i][j])
                count +=1
        list_total.sort()
        if count % 2 != 0:
            mediana = list_total[count//2]
        else:
            mediana = ((list_total[count//2] + list_total[count//2-1])/2)
        return (f"Median of all values is {mediana}")
    
    def min(self):
        count = 0
        list_us = list(self.list_obj)
        minimum = list_us[0][0]
        for i in range(len(list_us)):
            for j in range(len(list_us[i])):
                if list_us[i][j] < minimum:
                    minimum = list_us[i][j]
                count +=1
        return (f"Minimum of all values is {minimum}")
    
    def suma(self):
        suma = 0
        count = 0
        list_us = list(self.list_obj)
        return f"Total sum is {sum( list_us[i][j] for i in range(len(list_us)) for j in range(len(list_us[i])))}"

# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_4(DataStatistics, DataContainer))
# VERIFICATION PROCESS

"""
Iar pe ultima sută de metri, Microsoft a cerut și un element de filtrare a datelor.

Creează o clasă `DataFilter` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `filter_zeros` va returna o listă cu toate elementele care sunt diferite de 0.
- `filter_negatives` va returna o listă cu toate elementele care sunt mai mari sau egale cu 0.
- `filter_positives` va returna o listă cu toate elementele care sunt mai mici sau egale cu 0.
- `filter_under_mean` va returna o listă cu toate elementele care sunt mai mari decât media aritmetică a tuturor elementelor calculate cu metoda `mean` din clasa `DataStatistics`.
"""

# CODUL TĂU VINE MAI JOS:
class DataFilter(DataStatistics):
    def __init__(self, *list_obj: DataContainer):
        super().__init__(*list_obj)
    
    def filter_zeros(self):
        list_us = list(self.list_obj)
        list_result =[]
        for i in range(len(list_us)):
            for j in range(len(list_us[i])):
                if list_us[i][j] != 0:
                    list_result.append(list_us[i][j])
        return (f"List excluding zero is: {list_result}")
    
    def filter_negatives(self):
        list_us = list(self.list_obj)
        list_result =[]
        for i in range(len(list_us)):
            for j in range(len(list_us[i])):
                if list_us[i][j] >= 0:
                    list_result.append(list_us[i][j])
        return (f"List excluding negatives is: {list_result}")
    
    def filter_positives(self):
        list_us = list(self.list_obj)
        list_result =[]
        for i in range(len(list_us)):
            for j in range(len(list_us[i])):
                if list_us[i][j] < 0:
                    list_result.append(list_us[i][j])
        return (f"List excluding positives is: {list_result}")
    def filter_under_mean(self):
        media = self.mean()
        list_us = list(self.list_obj)
        list_result =[]
        for i in range(len(list_us)):
            for j in range(len(list_us[i])):
                if list_us[i][j] > media:
                    list_result.append(list_us[i][j])
        return (f"All values more than the average value = {media} are : {list_result}")
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_5(DataFilter, DataStatistics, DataContainer))
print(session.get_completion_percentage())
# VERIFICATION PROCESS