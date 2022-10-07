cashier_name = "Людмила"
price = 99
count_products = int(input("Введите количество товаров: "))
count_packages = int(input("Введите количество пакетов"))
print("Магазин ВСЕ ПО 99")
print("КАССОВЫЙ ЧЕК")
print(f"Кассир: {cashier_name}")
print("=====================")
print(f"Количество товаров: {count_products}")
print(f"Количество пакетов: {count_packages}")
sum_ = price*count_products + count_packages
discount = 0
if 500 <= sum_ <=1500:
    print('Размер скидки: 5%')
    discount = 5
if 1500 < sum_ <= 5000:
    print('Размер скидки: 10%')
    discount = 10
if 5000 <= sum_ <= 1000:
    print('Размер скидки: 20%')
    discount = 20
if sum_ > 10000:
    print('Размер скидки: 50%')
    discount = 50
print(f"ИТОГО: {sum_ - sum_ * discount/100}")
print(f"ИТОГО: {sum_ * ((100-discount)/100)}")