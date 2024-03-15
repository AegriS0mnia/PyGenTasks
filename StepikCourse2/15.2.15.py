def info_kwargs(**kwargs):
    keys = sorted(kwargs)

    for i in keys:
        print(f'{i}: {kwargs[i]}')

info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
