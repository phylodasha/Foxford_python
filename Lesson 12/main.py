cashier_name = "Людмила"
price = 99
count_products = int(input("Введите количество товаров: "))
count_packages = int(input("Введите количество пакетов"))
print("ООО Супер магазин")
print("КАССОВЫЙ ЧЕК")
print(f"Кассир: {cashier_name}")
print("=====================")
print(f"Количество товаров: {count_products}")
print(f"Количество пакетов: {count_packages}")
print(f"ИТОГО: {price*count_products + count_packages} руб.")

mark1 = int(input("Добрый день, пользователь 1! Введите оценку магазину"))
mark2 = int(input("Добрый день, пользователь 2! Введите оценку магазину"))
mark3 = int(input("Добрый день, пользователь 3! Введите оценку магазину"))
mark4 = int(input("Добрый день, пользователь 4! Введите оценку магазину"))
mark5 = int(input("Добрый день, пользователь 5! Введите оценку магазину"))
count_users = 5

print(f"По опросам пользователей ср. оценка: {(mark1 + mark2 + mark3 + mark4 + mark5)/count_users}")