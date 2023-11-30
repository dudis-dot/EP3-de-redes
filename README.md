# EP3-de-redes
# Preparando um ambiente
Para rodar os exemplos é preciso ter o python, pip e o venv instalados no computador, depois crie uma pasta chamada venv em uma das pastas spotipy.
Em seguinda, rode o comando (dentro da pasta do spotipy que você colocou a pasta venv):
  $ python -m venv venv

Depois, execute o comando:
  $ pip install -r requirements.txt

Agora, crie um arquivo chamado .env e coloque o seguinte contéudo:
  SPOTIPY_CLIENT_ID = <seu_id_do_spotify>
  SPOTIPY_CLIENT_SECRET = <sua_senha_spotipy>
  **Obs:** pra conseguir esses valores siga esse tutorial: https://www.youtube.com/watch?v=yxSKrVXeKcI&list=PLqgOPibB_QnzzcaOFYmY2cQjs35y0is9N&index=2

Agora, repita o procedimento acima na outra pasta spotipy. Pronto você já esta com seu ambiente configurado.

# Rodando os exemplos
Para rodar os exemplos poc.py é necessário abrir dois terminais, um dentro da pasta spotipy-2.22 e outro na pasta spotipy-2.23.
Em seguida, rode o abaixo nos dois terminais:
  $ source venv/bin/activate

E depois,execute os arquivos poc.py.

Para desativar o ambiente virtual, execute:
  $ deactivate
