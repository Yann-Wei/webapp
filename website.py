import streamlit as st
st.set_page_config(page_title="Hello Webpage", layout= "wide")

#header
st.subheader("This is a subtitle")
st.title("This is a title")
st.write("Here is where you write")
st.write("[Learn More> ](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)")
if 	'count' not in st.session_state:
  st.session_state.count = ""

if st.button("Click me"):
  st.session_state.count +=1
st.write(st.session_state.count)
  
  
  
