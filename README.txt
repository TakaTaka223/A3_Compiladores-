MyLang (ANTLR4 - Python target)
=================================

Conteúdo do pacote:
- MyLang.g4           : gramática ANTLR v4
- main.py             : executável principal (usa o parser gerado)
- typechecker.py      : visitor que faz checagem de tipos básica
- exemplo.mylang      : programa de exemplo
- requirements.txt    : dependências Python

Passos para usar (Linux/macOS/Windows com terminal):
1) Baixe o jar do ANTLR (ex: antlr-4.11.1-complete.jar) em https://www.antlr.org/download.html
   e coloque em uma pasta, por exemplo /home/usuario/antlr/antlr-4.11.1-complete.jar

2) Gere o parser Python a partir da gramática:
   No terminal, posicione-se na pasta onde está esse README e rode:
   java -jar /path/to/antlr-4.11.1-complete.jar -Dlanguage=Python3 MyLang.g4

   Isso vai gerar arquivos: MyLangLexer.py, MyLangParser.py, MyLangListener.py, MyLangVisitor.py
   (e possivelmente outros).

3) Instale a runtime Python do ANTLR:
   pip install -r requirements.txt

4) Rode o analisador e type checker:
   python main.py exemplo.mylang

   Saída esperada: a árvore de parse (em forma textual) e a checagem de tipos.
   Se não houver erros, verá \"Type checking: OK (sem erros)\".

Notas e dicas:
- A checagem de tipos é básica e não implementa escopo de bloco (todas as variáveis ficam em um único símbolo).
- Se quiser gerar uma imagem da parse tree, use a ferramenta gráfica do ANTLR (GUI) ou exporte a tree em alguma ferramenta que suporte.
- Para estender a linguagem: adicione operadores lógicos (&&, ||), implemente escopo com push/pop de tabelas, adicione funções, etc.
