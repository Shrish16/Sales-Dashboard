import pandas as pd
import streamlit as st
import plotly.express as px

st.title("📊 Sales Dashboard")

df = pd.read_csv("data.csv")

region = st.selectbox("Select Region", df["Region"].unique())
filtered = df[df["Region"] == region]

fig = px.bar(filtered, x="Product", y="Sales", color="Product")
st.plotly_chart(fig)

st.write(filtered)
