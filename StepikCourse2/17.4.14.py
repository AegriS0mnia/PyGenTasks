with open('logfile.txt', 'r', encoding='utf-8') as input, open('output.txt', 'w', encoding='utf-8') as output:
    users = input.readlines()
    for user in users:
        user = user.split(',')

        log_in_time = [int(i) for i in user[1].split(':')]
        log_out_time = [int(i) for i in user[2].split(':')]
        active_time = (log_out_time[0] - log_in_time[0]) * 60 + (log_out_time[1] - log_in_time[1])
        is_active_time_more_than_hour = active_time >= 60

        if is_active_time_more_than_hour:
            print(user[0], file=output)
