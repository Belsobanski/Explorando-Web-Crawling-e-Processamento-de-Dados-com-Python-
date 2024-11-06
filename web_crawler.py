import requests
from bs4 import BeautifulSoup

# URL do site que queremos "crawlear"
url = "https://edition.cnn.com/politics"  # Coloque a URL que deseja acessar

# Fazendo a requisição para o site
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Criando o objeto BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrando os títulos das notícias (alterar conforme o site)
    # Aqui, estou usando uma estrutura de exemplo; ajustar o seletor ao site que está sendo "crawleado"
    headlines = soup.find_all('h3')  # Seleciona todos os elementos <h3>
    
    print("Títulos das notícias encontradas:")
    for index, headline in enumerate(headlines, start=1):
        print(f"{index}. {headline.get_text().strip()}")
else:
    print(f"Erro ao acessar o site: Status {response.status_code}")
