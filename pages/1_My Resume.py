import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

path = "assets/My Resumé.pdf"

with open(path, 'rb') as f:
   st.download_button('Download', f, 'Copeland Carter Resume.pdf', mime='application/pdf')

pdf_viewer(path)
