from textwrap import indent
from bs4 import BeautifulSoup
from lxml import etree
import requests
import time
from datetime import datetime
import re
import csv

# link = 'https://myanimelist.net/anime/1/Cowboy_Bebop'


def get_info(link):
    result = []

    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')

    # Title
    title = soup.find('h1', class_ = "title-name h1_bold_none").text.replace(',','')
    
    # Score
    try:
        score = soup.find('span', itemprop = "ratingValue").text
    except AttributeError:
        score = '-1'

    # Studio
    studios = soup.find('span', text = "Studios:")
    studio = studios.find_next_siblings('a')

    # Source
    try:
        source = soup.find('span', text = "Source:").next_sibling.strip()
    except AttributeError:
        source = ''

    # This finds both genres and themes
    genres = soup.find_all('span', itemprop = 'genre')
    
    # Demographic
    try:
        demographic = soup.find('span', text = "Demographic:").find_next_sibling().text
    except:
        demographic = ''

    #find the id
    i = 30
    id = ""
    while(link[i] != '/'):
        id += link[i]
        i += 1

    #find release year
    years = soup.find('span', text = "Aired:").next_sibling
    num = re.findall(r'\d+', years)
    num = [int(i) for i in num]
    for i in num:
        if i < 1900:
            num.remove(i)
    year = min(num)
    
    #find actors
    actors = soup.find_all(class_ ="va-t ar pl4 pr4")
    

    # Build the result
    result.append(id)
    result.append(title)
    result.append(year)
    result.append(score)
    if studio[0].text != 'add some':
        text = ""
        for each in studio:
            text = text + each.text + " "
        result.append(text)
    else:
        result.append(" ")
    if source != '':
        result.append(source)
    else:
        result.append(" ")
    if demographic != '':
        result.append(demographic)
    else:
        result.append(" ")
    text = ""
    for each in genres:
        text = text + each.text + " "
    result.append(text)
    text = ""
    for each in actors:
        text = text + each.text.replace('Japanese','').replace(',','').strip('\n') + " "
    result.append(text)

    
    # # Remove stop words and punctuation before appending to show info
    # stopWords = ['the', 'a', 'of', 'and', 'to', 'in', 'that', 
    #             'is', 'for', 'be', 'an', 'no', 'wo', 'ni', 'ga', ',']
    # punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # titleWords = title.lower()
    # for ele in titleWords:
    #     if ele in punc:
    #         titleWords = titleWords.replace(ele,'')
    # titleWords = titleWords.split()
    # for each in stopWords:
    #     if (each in titleWords):
    #         titleWords.remove(each)
    # for each in titleWords:
    #     result.append(each)
    
    #print(result)
    return result


def main():
    startTime = datetime.now()
    links = []
    with open('show_links_2017_2021.csv', 'r', encoding='utf-8') as reader:
        for line in reader.readlines():
            links.append((line.strip('\n')))

    with open('test_set.csv', 'a', encoding='utf-8') as writer:
        for link in links:
            output = get_info(link)
            writer.write(str(output).strip('[]')+'\n')
            print('Scrapping --> {0} success!!!'.format(link))
            time.sleep(4)
    endTime = datetime.now()

    print('Elapsed time: ',format(endTime - startTime))

if __name__=="__main__":
    main()


# with open('temp.csv', 'a', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         for val in output:
#             writer.writerow(val)

# # print(years)