import requests as r
from bs4 import BeautifulSoup

try:
    ask = input("Qual site deseja pegar os dados: ")
    req = r.get(ask)
    soup = BeautifulSoup(req.content,'html.parser')
    novo = str(soup)
    arquivo = open("document.txt", "w")
    arquivo.write(novo)
    arquivo.close()

except Exception as e:
    print(e)

finally:
    doc = open("document.txt", "r")
    print(doc.read())
    print("Seção finalizada")
