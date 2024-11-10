import streamlit as st
import streamlit_authenticator as stauth

# 初始化认证器
authenticator = stauth.Authenticate(...)

# 登录表单
authenticator.login('Login', 'main')

if st.session_state["authentication_status"]:
    # 用户已登录,显示主要内容
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    # 显示应用的主要内容
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')