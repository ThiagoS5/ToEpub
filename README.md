# 📖 Conversor PDF para EPUB: Sua Biblioteca Digital, Simplificada

![Banner da Aplicação](https://dummyimage.com/1200x600/343a40/ffffff.png&text=Conversor+PDF+para+EPUB)

> Transforme seus documentos PDF em eBooks no formato EPUB com um único comando. Perfeito para organizar sua biblioteca e ler no Kindle ou em outros e-readers.

---

## 🚀 Sobre o Projeto

O **Conversor PDF para EPUB** é um script de linha de comando em Python, criado para automatizar e simplificar a conversão de múltiplos arquivos PDF para o formato EPUB.

O projeto foi desenvolvido com foco na geração de um arquivo final de alta qualidade, priorizando uma estrutura de navegação que melhora a experiência de leitura em dispositivos como o Kindle.

## ✨ Principais Funcionalidades

- **🔄 &nbsp; Conversão em Lote:** Converte todos os arquivos PDF encontrados em uma pasta de uma só vez.
- **📚 &nbsp; Navegação Otimizada:** Cada página do PDF é convertida em um capítulo individual no EPUB, facilitando a navegação pelo sumário do e-reader.
- **📂 &nbsp; Pastas Flexíveis:** Permite ao usuário especificar pastas de origem e destino, oferecendo total controle sobre a organização dos arquivos.
- **⚙️ &nbsp; Simplicidade de Uso:** Executado através de uma interface de linha de comando simples e direta.

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído com um conjunto de bibliotecas Python robustas e eficientes.

- **Linguagem:** [Python](https://www.python.org/) (v3.x)
- **Bibliotecas Principais:**
  - **Leitura de PDF:** [PyMuPDF](https://pymupdf.readthedocs.io/)
  - **Criação de EPUB:** [ebooklib](https://github.com/aerkalov/ebooklib)
  - **Interface de Comando:** [argparse](https://docs.python.org/3/library/argparse.html) (Biblioteca padrão do Python)

## 📂 Estrutura do Projeto

A arquitetura do projeto é simples e direta, focada na funcionalidade principal.

```
c:/Dev/ToEpub/
├───conversor.py        # O script principal de conversão
└───requirements.txt    # As dependências do projeto
```

## 🏁 Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e executar o script em seu ambiente de desenvolvimento.

1.  **Clone o repositório (ou baixe os arquivos):**
    Se você tiver Git, pode clonar. Caso contrário, apenas certifique-se de que `conversor.py` e `requirements.txt` estejam na mesma pasta.

2.  **Crie e ative um ambiente virtual (Recomendado):**
    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    Com o ambiente virtual ativado, instale as bibliotecas necessárias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o conversor:**
    Agora você pode usar o script. Aqui estão alguns exemplos:

    *   **Converter PDFs na pasta atual:**
        ```bash
        python conversor.py
        ```
    *   **Converter PDFs de uma pasta específica:**
        ```bash
        python conversor.py "C:\Caminho\Para\Seus\PDFs"
        ```
    *   **Especificar origem e destino:**
        ```bash
        python conversor.py "C:\Caminho\PDFs" --destino "C:\Caminho\EPUBs"
        ```

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usar e modificar como desejar.
