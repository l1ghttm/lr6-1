spisok = ["олег", "кот", "фортнайт", "кс", "бабушка", ",батон"] #создание списка
skok = 0 #создание переменной для подсчета букв б
for str in spisok: #пребереание строк в списке
    if "б" in str: #проверка на содержание буквы 
        skok += 1 #увеличивание счета
print("кол-во строк содержащих букву б : ", skok) # вывод 
