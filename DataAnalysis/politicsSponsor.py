import pandas as pd 

# 미국 연방 선거 관리 위원회 정치 활동 후원금 데이터
# http://www.fec.gov/disclosurep/PDownload.do
# 기부자 이름(cand_nm), 직업, 고용 형태, 주소, 기부 금액(contb_receipt_amt)

fec = pd.read_csv('P00000001-ALL.csv')
print('\ninfo() 함수는 요약한 내용을 이용하여 간단히 보여 주는 함수이다.')
print(fec.info())

print('\n다음과 같은 형태로 데이터가 저장이 된다.')
print(fec.ix[123456])

print('\nunique() 함수를 이용하여 모든 정당 후보의 목록을 얻자.')
unique_cands = fec.cand_nm.unique()
print( unique_cands )
print('-' * 50)
print( unique_cands[2] )

print('\n소속 정당은 사전을 이용하여 표시할 수 있다.')
parties = {'Bachmann, Michelle':'Republican',
           'Cain, Herman':'Republican',
           'Gingrich, Newt':'Republican',
           'Huntsman, Jon':'Republican',           
           'Johnson, Cary Earl':'Republican',
           'McCotter, Thaddeus G':'Republican',
           'Obama, Barack':'Democrat',
           'Paul, Ron':'Republican',
           'Pawlenty, Timothy':'Republican',
           'Perry, Rick':'Republican',
           'Romer, Charles E. "Buddy" III':'Republican',
           'Romney, Mitt':'Republican',
           'Santorum, Rick':'Republican'
           }

print('\n위 사전 정보를 이용하여 후보 이름으로 부터 정당 배열을 구할 수 있다.')
print('123456:123461은 샘플로 5개만 추출해본 것이다.')
print( fec.cand_nm[123456:123461] )
print('-' * 50)
print( fec.cand_nm[123456:123461].map(parties) )

print('\n정당 컬럼을 추가한다.')
fec['party'] = fec.cand_nm.map(parties)


print('\nvalue_counts() 함수는 도수를 계산하여 역순으로 보여 주는 함수이다.')
print(fec['party'].value_counts())
print('-' * 50)

print('\n기부금(contb_receipt_amt)이 양수인 항목만 골라내기')
print((fec.contb_receipt_amt > 0 ).value_counts())
fec = fec[fec.contb_receipt_amt > 0 ]

print('\n버락 오바마와 미트 롬니가 양대 후보이므로 이 두 후보의 기부금 정보만 따로 추려 낸다.')
# isin : 데이터베이스의 in 절과 유사한 기능을 한다.
fec_mrbo = fec[fec.cand_nm.isin(['Obama, Barack', 'Romney, Mitt'])]
      
# 직장 및 피고용별 기부 통계
print('-' * 50)
print(fec.contbr_occupation.value_counts()[:10])

occ_mapping = {
        'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDED',
        'INFORMATION REQUESTED':'NOT PROVIDED',
        'INFORMATION REQUESTED (BEST EFFORTS)':'NOT PROVIDED',
        'C.E.O.':'CEO'   
    }

# 매핑 정보가 없는 직업은 키를 그래도 반영한다.
f = lambda x : occ_mapping.get(x, x)
fec.contbr_occupation = fec.contbr_occupation.map(f)

eemp_mapping = {
        'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDED',
        'INFORMATION REQUESTED':'NOT PROVIDED',
        'SELF':'SELF-EMPLOYED',
        'SELF EMPLOYED':'SELF-EMPLOYED'   
    }

# 매핑 정보가 없는 직업은 키를 그래도 반영한다.
f = lambda x : eemp_mapping.get(x, x)
fec.contbr_employer = fec.contbr_employer.map(f)

by_occupation = fec.pivot_table('contb_receipt_amt', index='contbr_occupation', \
                           columns='party', aggfunc='sum') 

over_2mm = by_occupation[by_occupation.sum(1) > 2000000 ]
print('-' * 50)
print( over_2mm )
over_2mm.plot(kind='barh')

import matplotlib.pyplot as plt
plt.savefig('직업별 기부 순위.png', dpi=400)

def get_top_amounts(group, key, n=5):
    totals = group.groupby(key)['contb_receipt_amt'].sum()
    
    # totals를 key의 값의 내림차순으로 정렬한다.
    return totals.sort_values(ascending=False)[-n]

grouped = fec_mrbo.groupby('cand_nm')
print('-' * 50)
print(grouped.apply(get_top_amounts, 'contbr_occupation', n=7))
print('-' * 50)
print(grouped.apply(get_top_amounts, 'contbr_employer', n=10))

import numpy as np 
# 기부 금액
bins = np.array([0, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000])
labels = pd.cut(fec_mrbo.contb_receipt_amt, bins )
print('-' * 50)
print( labels )

grouped = fec_mrbo.groupby(['cand_nm', labels])
print('-' * 50)
print(grouped.size().unstack(0))
      
bucket_sums = grouped.contb_receipt_amt.sum().unstack(0)
print('-' * 50)
print( bucket_sums )

normed_sums = bucket_sums.div( bucket_sums.sum(axis=1), axis=0)
print('-' * 50)
print( normed_sums )

normed_sums[:-2].plot(kind='barh', stacked=True)
plt.savefig('기부 금액 규모별 후보당 기부 비율.png', dpi=400)

# 주별 기부 통계
grouped = fec_mrbo.groupby(['cand_nm', 'contbr_st'])
totals = grouped.contb_receipt_amt.sum().unstack(0).fillna(0)
totals = totals[totals.sum(1) > 100000]
print('-' * 50)
print(totals[:10])

percent = totals.div(totals.sum(1), axis = 0 )
print('-' * 50)
print(percent[:10])
print('\n작업 완료')