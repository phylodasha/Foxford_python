first_list = ['макароны', 'печенье', 'морковь']
second_list = [1, 2, 3, 4, 5]
third_list = [11, 10, 12, 15, 13, 14, 58]

third_list[2] = 5 * 5
fourth_list = ['Тарон', 33, 'Яша', 76, 99, 'Ярослав', 'Вера']


# toy_box[2], toy_box[-4]
toy_box = ['машинка', 'робот', 'танк', 'LEGO', 'медведь', ' шашки']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(type(5))
print([numbers[0]] + numbers[3:5])
print(first_list[0:2] + toy_box[1:5])
print(first_list + third_list)

print(' '.join(toy_box))

print(toy_box[0:-1])

