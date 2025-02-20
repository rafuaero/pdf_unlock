from PyPDF2 import PdfReader, PdfWriter
import sys

# .gitignore is configured to ignore pdf files

locked_file = input("Enter the name and path of the locked pdf:  ") 
password = input("Enter the password to unlock the pdf:  ")
unlocked_file = input("enter the name of the unlocked file:  ") 


# read locked pdf
reader = PdfReader(locked_file)
if reader.is_encrypted:
    reader.decrypt(password)

# create new pdf
writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)

# save pdf without password
with open(unlocked_file, 'wb') as output_pdf:
    writer.write(output_pdf)

print(f"the pdf has been un locked")
