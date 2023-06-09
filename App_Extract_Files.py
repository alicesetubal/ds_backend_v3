import pandas as pd
import streamlit as st
import PyPDF2 
import io
import docx2txt

#Criei classes para deixar o código mais legível e organizado
class File_Extractor:
    def __init__(self, file):
        self.file = file

#Primeiro tenho que definir as funções para extrair o texto dos arquivos
    def extract_text_csv(self):
     data_frame = pd.read_csv(self.file)
     texto = data_frame.to_string(index=False)
     return texto

    def extract_text_xlsx(self):
      data_frame = pd.read_excel(self.file)
      texto = data_frame.to_string(index=False)
      return texto

    
    def extract_text_pdf(self):
      reader= PyPDF2.PdfReader(self.file)
      numPages = len(reader.pages)
      texto= ''
      for page in range(numPages):
        texto += reader.pages[page].extract_text()
      return texto
        

    def extract_text_txt(self):
      texto = self.file.getvalue().decode()
      return texto

    def extract_text_docx(self):
      texto = docx2txt.process(self.file)
      return texto
    
st.header("Welcome to Extract File :smile:") 
#Local onde o utilizador irá adicionar o arquivo
arquivo = st.file_uploader('Insira seu arquivo:' , type=['csv', 'xlsx', 'pdf', 'txt', 'docx'])


#Aqui foi definido cada MIME para o streamlit reconhecer o tipo de arquivo
#Utilizei o if para verificar qual tipo de arquivo
if arquivo is not None:
    
    file_extractor = File_Extractor(arquivo)
    
    
    if arquivo.type == 'text/csv':
        
        texto = file_extractor.extract_text_csv()
    
    if arquivo.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
          texto = file_extractor.extract_text_xlsx()
    
    elif arquivo.type == 'application/pdf':
          texto = file_extractor.extract_text_pdf()
          
    elif arquivo.type == 'text/plain':
          texto = file_extractor.extract_text_txt()
          
    elif arquivo.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        texto = file_extractor.extract_text_docx()
        
else:
  
  st.stop()
#Aqui apresenta o texto extraído no Streamlit
st.header("O texto extraido foi:")
st.code(texto)