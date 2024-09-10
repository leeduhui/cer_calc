import pandas as pd
import numpy as np
from difflib import ndiff

# Levenshtein Distance 유사 계산 함수 (difflib 기반)
def levenshtein_distance_ndiff(ref_text, hyp_text):
    """
    두 텍스트 사이의 Levenshtein Distance를 difflib.ndiff를 사용해 계산하는 함수.
    """
    # ndiff를 사용해 두 텍스트의 차이점 계산
    diff = list(ndiff(ref_text, hyp_text))
    
    # 삽입, 삭제, 교체를 계산
    levenshtein_dist = sum(1 for d in diff if d[0] in {'-', '+'})
    
    return levenshtein_dist

# Levenshtein Distance 계산 함수 (동적 프로그래밍 기반)
def levenshtein_distance_dp(ref, hyp):
    """
    두 텍스트 사이의 Levenshtein Distance를 동적 프로그래밍으로 계산하는 함수.
    """
    m, n = len(ref), len(hyp)
    dp = np.zeros((m + 1, n + 1), dtype=int)

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if ref[i - 1] == hyp[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,     # 삭제
                               dp[i][j - 1] + 1,     # 삽입
                               dp[i - 1][j - 1] + 1) # 치환

    return dp[m][n]

# CER 계산 함수 (동적 프로그래밍 기반 Levenshtein Distance 사용)
def calculate_cer(ref_text, hyp_text):
    lev_dist = levenshtein_distance_dp(ref_text, hyp_text)  # 여기서 dp 버전을 사용
    total_chars = len(ref_text)
    
    # CER 계산 (최대값을 1.0으로 제한)
    cer = min(lev_dist / total_chars if total_chars > 0 else 1.0, 1.0)
    #cer = lev_dist / len(ref_text)
    
    return cer

# 엑셀 파일 불러오기
file_path = './데이터(네이버)_유니바api저장_ver1.1.xlsx'
sheet_name = 'WEB&CER(115)'
df = pd.read_excel(file_path, sheet_name=sheet_name)

# H2행부터 H116행까지의 데이터만 선택
df_subset = df.loc[1:115].copy()  # 슬라이스의 복사본을 생성

# Origin Data와 naver_clova_stt_result(2023) 비교하여 CER 계산 후 P열에 저장
df_subset['P'] = df_subset.apply(lambda row: calculate_cer(str(row['Origin Data']), str(row['univaResult'])), axis=1)

# Origin Data와 univaResult 비교하여 CER 계산 후 Q열에 저장
df_subset['Q'] = df_subset.apply(lambda row: calculate_cer(str(row['Origin Data']), str(row['univaResult(2024)'])), axis=1)

# 원본 데이터프레임에 결과 병합
df.loc[1:115, 'P'] = df_subset['P']
df.loc[1:115, 'Q'] = df_subset['Q']

# 결과를 엑셀 파일로 저장
output_file_path = './output_데이터(네이버)_유니바api저장_ver1.1.xlsx'
df.to_excel(output_file_path, sheet_name=sheet_name, index=False)

