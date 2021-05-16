import pandas as pd
import pandas as pd
data = pd.read_excel('cardbin.xlsx', sheet_name=0, dtype=str, index_col=None)
data = data.drop('적용날짜', 1)
data = data.drop('카드코드', 1)
data.columns = ['BIN','ISSUER','CARDNAME','CARDTYPE']
data['CARDOWNERTYPE'] = 0

# 법인카드 판별로직
i = data[data['CARDNAME'].str.contains('법인')].index
for a in i:
  data.at[a,'CARDOWNERTYPE'] = 1

# 의미없는 카드 종류 삭제 로직 - 구매
i = data[data['CARDTYPE'].str.contains('구매')].index
data.drop(i, inplace=True)

# 의미없는 카드 종류 삭제 로직 - 버츄얼
i = data[data['CARDTYPE'].str.contains('버츄얼')].index
data.drop(i, inplace=True)

# 의미없는 카드 종류 삭제 로직 - 교통
i = data[data['CARDTYPE'].str.contains('교통')].index
data.drop(i, inplace=True)

# 의미없는 카드 종류 삭제 로직 - 판매
i = data[data['CARDTYPE'].str.contains('판매')].index
data.drop(i, inplace=True)

# 의미없는 카드 종류 삭제 로직 - 주유
i = data[data['CARDTYPE'].str.contains('주유')].index
data.drop(i, inplace=True)

# 의미없는 카드 종류 변경 로직 - 현대자사
i = data[data['CARDTYPE'].str.contains('현대자사')].index
for a in i:
  data.at[a,'CARDTYPE'] = '신용카드(일반)'

# 의미없는 카드 종류 변경 로직 - T&E카드
i = data[data['CARDTYPE'].str.contains('T&E카드')].index
for a in i:
  data.at[a,'CARDTYPE'] = '신용카드(일반)'
  
# 의미없는 카드 종류 변경 로직 - 현대연합BIN
i = data[data['CARDTYPE'].str.contains('현대연합BIN')].index
for a in i:
  data.at[a,'CARDTYPE'] = '신용카드(일반)'

# 의미없는 카드 종류 변경 로직 - 프리
i = data[data['CARDTYPE'].str.contains('프리')].index
for a in i:
  data.at[a,'CARDTYPE'] = '신용카드(일반)'

# 의미없는 카드 종류 변경 로직 - 산업은행
i = data[data['CARDTYPE'].str.contains('산업은행')].index
for a in i:
  data.at[a,'CARDTYPE'] = '신용카드(일반)'

# 의미없는 카드 종류 변경 로직 - 신세계
i = data[data['CARDTYPE'].str.contains('신세계')].index
for a in i:
  data.at[a,'CARDTYPE'] = '신용카드(일반)'

