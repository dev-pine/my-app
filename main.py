# 필요한 라이브러리 불러오기
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# CSV 파일 경로
file_path = '202406_202406_연령별인구현황_월간.csv'

# CSV 파일 읽기
data = pd.read_csv(file_path, encoding='cp949')  # 한글 인코딩 처리

# 데이터 확인
st.write(data.head())
# 스트림릿 코드
def main():
    st.title("지역별 중학생 인구 비율")

    # CSV 파일 읽기
    data = pd.read_csv(file_path, encoding='cp949')  # 한글 인코딩 처리

    # 데이터 처리
    # 예시 데이터 컬럼명이 다를 수 있으므로, 컬럼명을 확인 후 적절히 수정해야 합니다.
    # 여기서는 '행정구역', '10세', '11세', '12세', '13세', '14세' 컬럼이 있다고 가정합니다.
    data = data[['행정구역', '10세', '11세', '12세', '13세', '14세']]

    # 사용자 입력 받기
    region = st.selectbox("지역을 선택하세요:", data['행정구역'].unique())

    # 선택한 지역 데이터 필터링
    region_data = data[data['행정구역'] == region]

    # 중학생 인구 비율 계산
    total_population = region_data[['10세', '11세', '12세', '13세', '14세']].sum(axis=1).values[0]
    middle_school_population = region_data[['13세', '14세']].sum(axis=1).values[0]
    middle_school_ratio = (middle_school_population / total_population) * 100

    # 원 그래프 그리기
    fig, ax = plt.subplots()
    labels = ['중학생 인구', '기타 인구']
    sizes = [middle_school_ratio, 100 - middle_school_ratio]
    colors = ['#ff9999','#66b3ff']
    explode = (0.1, 0)  # 중학생 인구 비율 강조

    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=140)

    ax.axis('equal')  # 원 그래프를 원형으로 그리기

    st.pyplot(fig)

if __name__ == "__main__":
    main()
