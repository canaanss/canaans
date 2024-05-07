from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import Sports
from st_on_hover_tabs import on_hover_tabs

st.set_page_config(
    page_title="Sports Films-wrestling",
    page_icon="🤼‍♂️",
    layout="wide",
)

# 禁用错误详情的显示
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

# ---- Perpare ----
img_Yolo = Image.open("images/摔跤.jpg")

# ---- Title ----
Sports.local_css("style/background.css")

left_column,right_column = st.columns((3,1))

with left_column:
    st.markdown(
        """
            <div style="background-color: #99b2d5; padding: 1rem; border-radius: 0.5rem; box-shadow: 0 0px 0px rgba(0, 0, 0, 0.1); color: white;">
            <h1 style="color: white;">摔跤-wrestling</h1>
            <p>Please choose the type of sports</p>
        </div>
        """,
        unsafe_allow_html=True
    )
with right_column:
    if st.button("返回首页"):
        st.switch_page("Sports.py")

# ---- Container with films ----
with st.container():
    st.write("---")
    image_column, text_column, margain_column = st.columns((0.5,2,0.5))
    with margain_column:
        st.link_button("进入详情", "http://localhost:8501/wrestling")
        
    with image_column:
    # insert image
        st.image(img_Yolo)

    with text_column:
        st.subheader("摔跤吧爸爸")
        st.write(
            """
            导演: 涅提·蒂瓦里
            编剧: 比于什·古普塔 / 施热亚·简 / 尼基尔·麦罗特拉 / 涅提·蒂瓦里
            主演: 阿米尔·汗 / 法缇玛·萨那·纱卡 / 桑亚·玛荷塔 / 阿帕尔夏克提·库拉那 / 沙克希·坦沃 / 塞伊拉·沃西 / 苏哈妮·巴特纳格尔 / 里特维克·萨霍里 / 吉里什·库卡尼
            """
        )
        code = '''类型: 剧情 / 家庭 / 传记 / 运动
                  制片国家/地区: 印度
                  语言: 印地语 / 英语
                  上映日期: 2017-05-05(中国大陆) / 2016-12-23(印度)
                  片长: 161分钟(印度) / 140分钟(中国大陆)'''
        st.code(code, language='txt')

# ---- Sidebar ----

st.markdown('<style>' + open('style/style_tab.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['首页', '电影', '运动'], 
                         iconName=['dashboard', 'money', 'economy'], 
                         styles = {'navtab': {'background-color':'#99b2d5',
                                                  'color': '#111',
                                                  'font-size': '18px',
                                                  'transition': '.3s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'},
                                       'tabOptionsStyle': {':hover :hover': {'color': 'white',
                                                                      'cursor': 'pointer'}},
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'},
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'}},
                             key="1")

    if tabs =='首页':
        st.switch_page("Sports.py")
    