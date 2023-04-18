from PyPDF2 import PdfWriter, PdfReader
from getpass import getpass

writer = PdfWriter()
reader = PdfReader('Python_для_школьников.pdf')

for page in range(reader.numPages):
    writer.add_page(reader.pages[page])

password = getpass(prompt='Введите пароль: ')
writer.encrypt(password)

with open('Python_для_школьников_protected.pdf', 'wb') as file:
    writer.write(file)
