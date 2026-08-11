import json



with open('/home/cecilia/Documentos/Extração-ABSA/Experimentos---ABSA/dados_principais/dados_fase1.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
dataset_final = []
for item in dados:
    
    alvos_da_frase = []
    frase_entrada = item['frase']
    
    for quadruplo in item['quadruplos']:
        a = quadruplo['Aspect term']
        b = quadruplo['Aspect category']
        c = quadruplo['Opinion term']
        d = quadruplo['Sentiment Polarity']
        
        telegramas = f"{a} | {b} | {c} | {d}"
        
        
        alvos_da_frase.append(telegramas)
        
        
        
    target_final = " [SEP] ".join(alvos_da_frase)
    
    
    par_final = {
        'input': frase_entrada,
        'target': target_final
    }
    
    dataset_final.append(par_final)
    
    
    
with open('dados_ajustados.json', 'w', encoding='utf-8') as f:
    json.dump(dataset_final, f, indent=4, ensure_ascii=False)