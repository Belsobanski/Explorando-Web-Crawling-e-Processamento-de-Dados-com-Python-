import json
import pandas as pd

# Carregando os dados do arquivo JSON
with open("noticias_cnn.json", "r", encoding="utf-8") as json_file:
    news_data = json.load(json_file)

# Criando o DataFrame a partir dos dados JSON
df = pd.DataFrame(news_data)

# Definindo o Schema manualmente (opcional)
# Isso garante que as colunas são 'Título', 'Data de Publicação' e 'Link'
df.columns = ['Título', 'Data de Publicação', 'Link']

# Exibindo o Schema do DataFrame (tipos das colunas)
print("Schema do DataFrame:")
print(df.dtypes)

# Exibindo o DataFrame para verificar os dados
print("\nDataFrame:")
print(df)

# Salvando o DataFrame em um arquivo CSV
df.to_csv("noticias_cnn_separadas.csv", index=False, encoding="utf-8")

print("\nDados salvos com sucesso no arquivo 'noticias_cnn_separadas.csv'.")
