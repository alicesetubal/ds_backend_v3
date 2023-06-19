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
    file_extractor_obj = FileExtrator() #criado uma instância para a classe.

 
    if arquivo is not None:
      file_type = arquivo.type
      #file_extractor = file_extractor(arquivo)
      extracted_text = None
      
      if arquivo.type == 'text/csv':
          
          texto = FileExtrator.extract_text_csv(arquivo)
      
      if arquivo.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            texto = FileExtrator.extract_text_xlsx(arquivo)
      
      elif arquivo.type == 'application/pdf':
            texto = FileExtrator.extract_text_pdf(arquivo)
            
      elif arquivo.type == 'text/plain':
            texto = FileExtrator.extract_text_txt(arquivo)
            
      elif arquivo.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
          texto = FileExtrator.extract_text_docx(arquivo)
          
      else:
    
       #st.stop()
       if extracted_text is not None:
           st.header("O texto extraido foi:")#Aqui apresenta o texto extraído no Streamlit
           st.code(extracted_text)