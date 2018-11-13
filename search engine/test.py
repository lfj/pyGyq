import json;

def search(query, ordering = 'normal'):
    if 'normal' == ordering:
        searchByNormal(query)
    elif 'simple' == ordering:
        searchBySimple(query)
    elif 'healthy' == ordering:
        searchByHealth(query)

def searchByNormal(query):
    global data
    list = query.split()

    searchResultList = []
    for index in data:
        if 'title' not in index:
            continue
        title = index['title']
        rating = getValueByKey(index, 'rating')
        if not isDigit(rating):
            rating = 0
        num = 0
        for word in list:
            titleNum = title.lower().count(word)
            categoriesNum = str(getValueByKey(index, 'categories')).lower().count(word.lower())
            ingredientsNum = str(getValueByKey(index, 'ingredients')).lower().count(word.lower())
            directionsNum = str(getValueByKey(index, 'directions')).lower().count(word.lower())
            num = num + 8 * titleNum + 4 * categoriesNum + 2 * ingredientsNum + directionsNum
        num = num + rating
        print(num)
        if 0 != num:
            result = {'title': title, 'num': num}
            insertNodeByMax(searchResultList, result)

    print('searchResultList=', searchResultList)
    print('用户输入的搜索字段=', list)
    print('排序方式是normal时的搜索结果如下')
    print('-----------------------------------------------------------------')
    for i in range(len(searchResultList)):
        if 10 == i:
            break;
        else:
            print('top' + str(i+1) + ":", searchResultList[i]['title'], searchResultList[i]['num'])
    print('-----------------------------------------------------------------')

def searchBySimple(query):
    global data
    list = query.split()
    searchResultList = []
    for index in data:
        if 'title' not in index:
            continue
        title = index['title']
        if isSearchInJson(list, index):
            directions = getValueByKey(index, 'directions')
            ingredients = getValueByKey(index, 'ingredients')
            if isListEmpty(directions) or isListEmpty(ingredients):
                continue
            num = len(directions) * len(ingredients)
            print(num)
            result = {'title': title, 'num': num}
            insertNodeByMin(searchResultList, result)
    print('searchResultList=', searchResultList)
    print('用户输入的搜索字段=', list)
    print('排序方式是simple时的搜索结果如下')
    print('-----------------------------------------------------------------')
    for i in range(len(searchResultList)):
        if 10 == i:
            break;
        else:
            print('top' + str(i + 1) + ":", searchResultList[i]['title'], searchResultList[i]['num'])
    print('-----------------------------------------------------------------')

def searchByHealth(query):
    global data
    list = query.split()
    searchResultList = []
    for index in data:
        if 'title' not in index:
            continue
        title = index['title']
        if isSearchInJson(list, index):
            categoriesNum = getValueByKey(index, 'calories')
            proteinNum = getValueByKey(index, 'protein')
            fatNum = getValueByKey(index, 'fat')
            print(fatNum)
            #如果三个值都不是数字则放弃
            if (not isDigit(categoriesNum)) or (not isDigit(proteinNum)) or (not isDigit(fatNum)):
                continue
            healthValue = calculateHealthValue(categoriesNum, proteinNum, fatNum)
            result = {'title': title, 'num': healthValue}
            insertNodeByMin(searchResultList, result)
    print('searchResultList=', searchResultList)
    print('排序方式是healthy时的搜索结果如下')
    print('用户输入的搜索字段=', list)
    print('-----------------------------------------------------------------')
    for i in range(len(searchResultList)):
        if 10 == i:
            break;
        else:
            print('top' + str(i + 1) + ":", searchResultList[i]['title'], searchResultList[i]['num'])
    print('-----------------------------------------------------------------')

#判断是否是数字（浮点数）
def isDigit(num):
    numStr = str(num)
    if numStr.replace(".", '').isdigit():
        return True
    return False

#判断搜索结果在该词条里有没有
def isSearchInJson(list, json):
    isIncluded = False
    for word in list:
        lowerWord = word.lower()
        if lowerWord in str(getValueByKey(json, 'title')).lower():
            isIncluded = True
            break
        elif lowerWord in str(getValueByKey(json, 'categories')).lower():
            isIncluded = True
            break
        elif lowerWord in str(getValueByKey(json, 'ingredients')).lower():
            isIncluded = True
            break
        elif lowerWord in str(getValueByKey(json, 'directions')).lower():
            isIncluded = True
            break
    return isIncluded

def isListEmpty(list):
    if len(list):
        return False
    return True

#计算健康值
def calculateHealthValue(categoriesNum, proteinNum, fatNum):
    minHealthValue = 0
    for n in range(1, 5):
        result = abs(categoriesNum - 510 * n) / 510 + 2 * abs(proteinNum - 18 * n) / 18 + 4 * abs(fatNum) / 150
        if 1 == n:
            minHealthValue = result
            continue
        else:
            if result < minHealthValue:
                minHealthValue = result
    return minHealthValue

#从json字符串中获取value
def getValueByKey(json, key):
    if key in json:
        return json[key]
    else:
        return ''

#按照从小到大的顺序进行插入
def insertNodeByMin(searchResultList, node):
    if [] == searchResultList:
        searchResultList.append(node)
    else:
        isInserted = False
        #for i in range(len(searchResultList)):
        for i, val in enumerate(searchResultList):
            if 'Ice Block ' == searchResultList[i]['title']:
                print("相同相同相同相同")

            #如果插入的title相同，认为是同一个菜单
            if searchResultList[i]['title'].replace(' ', '') == node['title'].replace(' ', ''):
                isInserted = True
                break
            elif searchResultList[i]['num'] > node['num']:
                searchResultList.insert(i, node)
                isInserted = True
                break
        if False == isInserted:
            searchResultList.append(node)

#按照从大到小的顺序进行插入
def insertNodeByMax(searchResultList, node):
    if [] == searchResultList:
        searchResultList.append(node)
    else:
        isInserted = False
        #for i in range(len(searchResultList)):
        for i, val in enumerate(searchResultList):
            #如果插入的title相同，认为是同一个菜单
            if searchResultList[i]['title'].replace(' ', '') == node['title'].replace(' ', ''):
                isInserted = True
                break
            elif searchResultList[i]['num'] < node['num']:
                searchResultList.insert(i, node)
                isInserted = True
                break
        if False == isInserted:
            searchResultList.append(node)

with open('recipes.json', 'r') as file:
    data = json.load(file)
#search('apple pork', 'normal')
search('apple pork', 'simple')
#search('apple pork banana', 'healthy')