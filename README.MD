# TDN VoD Server
Este projeto serve como servidor da aplicação TDN VoD

## Requisitos
Para executar o servidor, você precisa ter os seguintes programas instalados:
* MySQL v8 + Python Connector, configurando as credenciais adequadas em `db/utils.py` e executando o script `db/tdnbay_script.sql` 
* MediaInfo
* ffmpeg (já incluído)

## Executar
Com todos os requisitos satisfeitos, basta executar o script `driver.py` para o servidor iniciar na porta 50000 por padrão.

Além do servidor socket, o servidor para miniaturas também será iniciado na porta 8000.
