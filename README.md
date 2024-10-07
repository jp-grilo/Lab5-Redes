# Lab5-Redes

## Servidor Web Simples em Python

Nesta tarefa, você desenvolverá um servidor Web simples em Python, capaz de
processar apenas uma requisição. Seu servidor Web (i) criará um socket de conexão
quando contatado por um cliente (navegador); (ii) receberá a requisição HTTP dessa
conexão; (iii) analisará a requisição para determinar o arquivo específico sendo
requisitado; (iv) obterá o arquivo requisitado do sistema de arquivo do servidor; (v) criará
uma mensagem de resposta HTTP consistindo no arquivo requisitado precedido por
linhas de cabeçalho; e (vi) enviará a resposta pela conexão TCP ao navegador
requisitante. Se um navegador requisitar um arquivo que não está presente no seu
servidor, seu servidor deverá retornar uma mensagem de erro “404 Not Found”.
Você pode procurar por códigos similares (especialmente no GitHub) para apoiar o seu
desenvolvimento. Sua tarefa é rodar seu servidor e depois testá-lo enviando requisições
de navegadores rodando em hospedeiros diferentes. Se você rodar seu servidor em um
hospedeiro que já tem um servidor Web rodando nele, então deverá usar uma porta
diferente da porta 80 para o seu servidor.
O relatório que será submetido deve conter a descrição das atividades, screenshots das
telas do código rodando, e outras informações que achar relevante para demonstrar a
conclusão do laboratório

## Estrutura do Projeto

- `server.py`: Código do servidor web.
- `NomdeDoArquivo.html`: Arquivos em HTML que serão retornados com a requisição.

## Como Executar


1. Coloque os arquivos `server.py` e `NomeDoArquivo.html` no mesmo diretório.
2. Abra um terminal no diretório onde os arquivos estão localizados.
3. Execute o comando:

   ```sh
   python server.py

4. Em um navegador qualquer, procure por:

  ```sh
  http://localhost:8080/NomeDoArquivo.html

