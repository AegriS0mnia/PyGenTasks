def build_query_string(query):
    keywords = []
    connected = []
    for i in query:
        keywords.append([i, str(query[i])])

    keywords.sort(key=lambda x: x[0])
    for i in keywords:
        connected.append('='.join(i))

    return '&'.join(connected)



query = {'name': 'timur', 'age': 28}


print(build_query_string({'name': 'timur', 'age': 28}))