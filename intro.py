import streamlit as st
st.title("My first Streamlit App Surampudi Praveen Kumar")
st.write("Welcome! This app calculates the square of a number.")
st.header("Select a number")
st.markdown("""""", unsafe_allow_html=True)
number=st.slider("Pick a number",0,1000,5)
st.subheader("Result")
squared_number = number * number
st.write(f"The square of **{number}** is **{squared_number}**.")
