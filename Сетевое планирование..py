#Исходные данные: Упорядоченная структурная таблица с временем работ и номерами предшественников (работ-родителей)
table_time = {"B1": 5, "B2": 8,"B3": 6,"B4": 7, "B5": 6, "B6": 9, "B7": 10, "B8": 7, "B9": 3, "B10": 8}
table_parents = {"B1":[],"B2":[] ,"B3":["B1","B2"] ,"B4":["B2"] , "B5":["B1","B2"] , "B6":["B1","B2"], "B7": ["B6"], "B8": ["B3","B4","B5","B6"], "B9": ["B3","B4","B5","B6"], "B10": ["B7","B8","B9"]}
#######
#Код:
#Просто список работ
works = []
for keys in table_time:
    works.append(keys)

#Функция подсчета раннего начала и раннего конца
list_rn = []
list_rk = []
for j in works:
#def R_nach_kon(x):  Функция подсчета раннего начала и раннего конца
    if table_parents[j] == []:
        r_nach = 0
        list_rn.append(r_nach)
        table_r_nach = {key: value for key, value in zip(works, list_rn)}
        #
        r_kon = r_nach + table_time[j]
        list_rk.append(r_kon)
        table_r_kon = {key: value for key, value in zip(works, list_rk)}
    else:
        list_rn_i = []
        for i in table_parents[j]:
            list_rn_i.append(table_r_kon[i])
        r_nach = max(list_rn_i)
        list_rn.append(r_nach)
        table_r_nach = {key: value for key, value in zip(works, list_rn)}
            #
        r_kon = r_nach + table_time[j]
        list_rk.append(r_kon)
        table_r_kon = {key: value for key, value in zip(works, list_rk)}

print("Таблица ранних начал:      ",table_r_nach)
print("Таблица ранних концов:     ",table_r_kon)

#############################################################################################
# Создал список из списков родителей (в кажом элементе этого списка списков будем искать значения для словаря детей)
values1 = []
for values in table_parents.values():
    values1.append(values)
#print("родители",values1)
# Создал список ключей ( имена родителей) для словаря детей
works = []
for keys in table_parents:
    works.append(keys)
#print("работы",works)
# Реализую алгоритм сбора детей для каждого родителя из списка works
i=0
j=0
list_children=[]
while i <= int(len(table_time)-1):
    list_child = []
    for j in range(int(len(table_time))):
        if works[i] in values1[j]:
            list_child.append(works[j])
        j += 1
    list_children.append(list_child)
    i+=1
#print(list_children)
# склевую два списка в словарь детей
table_children = {key:value for key, value in zip(works,list_children)}
print("Таблица детей:", table_children)
################################################################################################################

#def Pozd_nach_kon  Функция подсчета позднего начала и раннего конца
list_pozd_kon=[]
list_pozd_nach=[]
#поменял порядок списка работ, чтобы начинать с конца
works1 = works[::-1]
#list_pozd_kon.insert(0, int(pozd_kon))

for k in works1:
    if table_children[k] == []:
        pozd_kon = int(max(table_r_kon.values()))
        list_pozd_kon.append(pozd_kon)
        table_list_pozd_kon = {key: value for key, value in zip(works1, list_pozd_kon)}
        #
        pozd_nach = pozd_kon - table_time [k]
        list_pozd_nach.append(pozd_nach)
        table_list_pozd_nach = {key: value for key, value in zip(works1, list_pozd_nach)}
    else:
        list_pozd_kon_i = []
        for i in table_children[k]:
            list_pozd_kon_i.append(table_list_pozd_nach[i])
            pozd_kon = min(list_pozd_kon_i)
        list_pozd_kon.append(pozd_kon)
        table_list_pozd_kon = {key: value for key, value in zip(works1, list_pozd_kon)}
        #
        pozd_nach = pozd_kon - table_time[k]
        list_pozd_nach.append(pozd_nach)
        table_list_pozd_nach = {key: value for key, value in zip(works1, list_pozd_nach)}
#Навожу красоту в порядке для таблицы
list_pozd_nach1=list_pozd_nach[::-1]
table_list_pozd_nach1 = {key: value for key, value in zip(works, list_pozd_nach1)}
list_pozd_kon1=list_pozd_kon[::-1]
table_list_pozd_kon1 = {key: value for key, value in zip(works, list_pozd_kon1)}
print("Таблица поздних начал:     ",table_list_pozd_nach1)
print("Таблица поздних концов:    ",table_list_pozd_kon1)

#def  Функция подсчета полного и свободного резервов
list_poln_reserv = []
for i in works:
    poln_reserv = table_list_pozd_nach1[i] - table_r_nach[i]
    list_poln_reserv.append(poln_reserv)
table_poln_reserv = {key: value for key, value in zip(works, list_poln_reserv)}
print("Таблица полных резервов:   ",table_poln_reserv)

#
list_sv_reserv=[]
for i in works:
    if table_poln_reserv[i] == 0:
        sv_reserv = 0
    else:
        list_r_nach_j =[]
        for j in table_children[i]:
            list_r_nach_j.append(table_r_nach[j])
            r_nach_min = min(list_r_nach_j)
            sv_reserv = r_nach_min - table_r_kon[i]
    list_sv_reserv.append(sv_reserv)
table_sv_reserv = {key: value for key, value in zip(works, list_sv_reserv)}
print("Таблица свободных резервов:",table_sv_reserv)
