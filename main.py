
# file_path = '202406_202406_연령별인구현황_월간.csv'
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# CSV 파일 경로
file_path = '202406_202406_연령별인구현황_월간.csv'

def main():
    st.title("지역별 중학생 인구 비율")

    # CSV 파일 읽기
    data = pd.read_csv(file_path, encoding='cp949')  # 한글 인코딩 처리

    # 열 이름 확인
    st.write("데이터 열 이름: ", data.columns.tolist())

    # 필요한 열 이름 설정 (예: '행정구역별(읍면동)', '2023년06월_10세', '2023년06월_11세', '2023년06월_12세', '2023년06월_13세', '2023년06월_14세')
    region_col = '행정구역별(읍면동)'  # 실제 파일의 열 이름으로 수정
    age_cols = ['2023년06월_10세', '2023년06월_11세', '2023년06월_12세', '2023년06월_13세', '2023년06월_14세']  # 실제 파일의 열 이름으로 수정

    # 데이터 처리
    data = data[[region_col] + age_cols]

    # 사용자 입력 받기
    region = st.selectbox("지역을 선택하세요:", data[region_col].unique())

    # 선택한 지역 데이터 필터링
    region_data = data[data[region_col] == region]

    # 중학생 인구 비율 계산
    total_population = region_data[age_cols].sum(axis=1).values[0]
    middle_school_population = region_data[['2023년06월_13세', '2023년06월_14세']].sum(axis=1).values[0]
    middle_school_ratio = (middle_school_population / total_population) * 100

    # 원 그래프 그리기
    fig, ax = plt.subplots()
    labels = ['중학생 인구', '기타 인구']
    sizes = [middle_school_ratio, 100 - middle_school_ratio]
    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0)  # 중학생 인구 비율 강조

    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
           shadow=True, startangle=140)

    ax.axis('equal')  # 원 그래프를 원형으로 그리기

    st.pyplot(fig)

if __name__ == "__main__":
    main()
