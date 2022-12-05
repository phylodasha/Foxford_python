price = 99
def print_receipt(products):
    print("ООО Супер магазин")
    print("КАССОВЫЙ ЧЕК")
    print("=====================")
    for product in products:
        print(f'{product} ----- 1шт.      {price}')
    print(f'ИТОГО: {len(products) * price}')
products = []
def add_product():
    product = input('Введите продукт, который вы положили в корзину (если хотите завершить ввод, напишите 0):  ')
    while product != '0':
        products.append(product)
        print(f'{product} добавлен в корзину')
        product = input('Введите продукт, который вы положили в корзину (если хотите завершить ввод, напишите 0):  ')

def welcome():
    print('Привет, дорогой покупатель!')

while 4==4:
    products = []
    welcome()
    add_product()
    print_receipt(products)