import csv
from operator import length_hint
import pandas
import string
import numpy

df = pandas.read_csv('user_names.csv')
df.columns = ['user','show_id','status']

current_user = df.loc[0]['user']
result = []
shows = ''
watched_count = 0
length = len(df)
# length = 600

# print(df.loc[0]['user'])
for i in range(length):
    if (df.loc[i]['user'] == current_user):
        if (df.loc[i]['status'] != 'ConsumptionStatus.dropped'):
            shows += str(df.loc[i]['show_id']) + ' '
            watched_count += 1

    else:
        result.append([current_user,watched_count,shows])
        current_user = df.loc[i]['user']
        shows = ''
        watched_count = 0
        if (df.loc[i]['status'] != 'ConsumptionStatus.dropped'):
            # shows.append(df.loc[i]['show_id'])
            shows += str(df.loc[i]['show_id']) + ' '
            watched_count += 1
    if(i == length-1):
        result.append([current_user,watched_count,shows])

outputdf = pandas.DataFrame(result, columns = ['user','watched count','watched list'])
outputdf.to_csv('users_watched2.csv', index=False)

print('process complete!!')

