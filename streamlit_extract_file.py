import pandas as pd
import streamlit as st
#import PyPDF2
#import docx2txt
from class_file_extractor import FileExtrator

 
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True


    


if check_password():
    st.header("Welcome to Extract File :smile:") 
    arquivo = st.file_uploader('Insira seu arquivo:' , type=['csv', 'xlsx', 'pdf', 'txt', 'docx'])#Local onde o utilizador irá adicionar o arquivo
    

 
    if arquivo is not None:
      file_extract_obj = FileExtrator(arquivo)
      
      if arquivo.type == 'text/csv':
          
           texto = file_extract_obj.extract_text_csv()
      
      if arquivo.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            texto = file_extract_obj.extract_text_xlsx()
      
      elif arquivo.type == 'application/pdf':
            texto = file_extract_obj.extract_text_pdf()
            
      elif arquivo.type == 'text/plain':
            texto = file_extract_obj.extract_text_txt()
            
      elif arquivo.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            texto = file_extract_obj.extract_text_docx()
          
      else:
       st.stop() 
       
    st.header("O texto extraido foi:")#Aqui apresenta o texto extraído no Streamlit
    st.code(texto)