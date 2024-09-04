import streamlit as st
st.set_page_config(page_title="Hello Webpage", layout= "wide")

#header
st.subheader("This is a subtitle")
st.title("This is a title")
st.write("Here is where you write")
st.write("[Learn More> ](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)")
count=0
if st.button("Click me"):
  count+=1
  st.write(count)
  
  
