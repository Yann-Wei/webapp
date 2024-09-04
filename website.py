import streamlit as st
st.set_page_config(page_title="Hello Webpage", layout= "wide")

#header
st.subheader("This is a subtitle")
st.title("This is a title")
st.write("Here is where you write")
st.write("[Learn More> ](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)")
if 'count' not in st.session_state:
  st.session_state.count = 0

if st.button("Do you want an euro?"):
  st.session_state.count += 1
  
if st.session_state.count != 0:
  st.write("You have",st.session_state.count,"€")

html_content= """
<h1> This is a title </h1>
<p> This is my first website </p>
"""
st.markdown(html_content, unsafe_allow_html =True)

user_input= st.text.input()
if user_input:
  st.write(user_input)




  
  
  
