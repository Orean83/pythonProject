

import csv
rows = []
#  чтение файла
with open('bonusHistory.csv', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter='|')
# пропуск первой строки с шапкой
    row = next(csvreader)
    for row in csvreader:
        rows.append(row)
# ввод данных
a = int(input('Введите начальную дату: '))
b = int(input('Введите конечную дату: '))
name = input('Введите юр. лицо: ')
file_name = input('Введите название файла: ')

# определение переменных для потраченных и накопленных бонусов
spend = 0
earned = 0
for s in rows:
# приведение переменных к нужным типам
    s[0] = int(s[0])
#  замена знака , на .
    s[1] = float(s[1].replace(',','.'))
    s[2] = float(s[2].replace(',','.'))

# условие для отбора данных
    if a<= s[0] <= b:
        spend = spend + s[1]
        # отброс знаков после запятой
        spend = round(spend, 2)
        earned = earned + s[2]
        earned = round(earned, 2)
print(spend, earned)

import os.path
# проверка на наличие файла
check_file = os.path.exists(file_name+'.csv')

# запись файла
with open(file_name+'.csv', 'a+', newline = '', encoding='utf-8') as total_file:
    csvwriter = csv.DictWriter(total_file, fieldnames= ['name', 'Потрачено', 'Накоплено'])

# проверка условия наличия файла
    if check_file == False:
        csvwriter.writeheader()

    csvwriter.writerow({'name':name, 'Потрачено':spend, 'Накоплено':earned})

tot = input('Посчитать итог? да/нет  ')
rows_tot = []
tot_spend = 0
tot_earned = 0
if tot == 'нет':
    exit()
else:
    with open(file_name+'.csv', encoding='utf-8') as total_f:
        totat_readf = csv.reader(total_f, delimiter=',')
        row_tot = next(totat_readf)
        for row_tot in totat_readf:
            rows_tot.append(row_tot)

    for st in rows_tot:
        st[1] = float(st[1])
        st[2] = float(st[2])
        tot_spend = tot_spend + st[1]
        tot_spend = round(tot_spend, 2)
        tot_earned = tot_earned + st[2]
        tot_earned = round(tot_earned, 2)
    print(tot_spend, tot_earned)

    with open(file_name + '.csv', 'a+', encoding='utf-8') as total_wr_file:
        csvtotwriter = csv.writer(total_wr_file)

        csvtotwriter.writerow(['Итог', tot_spend, tot_earned])