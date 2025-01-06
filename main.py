import streamlit as st
from scrape import scrape_web

st.title("AI webscraper")

url=st.text_input("Enter a Website URL: ")

if st.button("scrape"):
    st.write("scraping")
    res=scrape_web(url)
    print(res)
