import streamlit as st
import pandas as pd
import numpy as np


data=pd.read_csv("tips.csv")
st.title("TIPS DATASET")
st.subheader("The data is with us")
st.write(data)

st.bar_chart(data,x="sex",y="total_bill")
st.line_chart(data,x="billdate",y="total_bill")

st.write("")


