import streamlit as st
from streamlit_chat import message
 
from bardapi import Bard

def query_optimizer(user_input):
    optimized_query = user_input
    # query opitmizer 하는 코드 넣기
    # optimize된 query 문장을 반환 
    return optimized_query

def generate_response(query):
    response = bard.get_answer(query)['content']
    # bard로 부터 optimize된 쿼리를 질문하여 답을 받아옴
    # bard로 부터 온 답변을 반환
    return response
 
def prompt_optimizer(response):
    optimized_prompt = response
    # Prompt optimize 하는 코드 넣고 결과 반환
    return optimized_prompt

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
 
if 'past' not in st.session_state:
    st.session_state['past'] = []
 
with st.form('form', clear_on_submit=True):
    user_input = st.text_input('You: ', '', key='input')
    submitted = st.form_submit_button('Send')
 
if submitted and user_input:
    
    #token = st.secrets["token"]
    token = 'dwg5yL4kwsQkay_WLnMrqlruwXvYokR5Ji4G_sUsuCSYczVdC9Y17Ampcp8h_x5KdhyBFA.'
    
    bard = Bard(token=token)

    optimized_query=query_optimizer(user_input) # 이 함수에서 쿼리 optimize하기
    
    response = generate_response(user_input) # optimze한 쿼리를 바드를 통해 답변 받아오기
    
    optimized_prompt = prompt_optimizer(response)
    
    st.title('✨ Graduation Project ✨')
    st.session_state.past.append(optimized_query)
    st.session_state.generated.append(optimized_prompt)
