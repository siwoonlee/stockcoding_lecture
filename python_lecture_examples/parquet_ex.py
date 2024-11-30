import pandas as pd
import numpy as np
import time

# 샘플 데이터프레임 생성
df = pd.DataFrame(np.random.randn(10000, 50), columns=list(range(50)))

# to_csv 속도 측정
start_time = time.time()
df.to_csv('data.csv')
csv_time = time.time() - start_time

# to_excel 속도 측정
start_time = time.time()
df.to_excel('data.xlsx')
excel_time = time.time() - start_time

# to_parquet 속도 측정 (pyarrow 엔진 사용)
start_time = time.time()
df.to_parquet('data.parquet')
parquet_time = time.time() - start_time

# 결과 출력
print(f"CSV 저장 시간: {csv_time:.5f} 초")
print(f"Excel 저장 시간: {excel_time:.5f} 초")
print(f"Parquet 저장 시간: {parquet_time:.5f} 초")


# CSV 읽기 속도 측정
start_time = time.time()
df_csv = pd.read_csv('data.csv')
csv_read_time = time.time() - start_time

# Excel 읽기 속도 측정
start_time = time.time()
df_excel = pd.read_excel('data.xlsx')
excel_read_time = time.time() - start_time

# Parquet 읽기 속도 측정 (pyarrow 엔진 사용)
start_time = time.time()
df_parquet = pd.read_parquet('data.parquet')
parquet_read_time = time.time() - start_time

# 결과 출력
print(f"CSV 읽기 시간: {csv_read_time:.5f} 초")
print(f"Excel 읽기 시간: {excel_read_time:.5f} 초")
print(f"Parquet 읽기 시간: {parquet_read_time:.5f} 초")
