import re;
import json;

def search(query, ordering = 'normal'):
    with open('recipes.json', 'r') as file:
        data = json.load(file)
    list = query.split()
    print(list)

    searchResultList = []
    for index in data:
        if 'title' not in index:
            continue

        title = index['title']
        ''' 单词出现的次数 '''
        num = 0
        for word in list:
            titleNum = title.count(word)
            categoriesNum = getValueByKey(index, 'categories').count(word)
            ingredientsNum = getValueByKey(index, 'ingredients').count(word)
            directionsNum = getValueByKey(index, 'directions').count(word)
            num = num + titleNum + categoriesNum + ingredientsNum + directionsNum
        print(num)
        if 0 != num:
            result = {'title': title, 'num': num}
            insertNode(searchResultList, result)

    print('searchResultList=', searchResultList)
    print('-----------------------------------------------------------------')
    for i in range(len(searchResultList)):
        if 10 == i:
            break;
        else:
            print('top' + str(i+1) + ":", searchResultList[i]['title'], searchResultList[i]['num'])
    print('-----------------------------------------------------------------')

def getValueByKey(json, key):
    if key in json:
        return json[key]
    else:
        return ''

def insertNode(searchResultList, node):
    if [] == searchResultList:
        searchResultList.append(node)
    else:
        isInserted = False
        for i in range(len(searchResultList)):
            if searchResultList[i]['num'] < node['num']:
                searchResultList.insert(i, node)
                isInserted = True
                break
        if False == isInserted:
            searchResultList.append(node)

search('Apple with', 'normal')
