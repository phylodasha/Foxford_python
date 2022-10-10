import random

start = input(
  "Привет! Это мини-игра, где надо убить монстра. Ничего не пиши, если хочешь начать, а если хочешь выйти напиши 'Exit'.\n"
)
if start == "Exit":
  print("Пока!")
  exit(1)
while start != "Exit":
  sword = input(
    "Итак, у тебя есть меч. Ты можешь нанести сильный удар, просто удар и удар ногой. Просто удар наносит от 15 до 40 урона, супер удар наносит намного больше - от 75 до 125, но уклонения не будет. А вот удар ногой наносит меньше - 5-20, но зато уклонение с 100 процентым шансом\n"
  )
  health = int("100")
  monster = random.randint(300, 600)
  print(monster)
  ss = input("О нет! Там монстр! Убей его!.\n")
  while monster > 0:
    damage = input(
      "Заметка: Чтобы сделать обычный удар напиши 'Attack', если сильный удар, то 'Super-Attack', а вот если удар ногой, то 'Leg-Attack'.\n"
    )
    if damage == "Attack":
      evasion = random.randint(1, 2)
      if evasion == 1:
        monsterDamage = random.randint(5, 15)
        health -= monsterDamage
        print("Вы не смогли увернуться. Вам нанесли", monsterDamage, "урона")
      else:
        print("Вы увернулись!")
      RealDamage = random.randint(15, 40)
      monster -= RealDamage
      print("Молодцы! Вы нанесли", RealDamage, "урона. У монстра осталось",
            monster, "здоровья, а у вас осталось", health, "здоровья.")
    if damage == "Super-Attack":
      monsterDamage = random.randint(1, 10)
      health -= monsterDamage
      RealDamage = random.randint(75, 125)
      monster -= RealDamage
      print("Молодцы! Вы нанесли", RealDamage, "урона. У монстра осталось",
            monster, "здоровья, но вам нанесли", monsterDamage,
            "урона. у вас осталось", health, "здоровья.")
    if damage == "Leg-Attack":
      RealDamage = random.randint(5, 20)
      monster -= RealDamage
      print("Молодцы! Вы нанесли", RealDamage, "урона. У монстра осталось",
            monster, "здоровья, а у вас осталось", health, "здоровья.")
  print("Ура! Вы убили его!")
  break
