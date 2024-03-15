age_of_user = int(input())

if age_of_user <= 13:
    print('детство')
if 14 <= age_of_user <= 24:
    print('молодость')
if 25 <= age_of_user <= 59:
    print('зрелость')
if age_of_user >= 60:
    print('старость')