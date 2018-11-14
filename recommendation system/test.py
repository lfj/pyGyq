#encoding:utf-8
import csv

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

#判断电影是否属于这个分类
def isMovieInGenre(genre, genreArray):
    for genreIndex in genreArray:
        if genre == genreIndex:
            return True
    return False

def insertInRatingArray(movie, movieGenreName):
    global highScoreMovie
    if 0 == len(highScoreMovie[movieGenreName]):
        highScoreMovie[movieGenreName].append(movie)
    else:
        #判断是否需要重新插入
        isReinserted = False
        for index in highScoreMovie[movieGenreName]:
            if movie['averageRating'] > index['averageRating']:
                isReinserted = True
                break
            elif movie['averageRating'] == index['averageRating']:
                highScoreMovie[movieGenreName].append(movie)
                break
        if isReinserted:
            highScoreMovie[movieGenreName] = []
            highScoreMovie[movieGenreName].append(movie)

#先导入u.data文件计算一下每个电影的平均分
data_file = csv.reader(open('ml-100k/u.data', 'r'))

#存储每个电影评分的数组
array = []

print(data_file)

for userRating in data_file:
    userRatingArray = splitString(userRating)
    print(userRatingArray)
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

item_file = csv.reader(open('ml-100k/u.item', 'r'))

movieArray = []
for movieIndex in item_file:
    try:
        movieArrayIndex = splitStringBySx(movieIndex)
        movieJson = {
            'movieId': movieArrayIndex[0],
            'title': movieArrayIndex[1],
            'genre': getGenre(movieArrayIndex),
            'averageRating': 0
        }
        print(movieJson)
        movieArray.append(movieJson)
    except:
        print('解析文件出现异常')

for movie in movieArray:
   for movieRating in array:
       if movie['movieId'] == movieRating['itemId']:
           movie['averageRating'] = movieRating['averageRating']

#记录电影名和电影ID映射的数组
itemArray = [
    'unknown',
    'Action',
    'Adventure',
    'Animation',
    'Children\'s',
    'Comedy',
    'Crime',
    'Documentary',
    'Drama',
    'Fantasy',
    'Film-Noir',
    'Horror',
    'Musical',
    'Mystery',
    'Romance',
    'Sci-Fi',
    'Thriller',
    'War',
    'Western'
]

#下面是各类电影评分最高的变量
highScoreMovie = {
    'unknown':[],
    'Action':[],
    'Adventure':[],
    'Animation':[],
    'Children\'s':[],
    'Comedy':[],
    'Crime':[],
    'Documentary':[],
    'Drama':[],
    'Fantasy':[],
    'Film-Noir':[],
    'Horror':[],
    'Musical':[],
    'Mystery':[],
    'Romance':[],
    'Sci-Fi':[],
    'Thriller':[],
    'War':[],
    'Western':[]
}

for movie in movieArray:
    for genreIndex in itemArray:
        # 如果电影在某个种类里，则去查一下是否是最高分，如果是最高分就插入，否则就并列
        if isMovieInGenre(genreIndex, movie['genre']):
            insertInRatingArray(movie, genreIndex)

#把每个种类的最高分的电影都打印出来
for key in highScoreMovie:
    highScoreArray = highScoreMovie[key]
    print("种类为" + key + "的电影评分最高分的电影如下：")
    for movie in highScoreArray:
        print('电影名：' + movie['title'] + ',平均评分为' + str(movie['averageRating']))
