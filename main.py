"""
用于文件下载
"""
import streamlit as st
# from src.set_sandbox import execbox

st.set_page_config(
    page_title="Run Python",
    page_icon=":shark:",
    layout="centered",
    initial_sidebar_state="expanded",  # 设置侧边栏初始为展开状态
    menu_items = {
        
        "about": "由码力十足的黄老师完成",
    }
)

# 可以在这个路径修改运行按钮的英文"D:\ProgramData\anaconda3\envs\EduTools\Lib\site-packages\streamlit_ace\frontend\build\static\js\main.707cd2a5.chunk.js"
# 放置在侧边栏
# with st.sidebar:

with st.sidebar:
    st.write("# 介绍")

    st.info("""
        这是一个基于Streamlit的Python代码在线运行网页，可以运行Python代码并实时显示输出。
        
        你可以编写Python代码，然后点击运行按钮，就可以看到运行结果。
                """)
    
    st.info("敲重点！由于基于streamlit，所以我们可以在页面上使用streamlit的组件！快复制下面代码玩玩！")

    st.code("st.balloons()")

    st.warning("如果一开始你看到红色的运行按钮无法使用，在输入框里输入任意字符即可使用！")



def _new_sandbox():
    import types
    module = types.ModuleType("__main__")
    return module.__dict__
local_scope = _new_sandbox()

from streamlit_monaco import st_monaco
code = st_monaco(language="python",minimap=True,theme="vs-dark")

if st.button("运行",key="code_run",type="primary"):
    exec(code, local_scope)
# print(local_scope)
