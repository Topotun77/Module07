# Домашнее задание по теме "Форматирование строк".
# История: соперничество двух команд - Мастера кода и Волшебники данных.

# Использование %:
team1_num = 4
team2_num = 6
team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'

print('В команде Мастера кода участников: %d ! ' % team1_num)
print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))

# Использование format():
score_1 = 25
score_2 = 36
team1_time = (100 * 60 + 100) / 3
team2_time = 41 * 60
print('Команда {} решила задач: {} !'.format(team2_name, score_2))
print('Волшебники данных решили задачи за {0:1.1f} с !'.format(team1_time))

# Использование f-строк:
challenge_fn = lambda x, y, z: x / y / z  # функция для расчета победителя
# print(challenge_fn(score_1, team1_num, team1_time), challenge_fn(score_2, team2_num, team2_time))

# Да, следующая запись длинная и практически нечитаема (хотя я пыталась форматирование добиться
# наилучшей читаемости), но хотелось проверить можно ли так реализовать присвоение
# через двойной if, оказалось, что можно! Поразительно! С такими возможностями языка можно писать
# не только максимально читаемый, но и максимально НЕчитаемый код )))
challenge_result = team1_name if (challenge_fn(score_1, team1_num, team1_time) >
                                  challenge_fn(score_2, team2_num, team2_time)) \
    else team2_name if (challenge_fn(score_1, team1_num, team1_time) <
                        challenge_fn(score_2, team2_num, team2_time)) \
    else 'Дружба'
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: победа команды {challenge_result}!')
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:1.2f} секунды на задачу!')
