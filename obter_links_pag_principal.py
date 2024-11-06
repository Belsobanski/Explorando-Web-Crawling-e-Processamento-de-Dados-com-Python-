import requests
from bs4 import BeautifulSoup
import csv

# URL do site que queremos coletar dados
url = "https://www.cnn.com/"

# Fazendo a requisição HTTP para o site
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Lista para armazenar dados de cada notícia
    news_data = []
    
    # Coletando dados de cada artigo (ajuste conforme a estrutura do site)
    articles = soup.find_all('article')  # Encontrar todos os elementos de artigo

    print("Informações das notícias:")
    for article in articles:
        # Título
        title = article.find('h3').get_text().strip() if article.find('h3') else 'Título não encontrado'
        
        # Link para o artigo
        link = article.find('a')['href'] if article.find('a') else 'Link não encontrado'
        if not link.startswith('http'):  # Ajusta links relativos
            link = "https://www.cnn.com" + link
        
        # Data de publicação
        date = article.find('time')['datetime'] if article.find('time') else 'Data não encontrada'
        
        # Imprimindo os dados
        print(f"Título: {title}\nLink: {link}\nData: {date}\n")
        
        # Adicionando os dados à lista
        news_data.append([title, link, date])
    
    # Salvando os dados em um arquivo CSV
    with open('noticias.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Título", "Link", "Data"])  # Cabeçalhos
        writer.writerows(news_data)  # Dados

    print("Os dados foram salvos em 'noticias.csv'.")

else:
    print(f"Erro ao acessar o site: Status {response.status_code}")
