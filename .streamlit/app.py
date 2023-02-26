import streamlit as st
from functions import summarize
import openai
import os
try:
    openai.api_key = "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"


    # initialize state variable 
    if "summary" not in st.session_state:
        st.session_state["summary"] = ""

    st.title("Text Summarizer")

    input_text = st.text_area(label='Enter full text:', value="", height=250)


    st.button(
        "Submit",
        on_click=summarize,
        kwargs={"prompt": input_text},
    )


    # configure text area to populate with current state of summary
    output_text = st.text_area(label='Summarized text:', value=st.session_state["summary"], height=250)
except:
  st.write('There was an error =(')