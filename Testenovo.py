import os
import shutil
import pdfplumber
import re

# Função para identificar o modelo do PDF
def identificar_modelo_pdf(pdf_path):
    # Função para ler o conteúdo do PDF com pdfplumber
    texto = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            texto += page.extract_text()

    # Exemplo: Identificando o modelo com base em uma palavra-chave
    if re.search(r'PONTOMAIS', texto):
        return 'modelo_1'
    elif re.search(r'CATHO', texto):
        return 'modelo_2'
    elif re.search(r'APLICAR', texto):
        return 'modelo_3'
    elif re.search(r'PLUXEE', texto):
        return 'modelo_4'
    elif re.search(r'FLASH', texto):
        return 'modelo_5'
    else:
        return 'modelo_desconhecido'

# Função para mover o arquivo para a pasta correta
def mover_arquivo(pdf_path, destino):
    try:
        if not os.path.exists(destino):
            os.makedirs(destino)
        shutil.move(pdf_path, destino)
        print(f"Arquivo movido para: {destino}")
    except Exception as e:
        print(f"Erro ao mover o arquivo {pdf_path}: {e}")

# Função principal para processar a pasta
def processar_pasta_pdfs(pasta_origem, pasta_destino_modelo1, pasta_destino_modelo2 , pasta_destino_modelo3 , pasta_destino_modelo4 , pasta_destino_modelo5):
    for arquivo in os.listdir(pasta_origem):
        if arquivo.endswith(".pdf"):
            caminho_pdf = os.path.join(pasta_origem, arquivo)
            modelo = identificar_modelo_pdf(caminho_pdf)

            if modelo == 'modelo_1':
                mover_arquivo(caminho_pdf, pasta_destino_modelo1)
            elif modelo == 'modelo_2':
                mover_arquivo(caminho_pdf, pasta_destino_modelo2)
            elif modelo == 'modelo_3':
                mover_arquivo(caminho_pdf, pasta_destino_modelo3)
            elif modelo == 'modelo_4':
                mover_arquivo(caminho_pdf, pasta_destino_modelo4)
            elif modelo == 'modelo_5':
                mover_arquivo(caminho_pdf, pasta_destino_modelo5)
            else:
                print(f"Modelo desconhecido para o arquivo: {arquivo}")

# Definir os caminhos das pastas
pasta_origem = "Z:\\INFORMATICA\\Testes Notas"
pasta_destino_modelo1 = "Z:\\INFORMATICA\\Testes Notas\\PONTOMAIS"
pasta_destino_modelo2 = "Z:\\INFORMATICA\\Testes Notas\\CATHO"
pasta_destino_modelo3 = "Z:\\INFORMATICA\\Testes Notas\\APLICAR"
pasta_destino_modelo4 = "Z:\\INFORMATICA\\Testes Notas\\PLUXEE"
pasta_destino_modelo5 = "Z:\INFORMATICA\Testes Notas\\FLASH"

# Chamar a função para processar a pasta de PDFs
processar_pasta_pdfs(pasta_origem, pasta_destino_modelo1, pasta_destino_modelo2 , pasta_destino_modelo3 , pasta_destino_modelo4 , pasta_destino_modelo5)

