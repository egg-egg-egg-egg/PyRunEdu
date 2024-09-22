from typing import Any
from streamlit_monaco import st_monaco



class CodeBlock:
    """
    创建一个代码块. 可以预设公开展示的代码，也可以设置隐藏的代码.

    private必须包含`{}`用于合并代码，最终的代码结果是private.formate(self._user_code)
    """
    def __init__(self,public:str = "",private:str = "",language:str = "python",safe:bool = True,in_form:bool =False,height:str="200px",theme:str = "vs-dark") -> None:
        self.preset_code = {
            "public": public,   # 预设公开的代码
            "private": private, # 预设隐藏的代码
        }
        self.height = height
        self.theme  = theme
        self.language = language

    
    def set_height(self,height:str):
        self.height = height
        return self
    
    def set_theme(self,theme:str):
        self.theme = theme
        return self
    
    def set_language(self,language):
        self.language = language
        return self

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self._user_code = st_monaco(
            value=self.preset_code['public'], 
            height=self.height,
            language=self.language,
            theme=self.theme,
            minimap=True
        )

