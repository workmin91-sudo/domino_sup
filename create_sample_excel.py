"""샘플 엑셀 파일 생성 스크립트"""
import pandas as pd

# 샘플 데이터
data = {
    '품목명': ['노트북', '마우스', '키보드', '모니터', '헤드셋'],
    '현재재고': [5, 20, 15, 8, 12],
    '최소재고': [10, 15, 10, 10, 10],
    '단위': ['대', '개', '개', '대', '개'],
    '공급업체명': ['ABC전자', 'XYZ기업', 'ABC전자', 'DEF컴퓨터', 'XYZ기업'],
    '공급업체이메일': ['abc@example.com', 'xyz@example.com', 'abc@example.com', 'def@example.com', 'xyz@example.com']
}

df = pd.DataFrame(data)
df.to_excel('sample_inventory.xlsx', index=False, engine='openpyxl')
print('샘플 엑셀 파일이 생성되었습니다: sample_inventory.xlsx')
