import pandas as pd

myenc = 'latin1'

# 나이('age'), 직업('occupation')은 실제 값이 아니고, 그룹을 가리키는 코드 번호이다.
# README 파일을 참조하면 된다.
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']

# users.dat : 사용자 정보(나이, 우편번호, 성별, 직업)
# ratings.dat : 영화 평점 정보
# movies.dat : 영화 아이디, 제목, 장르

users = pd.read_csv('users.dat', sep='::', header=None, names=unames, encoding=myenc)
ratings = pd.read_csv('ratings.dat', sep='::', header=None, names=rnames, encoding=myenc)
movies = pd.read_csv('movies.dat', sep='::', header=None, names=mnames, encoding=myenc)

print('\n사용자 정보 5개')
print( users[:5])

print('\n평점 정보')
print( ratings[:5])

print('\n영화 정보')
print( movies[:5])

# 나이와 성별에 따른 어떤 영화의 평균 평점을 계산한다고 하자.
# merge 함수를 이용하여 데이터를 병합한다.
# merge는 병합하려는 두 테이블에서 중복되는 열의 이름을 키로 사용한다.
# on 속성을 명시하지 않으면, 공통 컬럼으로 머지한다.
data = pd.merge(pd.merge(ratings, users), movies )
# print( data )

print('\n인덱스 번호 0번의 행 정보')
print(data.ix[0])

# 성별에 따른 각 영화의 평균 평점은 pivot_table 메소드를 사용하면 된다.
# 평점을 대상으로, 색인은 제목을, 컬럼은 성별을 이용하여 평균 값을 구해주세요.
mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean') 
print('\n성별에 따른 영화 평점의 평균')
print( mean_ratings[:5] )

ratings_by_title = data.groupby('title').size()
print('\n영화 제목으로 그룹화한 수 평점 건수')
print( ratings_by_title[:10] )

active_titles = ratings_by_title.index[ratings_by_title >= 250]
print('\n250건 이상의 평점 정보가 있는 영화')
print( active_titles )

mean_ratings = mean_ratings.ix[active_titles]
print('\n성별에 따른 영화 평점의 평균(평점 건수가 250개 이상인 것만)')
print( mean_ratings )

top_female_ratings = mean_ratings.sort_index(ascending=True)
#top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
print('\n여성에게 높은 평점을 받은 영화 목록은')
print( top_female_ratings[:10] )

print('\n평점 차이 구하기')
print('남녀 간에 호불호가 갈리는 영화를 찾아 보자')
print('남녀 간의 평균 평점을 저장하기 위한 diff 컬럼을 하나 추가한다.')
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
print('sort_values() 함수는 내부의 diff 값을 기반으로 정렬해주는 함수이다.')
sorted_by_diff = mean_ratings.sort_values(by='diff')
print('\n여성들이 더 선호하는 순서대로 정렬하려면')
print('diff를 이용하여 정렬하면 된다.')
print( sorted_by_diff[:15] )

print('\n남성들이 더 선호하는 순서대로 정렬')
print(sorted_by_diff.sort_values(by='diff', ascending=False)[:15])

# 평점의 표준 편차를 구하고....
rating_std_by_title = data.groupby('title')['rating'].std()

print('active_titles : 250건 이상의 평점 정보가 있는 영화')
rating_std_by_title = rating_std_by_title.ix[active_titles]

print('\n내림차순으로 정렬')
print(rating_std_by_title.sort_values(ascending=False)[:15])

print('\n작업 완료')