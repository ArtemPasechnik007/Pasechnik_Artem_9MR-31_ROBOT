
temp = int(input("Введите температуру (°C): "))
rain = int(input("Есть осадки? (1/2) 1 - да 2 - нет: "))


if rain == 1 and 30 > temp > 20 :
    print("Наденьте Футболку, Шорты и возьмите Дождевик")

if rain == 2 and 30 > temp > 20 :
    print("Наденьте Футболку, Шорты")
if 20 > temp > 0  :
    level_rain = int(input("Осадки сильные? (1/2) 1 - да 2 - нет: "))

    if 20 > temp > 0 and rain == 1 and level_rain == 1:
        print("Наденьте Пальто, Резиновые сапоги и возьмите Зонт")

    if 20 > temp > 0 and rain == 1 and level_rain == 2:
        print("Наденьте Пальто и возьмите Дождевик")

if temp < 0:
    print("Наденьте Пуховик")

if 20 > temp > 0  and rain == 2 :
    print("Наденьте Пальто")



