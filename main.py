import streamlit as st

st.set_page_config(layout='wide')

st.write(
    """<iframe
  src="https://jupyter.org/try-jupyter/lab/"
  width="100%"
  height="700px"
></iframe>""",unsafe_allow_html = True
)