import streamlit as st

from bbquote.lib import get_quote

result = get_quote()
author = result['author']
quote = result['quote']  # assuming the function returns an author and a quote

st.write('# Welcome to the bbquote interface')
st.write(f"{quote}, {author}")
