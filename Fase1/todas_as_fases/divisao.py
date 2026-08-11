from sklearn.model_selection import train_test_split
import json


with open('/home/cecilia/Documentos/Extração-ABSA/Experimentos---ABSA/dados_principais/dados_ajustados.json', 'r', encoding='utf-8') as arquivo:
        dados_divisao = json.load(arquivo)
        
        
resto, teste = train_test_split(dados_divisao, test_size=0.1, random_state=42)
treino, validacao = train_test_split(resto, test_size=0.11, random_state=42)





with open('train_novo.json', 'w', encoding='utf-8') as f:
    json.dump(treino, f, indent=4, ensure_ascii=False)

with open('val_novo.json', 'w', encoding='utf-8') as f:
    json.dump(validacao, f, indent=4, ensure_ascii=False)

with open('test_novo.json', 'w', encoding='utf-8') as f:
    json.dump(teste, f, indent=4, ensure_ascii=False)