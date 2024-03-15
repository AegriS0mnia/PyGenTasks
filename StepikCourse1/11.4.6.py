number_of_webpages = int(input())
web_pages_set = []
junk_web_pages_set_= []
clear_web_page_set = []
for _ in range(number_of_webpages):
    web_page = input()
    web_pages_set.append(web_page)

keyword_number = int(input())
keyword_set = []
for _ in range(keyword_number):
    keyword_ = input().lower()
    keyword_set.append(keyword_)

for current_web_page in web_pages_set:
    for current_keyword in keyword_set:
        if current_keyword not in current_web_page.lower() and current_web_page not in junk_web_pages_set_:
            junk_web_pages_set_.append(current_web_page)

for i in web_pages_set:
    if i not in junk_web_pages_set_:
        clear_web_page_set.append(i)

print(*clear_web_page_set, sep='\n')