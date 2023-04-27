per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = (input("Введите сумму, которую планируете положить на вклад: ").split())
money_end = int(''.join(money))

values = list(map(float, per_cent.values()))
values_0, values_1, values_2, values_3 = values[0], values[1], values[2], values[3]

deposit = list(map(round, [money_end*values_0/100, money_end*values_1/100, money_end*values_2/100, money_end*values_3/100]))
print('Накопленные средства за год вклада в каждом из банков —', ', '.join(list(map(str, deposit))))

print('Максимальная сумма, которую вы можете заработать —', max(deposit))