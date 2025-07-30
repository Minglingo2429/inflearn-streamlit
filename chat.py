import streamlit as st
from dotenv import load_dotenv

from llm import get_ai_response

# 초기 설정
st.set_page_config(page_title="노동법 챗봇", page_icon="🤖")
st.title("🤖 노동법 챗봇")
st.caption("노동법에 관련된 모든 것을 답해드립니다!")
# env 파일에서 API 키를 로드
load_dotenv()

# 세션 상태 초기화 및 메시지 리스트 설정
if 'message_list' not in st.session_state:
    st.session_state.message_list = []
    
print(f"before == {st.session_state.message_list}")

# 대화 UI에 이전 대화 메시지 표시
for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])

    
if user_question := st.chat_input(placeholder="노동법에 관련된 궁금한 내용들을 말씀해주세요!"):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})
    
    with st.spinner("답변을 생성하는 중입니다..."):
        ai_response = get_ai_response(user_question)
        with st.chat_message("ai"):
            st.write_stream(ai_response) # generator 받는 것, return 값이 stream 형태로 오기 때문에 st.write_stream 사용
        st.session_state.message_list.append({"role": "ai", "content": user_question})

