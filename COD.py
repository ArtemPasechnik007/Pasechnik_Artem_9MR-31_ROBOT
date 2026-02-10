
temp = int(input("Введите температуру (°C): "))
rain = int(input("Есть осадки? (1/2) 1 - да 2 - нет: "))

if rain == 1 and 30 > temp > 20 :
    print("Наденьте Футболку, Шорты, дождевик")

elif rain == 2 and 30 > temp > 20 :
    print("Наденьте Футболку, Шорты")

elif temp < 0:
    print("Наденьте пуховик")

elif temp > 0 and rain == 2 :
    print("Наденьте пальто")

