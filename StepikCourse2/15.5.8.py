is_num = lambda number: -1 <= number.find('-') == number.rfind('-') <= 0 and (len(number.split('.')) <= 2)\
         and number.split('.')[0].replace('-', '').isdigit() and number.split('.')[-1].replace('-', '').isdigit()
