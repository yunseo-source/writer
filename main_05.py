from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI()

st.title('AI 작사가')

content = st.text_input('작사할 주제를 제시해주세요。')

if st.button('작사 요청하기'):
    with st.spinner('노래 가사 작성 중입니다...'):
        result = chat_model.invoke(content + "에 대한 노래의 작사를 해 줘")
        st.write(result.content)