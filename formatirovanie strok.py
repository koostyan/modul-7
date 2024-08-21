team1_num = 5
team2_num = 6
print("В команде Мастера кода участников: %d ! " % team1_num)  # Использование %:
print("В команде Волшебники данных участников: %d ! " % team2_num)
print("Итого сегодня в командах участников: %d и %d! " % (team1_num, team2_num))
print()

score_1 = 40
score_2 = 42
print("Команда Мастера кода решила задач: {} !".format(score_1))  # Использование format():
print("Команда Волшебники данных решила задач: {} !".format(score_2))
team1_time = 18015.2
print("Волшебники данных решили задачи за {} с !".format(team1_time))
print()

tasks_total = score_1 + score_2
time_avg = 350.4
print(f'Команды решили {score_1} и {score_2} задач.')  # Использование f-строк:
if score_1 > score_2 or score_1 == score_2:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(f'Результат битвы: {result}')
print(f'Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')
