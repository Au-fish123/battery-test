import streamlit as st
import time

st.set_page_config(page_title="電量測試", page_icon="🔋")

st.title("電量測試")

if "show_result" not in st.session_state:
    st.session_state.show_result = False

if st.button("執行"):
    # 重新執行時先清掉舊結果
    st.session_state.show_result = False

    progress = st.progress(0)
    result_area = st.empty()

    for i in range(101):
        time.sleep(0.03)
        progress.progress(i)

    st.session_state.show_result = True
    result_area.success("有電")