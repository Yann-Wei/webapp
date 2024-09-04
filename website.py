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

<img src= https://lens.google.com/search?ep=gsbubb&hl=en-LU&re=df&p=AbrfA8os4HOF3mUmr_WEsvj3etKj4FUN-jb5eyBMR7jZbVFRR-ssKFcK8to9AEIh2LXkjKW8bR_XLZmdGJ-dNB9OWdJfiu08923oGT_kVSN01rft6CCvqYfoYFXD_LN4KRz_E-Q8iqmy_chDPx248TkFapQQJs05wuJLsbkjuMhJn7e1QkFVMtGlRIbNmDPjfl_GNiEntotXMETQew%3D%3D#lns=W251bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsIkVrY0tKR1UwWldRME1qWTNMVFE1T0dJdE5HTTFOUzA1WmpZMExUWmxObUl6TURFMVpqbGtPUklmU1RSVkxVOVFkRTlhYkdObU5FWXpjRVF5ZGpoaFkzUmxNVmxmYjBkNGF3PT0iLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsWyI2ODBlNDZlYS0yODNkLTQzODQtYjNhMi02OWE4OTQ0ZWViYWUiXV0=/>
"""
st.markdown(html_content, unsafe_allow_html =True)





  
  
  
