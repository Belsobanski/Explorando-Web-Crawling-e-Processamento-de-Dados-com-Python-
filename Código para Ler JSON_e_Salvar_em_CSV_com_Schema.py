import json
import pandas as pd

# Carregando os dados do arquivo JSON
with open("noticias_cnn.json", "r", encoding="utf-8") as json_file:
    news_data = json.load(json_file)

# Verificando os dados e organizando em um formato adequado
# Se os dados já estiverem estruturados como dicionários com as chaves corretas
# (Título, Data de Publicação, Link), podemos diretamente criar o DataFrame.

# Criando um DataFrame a partir dos dados JSON, com as colunas específicas
df = pd.DataFrame(news_data)

# Se necessário, você pode renomear as colunas
df.columns = ['Título', 'Data de Publicação', 'Link']

# Exibindo o schema do DataFrame para garantir a estrutura
print("Schema do DataFrame:")
print(df.dtypes)

# Salvando o DataFrame em um arquivo CSV com as colunas separadas
df.to_csv("noticias_cnn_separadas.csv", index=False, encoding="utf-8")

print("Dados salvos com sucesso no arquivo 'noticias_cnn_separadas.csv'.")
