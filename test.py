import re;
import json;

def search(query, ordering = 'normal'):

def searchByNormal(query):
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
            categoriesNum = str(getValueByKey(index, 'categories')).lower().count(word.lower())
            ingredientsNum = str(getValueByKey(index, 'ingredients')).lower().count(word.lower())
            directionsNum = str(getValueByKey(index, 'directions')).lower().count(word.lower())
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

def searchBySimple(query):


def searchByHealth(query):


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
        #for i in range(len(searchResultList)):
        for i, val in enumerate(searchResultList):
            #如果插入的title相同，认为是同一个菜单
            if searchResultList[i]['title'].replace(' ', '') == node['title'].replace(' ', ''):
                if node['num'] > searchResultList[i]['num']:
                    searchResultList[i]['num'] = node['num']
                    isInserted = True
                    break
            elif searchResultList[i]['num'] < node['num']:
                searchResultList.insert(i, node)
                isInserted = True
                break
        if False == isInserted:
            searchResultList.append(node)

search('apple pork', 'normal')
