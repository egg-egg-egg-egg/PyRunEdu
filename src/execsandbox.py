import streamlit as st
from streamlit_ace import st_ace


FONT_SIZE = 14
EXTRA_LINES = 2
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
CODE_SPACE_SETTINGS = """
{}
"""
# CODE_SPACE_SETTINGS = {
#     "public":"""
# {}

# """,
#     "private":"""
# import streamlit as st

# print = st.write


# """,
# }
# ks = sendbox_settings.keys()
# s = f"{",".join(ks)} = [None]*{len(ks)}"
# CODE_SPACE_SETTINGS["public"].format(s)
# CONTENT = CODE_SPACE_SETTINGS["private"]+"\n"

def editor(body="",
        button_label="Run",
        autorun=False,
        height=None,
        line_numbers=False,
        key=None,):
    body = body.strip()

    if height is None:
        nlines = body.count("\n")
        if nlines < 3:
            nlines = 3
        height = (FONT_SIZE + 2) * (nlines + 1 + EXTRA_LINES)

    kwargs = dict(
        value=body,
        language="python",
        theme="dawn",
        keybinding="vscode",
        font_size=FONT_SIZE,
        height=height,
        show_gutter=line_numbers,
        key=key,
    )

    # TODO: Find some way to enter small text so we can show a label above the editor, just like
    # Streamlit's normal components.
    # TODO: Make this collapsible.
    content = st_ace(**kwargs)

def execbox(
        body="",
        button_label="Run",
        autorun=False,
        height=None,
        line_numbers=False,
        key=None,
    ):
    """Display a button widget.

    Parameters
    ----------
    body : str
        The initial code to show in the execbox.
    button_label : str
        The label to use for the "Run" button.
    autorun : bool
        Whether the code should execute with each keystroke.
    height : int or None
        The height of the execbox, in pixels. If None, calculates the height smartly to fill the
        content and a couple more lines.
    line_numbers : bool
        Whether to show line numbers.
    key : str or None
        An optional string to use as the unique key for the widget. If this is omitted, a key will
        be generated for the widget based on its content. Multiple widgets of the same type may not
        share the same key.


    Returns
    -------
    str
        The source code in the execbox.
    """

    body = body.strip()

    if height is None:
        nlines = body.count("\n")
        if nlines < 3:
            nlines = 3
        height = (FONT_SIZE + 2) * (nlines + 1 + EXTRA_LINES)

    kwargs = dict(
        value=body,
        language="python",
        theme="dawn",
        keybinding="vscode",
        font_size=FONT_SIZE,
        height=height,
        show_gutter=line_numbers,
        key=key,
    )

    # TODO: Find some way to enter small text so we can show a label above the editor, just like
    # Streamlit's normal components.
    # TODO: Make this collapsible.
    content = st_ace(**kwargs)

    # TODO: Change AceEditor (or use our own editor frontend) so we don't rerun the script on every
    # keystroke when autorun is False.
    if autorun:
        run = True
    else:
        autokey = hash((body, button_label, autorun, height, line_numbers, key))
        run = st.button(button_label, key=autokey)

    if run:
        # TODO: Allow people to set their own local_scope (so two execboxes call share scopes!). For
        # this we'll likely need to use session state, though.
        local_scope = _new_sandbox()

        try:
            # TODO: Add a new container and a `with` block here!
            exec(CODE_SPACE_SETTINGS.format(content), local_scope)
        except Exception as e:
            st.exception(e)

    return content


def _new_sandbox():
    import types
    module = types.ModuleType("__main__")
    # module.__dict__.update()
    return module.__dict__
