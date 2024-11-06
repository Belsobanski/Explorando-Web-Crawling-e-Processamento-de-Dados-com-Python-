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
    
    # Lista para armazenar os dados das notícias
    news_data = []
    
    # Encontrando todos os links de artigos
    articles = soup.find_all('a', href=True)  # Captura todos os links na página
    
    # Filtrando links de notícias
    for article in articles:
        link = article['href']
        
        # Filtra apenas links de notícias do ano atual
        if link.startswith("/2024") or link.startswith("https://www.cnn.com/2024"):
            full_link = "https://www.cnn.com" + link if link.startswith("/") else link
            
            # Acessando cada página de notícia
            article_response = requests.get(full_link)
            
            if article_response.status_code == 200:
                article_soup = BeautifulSoup(article_response.content, 'html.parser')
                
                # Captura do título
                title = article_soup.find('h1').get_text(strip=True) if article_soup.find('h1') else "Título não encontrado"
                
                # Captura da data de publicação
                date_element = article_soup.find('meta', attrs={'name': 'pubdate'}) or article_soup.find('meta', attrs={'property': 'article:published_time'})
                date = date_element['content'][:10] if date_element and 'content' in date_element.attrs else "Data não encontrada"
                
                # Adicionando os dados da notícia à lista
                news_data.append([title, date, full_link])
    
    # Salvando os dados no arquivo CSV
    with open("noticias_cnn.csv", mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Título", "Data de Publicação", "Link"])  # Cabeçalho
        writer.writerows(news_data)
    
    print("Dados salvos com sucesso no arquivo 'noticias_cnn.csv'.")

else:
    print(f"Erro ao acessar o site: Status {response.status_code}")
