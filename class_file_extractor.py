import pandas as pd
import PyPDF2
import docx2txt





# Criei classes para deixar o código mais legível e organizado
class file_extractor:
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