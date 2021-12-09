import pandas as pd
import numpy as np

#','가 있는 숫자를 int형으로 바꿔주는 함수
def num_to_int(x):
    if (type(x) is int) | (type(x) is float):
        return x
    else:
        return int(x.replace(',', ''))

def pro(x):
    if x.find('미만')>=0:
        return 0
    elif x=='ㅡ':
        return 0
    else:
        return x
#열을 모두 보여줌
# pd.set_option('display.max_columns', None)

df1 = pd.read_csv('./탐구등급구분 2.csv')
df1.drop([0, 1], inplace=True)  #필요없는 행 삭제
df1.set_index('등급', inplace=True)   #등급 열을 인덱스로 지정
df1 = df1.applymap(pro)
df1 = df1.astype(int)

df2 = pd.read_csv('./탐구표준점수.csv')
df2.fillna(0, inplace=True) #NaN 값들을 0으로 채움
df2.loc[1:] = df2.loc[1:].replace('계', 0)   #형변환을 위해 '계' 문자를 없앰
df2.loc[1:] = df2.loc[1:].applymap(num_to_int)  #형변환 실행

# for i in range(0, len(df1.columns)):
#     for j in range(0, 51):
#
#     print(df2.iloc[1, 3*i])


print(df2)
print(df1)

for sub in df1.columns:
    a = df2.iloc[:, 0:3]
    b = df1['성공적인 직업생활']

    print(a)
    print(b)

    score={}
    ba = {}
    score[1] = 50
    grade = 1
    s_df = pd.DataFrame()


    s_df['성공적인 직업생활'] = np.nan
    for i in range(1, 51):
        if i>1:
            score[i] = score[i-1] +(a.iloc[i, 0]-a.iloc[i-1,0])
        ba[score[i]] = round( (int(a.iloc[50, 1]) - int(a.iloc[i, 2]) + int(a.iloc[i,1]/2))/int(a.iloc[50, 1])*100)

        s_df.loc[i, '점수'] = score[i]
        s_df.loc[i, '등급'] = grade
        s_df.loc[i, '백분위'] = ba[score[i]]
        s_df.loc[i, '표준점수'] = a.iloc[i, 0]
        # s_df.loc[i, '등급']
        if a.iloc[i, 0] == b.loc[grade]:
            grade+=1






