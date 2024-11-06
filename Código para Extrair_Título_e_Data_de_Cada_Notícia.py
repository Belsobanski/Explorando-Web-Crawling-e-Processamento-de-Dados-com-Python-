import requests
from bs4 import BeautifulSoup

# URL do site que queremos coletar dados
url = "https://www.cnn.com/"

# Fazendo a requisição HTTP para o site
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Lista para armazenar links das notícias
    news_links = []
    
    # Encontrando todos os links de artigos
    articles = soup.find_all('a', href=True)  # Captura todos os links na página
    
    # Filtrando links de notícias
    for article in articles:
        link = article['href']
        
        # Filtra apenas links de notícias do ano atual
        if link.startswith("/2024") or link.startswith("https://www.cnn.com/2024"):
            full_link = "https://www.cnn.com" + link if link.startswith("/") else link
            news_links.append(full_link)
    
    # Iterar sobre cada link de notícia para extrair título e data
    print("Título e data das notícias:")
    for link in news_links:
        article_response = requests.get(link)
        
        if article_response.status_code == 200:
            article_soup = BeautifulSoup(article_response.content, 'html.parser')
            
            # Tentando capturar o título da notícia
            title = article_soup.find('h1').get_text(strip=True) if article_soup.find('h1') else "Título não encontrado"
            
            # Tentando capturar a data de publicação da notícia
            date_element = article_soup.find('meta', attrs={'name': 'pubdate'}) or article_soup.find('meta', attrs={'property': 'article:published_time'})
            date = date_element['content'][:10] if date_element and 'content' in date_element.attrs else "Data não encontrada"
            
            # Imprimindo o título e a data
            print(f"\nTítulo: {title}")
            print(f"Data de Publicação: {date}")
            print(f"Link: {link}")

else:
    print(f"Erro ao acessar o site: Status {response.status_code}")
