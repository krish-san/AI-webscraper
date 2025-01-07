import streamlit as st
from scrape import scrape_web,extract_body,clean_body,split_dom_content

st.title("AI webscraper")

url=st.text_input("Enter a Website URL: ")

if st.button("scrape"):
    st.write("scraping")
    res=scrape_web(url)
    body_content=extract_body(res)
    cleaned_content=clean_body(res)

    st.session_state.dom_content=cleaned_content
    with st.expander("View DOM Content"):  #button
        st.text_area("DOM Content ",cleaned_content,height=350)

    if "dom_content" in st.session_state:
         parse_des=st.text_area("Specify the content you to parse .")
         if st.button("Parse Content"):
             if parse_des:
                 st.write("parsing the content")

                 dom_chunks=split_dom_content(st.session_state.dom_content)
