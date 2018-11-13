#encoding:utf-8
import csv
import pandas

def splitString(array):
    if len(array):
        str = array[0]
        return str.split()
    else:
        return []

#根据竖线来分割字符
def splitStringBySx(array):
    if len(array):
        str = array[0]
        return str.split('|')
    else:
        return []

#csv_file = csv.reader(open('ml-100k/u.data', 'r'))
#print(csv_file)
#for genre in csv_file:
#    print(splitString(genre))

'''
#先导入u.data文件计算一下每个电影的平均分
data_file = csv.reader(open('ml-100k/u.data', 'r'))

#存储每个电影评分的数组
array = []

print(data_file)

for userRating in data_file:
    userRatingArray = splitString(userRating)
    isNewInserted = True
    for index in array:
        if index['itemId'] == userRatingArray[1]:
            index['totalRating'] = index['totalRating'] + int(userRatingArray[2])
            index['totalUserNum'] = index['totalUserNum'] + 1
            isNewInserted = False
            break
    if isNewInserted:
        userRatingJson = {
            'itemId': userRatingArray[1],
            'totalRating': int(userRatingArray[2]),
            'totalUserNum': 1,
            'averageRating': 0
        }
        array.append(userRatingJson)

for movieRatingIndex in array:
    movieRatingIndex['averageRating'] = movieRatingIndex['totalRating'] / movieRatingIndex['totalUserNum']
    print('电影' + movieRatingIndex['itemId'] + '平均分是' + str(movieRatingIndex['averageRating']))

'''

#获取电影种类
def getGenre(movieArrayIndex):
    genreArray = []
    if  movieArrayIndex[5] == '1':
        genreArray.append('unknown')
    if  movieArrayIndex[6] == '1':
        genreArray.append('Action')
    if  movieArrayIndex[7] == '1':
        genreArray.append('Adventure')
    if  movieArrayIndex[8] == '1':
        genreArray.append('Animation')
    if  movieArrayIndex[9] == '1':
        genreArray.append('Children\'s')
    if  movieArrayIndex[10] == '1':
        genreArray.append('Comedy')
    if  movieArrayIndex[11] == '1':
        genreArray.append('Crime')
    if  movieArrayIndex[12] == '1':
        genreArray.append('Documentary')
    if  movieArrayIndex[13] == '1':
        genreArray.append('Drama')
    if  movieArrayIndex[14] == '1':
        genreArray.append('Fantasy')
    if  movieArrayIndex[15] == '1':
        genreArray.append('Film-Noir')
    if  movieArrayIndex[16] == '1':
        genreArray.append('Horror')
    if  movieArrayIndex[17] == '1':
        genreArray.append('Musical')
    if  movieArrayIndex[18] == '1':
        genreArray.append('Mystery')
    if  movieArrayIndex[19] == '1':
        genreArray.append('Romance')
    if  movieArrayIndex[20] == '1':
        genreArray.append('Sci-Fi')
    if  movieArrayIndex[21] == '1':
        genreArray.append('Thriller')
    if  movieArrayIndex[22] == '1':
        genreArray.append('War')
    if  movieArrayIndex[23] == '1':
        genreArray.append('Western')
    return genreArray

item_file = csv.reader(open('ml-100k/u.item', 'r'))

movieArray = []
for movieIndex in item_file:
    #try:
        movieArrayIndex = splitStringBySx(movieIndex)
        '''
        movieJson = {
            'movieId': movieArrayIndex[0],
            'title': movieArrayIndex[1],
            'genre': getGenre(movieArrayIndex)
        }
        '''
        #print(movieArrayIndex)
        print(movieArrayIndex)

    #except:
    #    print('解析文件出现异常')
