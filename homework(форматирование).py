team_num1 = 5
team_num2 = 6
score1 = 41
score2 = 52
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if score2 > score1:
    challenge_result = 'Победа команды Мастера кода'
elif score1 == score2:
    challenge_result = "Ничья"

print("В команде Мастера кода участников: %s!" % 6)
print("Итого сегодня в командах участников: %s и %s!" % (5, 6))

print("\nКоманда Волшебники данных решила задач: {}!".format(4))
print("Волшебники данных решили задачи за {time} c.".format(time=412.4))

print(f"\nКоманды решили {score1} и {score2} задач")
print(f"Результат соревнования: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу")