print('При покупке трёх и более билетов представляется скидка 10% на весь заказ')
bilets = int(input("Введите количество приобретаемых билетов: "))
age = [int(input('Введите возраст посетителя для каждого билета: ')) for i in range(0, bilets)]
price = 0
for i in age:
    if i < 18:
        price += 0
    elif 18 <= i <= 25:
        price += 990
    else:
        price += 1390

if bilets >= 3:
    total_price = (f'{int(price * 0.9)} руб. (применена скидка 10%)')
else:
    total_price = (f'{price} руб.')

print(f'Стоимость билетов составляет {total_price} ')