#creates bag of words with selected features
def Create_soup_selection(x,studio=False,source=False,genre=False,va=False,all=False):
    result = x['Anime Title']

    if x['Studio'] != 'n/a' and (studio or all):
        result += ' ' + x['Studio']
    if x['Source Material'] != 'n/a' and (source or all):
        result += ' ' + x['Source Material']
    if x['Genre'] != 'n/a' and (genre or all):
        result += ' ' + x['Genre']
    if x['VAs'] != 'n/a' and (va or all):
        result += ' ' + x['VAs']

    punc = '[],\'\"'
    
    for ele in result:
        if ele in punc:
            result = result.replace(ele, "")

    result
    return result

#sorts list of tuples by the second element
def Sort_Tuple(tup):
    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):
            
        for j in range(0, lst-i-1):
            if (tup[j][1] < tup[j + 1][1]):
                temp = tup[j]
                tup[j]= tup[j + 1]
                tup[j + 1]= temp
    return tup

#finds the jaccard similarity
def Jaccard(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection / union)