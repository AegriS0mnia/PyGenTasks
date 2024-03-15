time_in_minutes = int(input())

integer_hours = time_in_minutes // 60
minutes = time_in_minutes % 60

recaculated_time = str(time_in_minutes) + ' мин - это ' + str(integer_hours)\
        + ' час ' + str(minutes) + ' минут.'

print(recaculated_time)