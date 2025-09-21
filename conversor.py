import fitz 
from ebooklib import epub
import os 
import argparse

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def converter_pdf_para_epub(caminho_pdf, pasta_de_destino):
    nome_base = os.path.splitext(os.path.basename(caminho_pdf))[0]
    caminho_epub = os.path.join(pasta_de_destino, f"{nome_base}.epub")

    print(f"-------------------------------------------------")
    print(f"Convertendo '{caminho_pdf}'...")

    try:
        doc = fitz.open(caminho_pdf)
    except Exception as e:
        print(f"Erro ao abrir o PDF: {e}")
        return

    book = epub.EpubBook()
    book.set_identifier(f"id_{nome_base}")
    book.set_title(nome_base)
    book.set_language("pt-br")
    book.add_author("Conversor Python em Lote")

    capitulos = []
    for i, page in enumerate(doc):
        texto_pagina = page.get_text("xhtml")
        titulo_capitulo = f"Página {i + 1}"
        nome_arquivo_capitulo = f"capitulo_{i + 1}.xhtml"
        
        capitulo = epub.EpubHtml(
            title=titulo_capitulo,
            file_name=nome_arquivo_capitulo,
            lang="pt-br"
        )
        capitulo.content = f"<h1>{titulo_capitulo}</h1>{texto_pagina}".encode("utf-8")
        book.add_item(capitulo)
        capitulos.append(capitulo)

    doc.close() 
    
    book.toc = [epub.Link(c.file_name, c.title, c.file_name.split('.')[0]) for c in capitulos]
    book.spine = ["nav"] + capitulos
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    try:
        epub.write_epub(caminho_epub, book, {{}})
        print(f"SUCESSO! O arquivo foi salvo em '{caminho_epub}'")
    except Exception as e:
        print(f"Erro ao salvar o EPUB: {e}")

def converter_todos_os_pdfs_na_pasta(pasta_origem, pasta_destino):
    if not os.path.isdir(pasta_origem):
        print(f"Erro: A pasta de origem '{pasta_origem}' não existe ou não é um diretório.")
        return

    arquivos_pdf = [f for f in os.listdir(pasta_origem) if f.lower().endswith(".pdf")]
    if not arquivos_pdf:
        print(f"Nenhum arquivo PDF foi encontrado na pasta '{pasta_origem}'.")
        return
    os.makedirs(pasta_destino, exist_ok=True)
    print(f"Pasta de origem: '{os.path.abspath(pasta_origem)}'")
    print(f"Todos os ePubs serão salvos na pasta: '{os.path.abspath(pasta_destino)}'\n")
    
    for nome_arquivo in arquivos_pdf:
        caminho_completo_pdf = os.path.join(pasta_origem, nome_arquivo)
        converter_pdf_para_epub(caminho_completo_pdf, pasta_destino)
    
    print(f"\nConversão em lote concluída! {len(arquivos_pdf)} arquivos processados.")

def main():
    limpar_tela()
    
    parser = argparse.ArgumentParser(
        description="Converte arquivos PDF para EPUB em lote.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "pasta_origem",
        nargs="?",
        default=".",
        help="Pasta onde os arquivos PDF estão localizados. Padrão: pasta atual."
    )
    parser.add_argument(
        "--destino",
        default=None,
        help="Pasta onde os EPUBs convertidos serão salvos.\nPadrão: uma pasta chamada 'EPUBS_Convertidos' dentro da pasta de origem."
    )
    
    args = parser.parse_args()
    
    pasta_origem = args.pasta_origem
    pasta_destino = args.destino
    
    if pasta_destino is None:
        pasta_destino = os.path.join(pasta_origem, "EPUBS_Convertidos")
        
    converter_todos_os_pdfs_na_pasta(pasta_origem, pasta_destino)

if __name__ == "__main__":
    main()