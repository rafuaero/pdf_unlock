from PyPDF2 import PdfReader, PdfWriter

# Caminho para o PDF bloqueado
arquivo_bloqueado = '2025-01-15_Fatura_Rafael Ferreira Costacurta_287569_BTG.pdf'

# Caminho para salvar o PDF desbloqueado
arquivo_desbloqueado = "fatura_jan25.pdf"

# Senha do PDF
senha = '68999801187'

# Ler o PDF protegido
reader = PdfReader(arquivo_bloqueado)
if reader.is_encrypted:
    reader.decrypt(senha)

# Criar um novo PDF sem senha
writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)

# Salvar o novo PDF sem senha
with open(arquivo_desbloqueado, 'wb') as output_pdf:
    writer.write(output_pdf)

print(f"O arquivo {arquivo_desbloqueado} foi criado sem senha.")
