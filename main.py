from PyPDF2 import PdfFileWriter, PdfFileReader
import os
from pathlib import Path

directoryFiles = "\\\\192.168.254.108\\Desenvolvimento\\Luca\\RPAs\\DocsSeguros\\"
allDocuments = []

# for para adicionar os arquivos dentro de um array

for file in os.listdir(directoryFiles):
    if ".pdf" in file:
        allDocuments.append(file)

# for para executar a ação em todos os documentos do array

for item in allDocuments:

    PDF = directoryFiles + item
    # pegando o nome do arquivo sem extensão
    fileName = os.path.splitext(item)[0]
    newFolder = (directoryFiles + fileName)

    if not os.path.exists(newFolder):  # verificando se a pasta já existe
        os.mkdir(newFolder)

    inputpdf = PdfFileReader(open(PDF, "rb"))  # abertura do pdf para leitura

    for i in range(inputpdf.numPages):  # for em cada pagina do pdf
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))

        # essa parte assumo n ter entendido mt bem kkkkk gerando um
        # novo arquivo de acordo com os parametros de nome passado e inserindo os dados da pagina lida

        with open(newFolder + "/" + str(i) + ".pdf", "wb") as outputStream:
            output.write(outputStream)  #escrevendo no arquivo gerado