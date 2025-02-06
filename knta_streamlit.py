import streamlit as st

def process_numbers(numbers_str):
    try:
        # 숫자를 리스트로 변환
        numbers = list(map(int, numbers_str.split()))
        
        # 중복 제거 및 정렬
        unique_numbers = sorted(set(numbers))
        
        # SQL IN 절 형식으로 변환
        in_clause = ', '.join([f"'{num}'" for num in unique_numbers])
        
        # SELECT 문 생성
        select_query = f"SELECT REPORT_KEY, STUDY_KEY, REPORT_BUFFER_LOB FROM REPORT WHERE REPORT_KEY IN ({in_clause});"
        
        return select_query
    except ValueError:
        return "잘못된 입력입니다. 숫자만 입력해주세요."

# Streamlit UI 구성
st.title("KNTA Report Clear v1.13")
st.write("숫자를 입력하면 SQL 쿼리를 생성합니다.")

# 사용자 입력
numbers_input = st.text_area("숫자를 입력하세요 (공백으로 구분)")

if st.button("변환"):  
    result_query = process_numbers(numbers_input)
    
    # 결과 출력
    st.text_area("결과 SQL 쿼리", result_query, height=150)

    # 클립보드 복사 대신 버튼 제공
    st.code(result_query, language="sql")  # 코드 블록 스타일 적용
    
    st.write("🔹 **직접 복사하려면 SQL 쿼리를 클릭하세요!**")