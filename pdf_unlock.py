from PyPDF2 import PdfReader, PdfWriter
import sys

locked_file = input("Enter the name and path of the locked pdf") 
password = input("Enter the password to unlock the pdf"
unlocked_file = input("enter the name of the unlocked file") 


# Ler o PDF protegido
reader = PdfReader(locked_file)
if reader.is_encrypted:
    reader.decrypt(password)

# Criar um novo PDF sem senha
writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)

# Salvar o novo PDF sem senha
with open(unlocked_file, 'wb') as output_pdf:
    writer.write(output_pdf)

print(f"the pdf has been un locked")
