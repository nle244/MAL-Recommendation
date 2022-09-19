#from mal import *
import requests
import mal_scraper


users_20 =  mal_scraper.discover_users()
s = list(users_20)
print(*s)
# print(s[1])

user_list = mal_scraper.get_user_anime_list(s[1])

output = []
for anime in user_list:
    # print(s[1])
    # print(anime['name'])
    # print(anime['id_ref'])
    # print(anime['consumption_status'])

    # output.append(s[1])
    # output.append(anime['name'])
    # output.append(anime['id_ref'])
    # output.append(anime['consumption_status'])

    # print(*output)
    print(s[1])




