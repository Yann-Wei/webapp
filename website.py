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

user_input= st.text_area("encrypt message:")
length= len(user_input)
a=0
b=length
while a<length:
  if length%2 ==0:
    st.write((b+100)//2, end="")
    a+=1
    b+=3
  elif length%2 !=0:
    st.write((b+69)//2, end="")
    a+=1
    b*=3
  
  





  
  
  
