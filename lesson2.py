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

print(f"ИТОГО: {sum_}")


