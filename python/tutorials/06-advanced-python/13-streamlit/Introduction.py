from cProfile import label

import streamlit as st
import pandas as pd

data = {
    "Name" : ["Ash","Lata"],
    "Marks" : [98,34]
}
df = pd.DataFrame(data)

st.title("Expense tracking system")
st.header("Expense tracking system")
st.subheader("Expense tracking system")
st.text("Expense tracking system")

st.date_input("Choose the Expense date:")
st.text_input("Enter you name: ")
st.number_input("Enter you age: ", min_value=12, max_value= 150)
st.table(df)

# st.line_chart([1,2,3,4,5])
# st.bar_chart(data, x = "Name" , y = "Marks", color = "#53698d")

value = st.slider(label= "marks")
st.write("Select Value:", value)

st.checkbox("Yes/No")

st.selectbox("Foods",["Pizza","Burger","Samosa"],label_visibility="collapsed")

st.multiselect("numbers",[1,2,3,4,5],max_selections=2)