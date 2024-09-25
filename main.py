"""
用于文件下载
"""
# import os
# import json

# import streamlit as st
# import streamlit.components.v1 as components

# from src import utils as u


# cfg_path = u.read_json_file("./config/path.json")

# options = st.multiselect(
#     "多选选框",
#     ["Green", "Yellow", "Red", "Blue"],
#     ["Yellow", "Red"])

# st.write("You selected:", options)


# # st单选box
# option = st.selectbox(
#    "你想查看什么代码文件？",
#    u.get_file_names(cfg_path["cpp"]),
#    index=None,
#    placeholder="请选择第几节课",
# )




# def run():
# 	iframe_src = "https://flowus.cn/share/6781489a-d317-4da7-b07d-7414ab3def45?code=DD8PQT&embed=true"
# 	components.iframe(iframe_src,height=1000,width=1000)  # 你可以为组件添加高度和宽度

# if __name__ == "__main__":
# 	run()
import streamlit as st
from src.set_sandbox import execbox

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

CODE_SPACE_SETTINGS = {
    "public":"""
{}

""",
    "private":"""
import streamlit as st

print = st.write


""",
}
sendbox_settings = {
        'os': None,  # 禁止访问os模块
        'subprocess': None,  # 禁止访问subprocess模块
        'pickle': None,  # 禁止访问pickle模块
        'shutil': None,  # 禁止访问shutil模块
        '__import__': None,  # 禁止动态导入模块
        'eval': None,  # 禁止使用eval
        'exec': None,  # 禁止使用exec
        'globals': None,  # 禁止访问全局变量
        'locals': None,  # 禁止访问局部变量
        'open': None,  # 禁止使用open函数
        'file': None,  # 禁止使用file类型
        'execfile': None,  # 禁止使用execfile函数
        'input': None,  # 禁止使用input函数
        'raw_input': None,  # 禁止使用raw_input函数（Python 2）
    }
ks = sendbox_settings.keys()
s = f"{','.join(ks)} = [None]*{len(ks)}"
CODE_SPACE_SETTINGS["public"] = CODE_SPACE_SETTINGS["public"].format(s)
CONTENT = CODE_SPACE_SETTINGS["private"]+"\n"+CODE_SPACE_SETTINGS["public"]


from src import coder as c

code_block = c.CodeBlock()

code_block()
# try:
#     exec(content, local_scope)
# except Exception as e:
#     st.exception(e)

# def _new_sandbox():
#     import types
#     module = types.ModuleType("__main__")
#     return module.__dict__
# local_scope = _new_sandbox()

# exec("""
# open = None
# print = st.write
# print(open)
# """, local_scope)
# # print(local_scope)
