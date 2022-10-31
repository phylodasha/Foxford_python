print('Привет! Это бот, который составляет для тебя список покупок! Вводи по одному все товары, которые хочешь купить. Когда запишешь все, что нужно, напиши слово конец с маленькой буквы')
product = input('введите товар: ')
product_list = []
while product!='конец':
    product_list.append(product)
    product = input('введите товар: ')


print('Отправляемся в магазин!')    
while len(product_list) > 0:
    user_input = input('Укажите купленный продукт: ')
    product_list.remove(user_input)
    i = 0
    print('Список продуктов: ')
    while i < len(product_list):
        print(product_list[i])
        i += 1

print('Все продукты в корзине! Пора идти на кассу!')

