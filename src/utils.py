import os
import json

import streamlit as st

@st.cache_data
def get_file_names(directory):
    """
    获取指定目录下的所有文件名（不包括子目录中的文件）。
    :param directory: 目录路径。
    :return: 文件名列表。
    """
    try:
        # 列出指定目录下的所有条目
        entries = os.listdir(directory)
        # 过滤出文件（排除目录）
        file_names = [name for name in entries if os.path.isfile(os.path.join(directory, name))]
        return tuple(file_names)
    except Exception as e:
        print(f"Error occurred: {e}")
        return ()

@st.cache_data
def read_json_file(file_path):
    """
    读取指定路径的JSON文件并返回其内容。
    :param file_path: JSON文件的路径。
    :return: 成功时返回JSON解析后的Python对象（通常是字典或列表），失败时返回None。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return f"错误：文件 {file_path} 未找到。"
    except json.JSONDecodeError:
        return f"错误：文件 {file_path} 不是有效的JSON格式。"
    except Exception as e:
        return f"读取文件时发生未知错误：{e}"
    

# 示例使用
# file_path = "example.json"
# json_data = read_json_file(file_path)
# if json_data:
#     print("成功读取JSON数据：", json_data)
# else:
#     print("读取JSON文件失败。")