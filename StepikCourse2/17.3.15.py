with open(r"C:\Users\mtagi\Downloads\data.csv", 'r', encoding='utf-8') as data:
    fields = data.readline().replace('\n', '').split(',')
    users = [user.replace('\n', '').split(',') for user in data.readlines()]
    def read_csv():
        data = []
        for user in users:
            data.append(dict(zip(fields, user)))
        return data

