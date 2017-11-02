from konlpy.tag import Kkma
from konlpy.utils import pprint
kokoma = Kkma()

text = u'명사만을 추출하여 워드클라우드를 그려봅니다.'
print('조금만 기다리세요.')
print( kokoma.nouns(text))