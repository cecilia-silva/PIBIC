import re
import nltk
import json



def processamento(frase,termo_aspecto):

    
    frase_tratada = re.sub(r'([.,!?()])', r' \1 ', frase)

    
    tokens_frase = frase_tratada.lower().split()
    tokens_aspecto = termo_aspecto.lower().split()

    
    tags = ["O"] * len(tokens_frase)

    
    if termo_aspecto.lower() == "implicit":
        return tokens_frase, tags

    tamanho_aspecto = len(tokens_aspecto)

    for i in range(len(tokens_frase) - tamanho_aspecto + 1):

        if tokens_frase[i : i + tamanho_aspecto] == tokens_aspecto:

           
            tags[i] = "B-ASP"

            for j in range(1, tamanho_aspecto):
                tags[i + j] = "I-ASP"

            break

    return tokens_frase, tags




with open('/home/cecilia/Documentos/Extração-ABSA/Experimentos---ABSA/dados_principais/test_novo.json', 'r', encoding='utf-8') as f:
    dados_originais = json.load(f)


lista_dados = []


for item in dados_originais:

    
    termo_bruto = str(item['target']).split('|')[0].strip()

    tokens, labels = processamento(item['input'], termo_bruto)

    novo_exemplo = {
        "tokens": tokens,
        "tags": labels,
        "aspect_term_completo": item['target']
    }

    lista_dados.append(novo_exemplo)


with open('test_bio_processado.json', 'w', encoding='utf-8') as f:
    json.dump(lista_dados, f, indent=4, ensure_ascii=False)