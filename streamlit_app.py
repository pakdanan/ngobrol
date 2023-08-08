import pandas as pd
import numpy as np
import streamlit as st
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
area = st.checkbox('Area Chart')
line = st.checkbox('Line Chart')
if area:
    st.area_chart(chart_data)
if line:
    st.line_chart(chart_data)
