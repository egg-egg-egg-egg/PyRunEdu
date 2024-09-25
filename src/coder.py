from set_sandbox import base_safe_builtins

import streamlit as st
from streamlit_monaco import st_monaco

import traceback
import sys
import io


class CodeBlock:
    """
    将一些代码编辑器封装成的可编辑代码块
    """
    def __init__(self, 
                 title: str = None, 
                 description: str = None, 
                 preset_code: str = None, 
                 height: int = 300, 
                 language: str = "python", 
                 theme: str = "vs-dark"):
        
        self.title = title
        self.description = description
        self.preset_code: str = preset_code, 
        self.height: int = height, 
        self.language: str = language, 
        self.theme: str = theme

        self.user_code = ""

    def displayBlock(self,):
        # 在 Streamlit 页面上展示题目和代码输入框
        if self.title:
            st.markdown(self.title)
        if self.description:
            st.write(self.description)
        
        # 接收用户输入的代码
        self.user_code = st_monaco(
            value=self.preset_code,
            height=self.height,
            language=self.language,
            theme=self.theme,
            minimap=True
        )
        
        return self

    def run_code(self, code: str):
        # 捕获代码执行中的异常并展示到页面
        try:
            # 创建一个新的环境，捕获执行结果
            result = self.execute_in_sandbox(code)
            st.success("代码执行成功！")
            st.text_area("输出结果：", result)
        except Exception as e:
            st.error("代码执行失败：")
            st.text(traceback.format_exc())

    def execute_in_sandbox(self, code: str) -> str:
        """执行用户代码的沙盒函数，防止不安全的代码运行。"""
        # 创建沙盒环境
        # 方法1: 使用 exec()，但要注意限制功能
        # 方法2: 使用 subprocess 进行独立进程调用
        
        # 使用 io.StringIO() 捕获输出
        output = io.StringIO()
        sys.stdout = output  # 将标准输出重定向到 output

        try:
            # 执行用户代码 (注意这里需要保证安全性，适当做出限制)
            exec(code, {})  # 仅提供空白字典，防止访问不安全的全局变量
        finally:
            sys.stdout = sys.__stdout__  # 恢复标准输出

        return output.getvalue()


class IOCodeBlock:
    """
    IO风格的可运行代码块
    """
    pass


class LCCodeBlock:
    """
    力扣风格的可运行代码块
    """
    pass