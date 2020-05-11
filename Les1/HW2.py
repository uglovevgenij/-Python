'''2. Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.'''

a = int(input('Количество секунд: '))

sec = 0
min = 0
hour = 0

if a >= 60:
    sec = a % 60
    min = a // 60
else:
    sec = a
if sec < 10:
    sec = '0' + str(sec)

if min >= 60:
    hour = min // 60
    min = min % 60
if min < 10:
    min = '0' + str(min)
if hour < 10:
    hour = '0' + str(hour)


print('{0}:{1}:{2}'.format(hour, min, sec))


#complete


