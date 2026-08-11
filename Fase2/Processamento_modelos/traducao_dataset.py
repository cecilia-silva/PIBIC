
import ast
import pandas as pd 
from sklearn.model_selection import train_test_split
import json

df = pd.read_csv('/home/cecilia/Documentos/PIBIC/Fase2/MEMD-DADOS-ORIGINAIS/dataset_Memd (1).csv')



def traducao(linha):
    aspect_term = []
    categories = []
    for quadruplo in ast.literal_eval(linha['quadruples']):
        
        aspecto = quadruplo['aspect']
        categoria = quadruplo['category']
        
        if aspecto['from'] == -1:
            aspecto = 'NULL'
            aspect_term.append(aspecto)
        
        else:
            aspect_term.append(" ".join(linha['raw_words'].split()[aspecto['from']:aspecto['to']]))

            
        
        categories.append(categoria)
            
       
    return aspect_term, categories


resultado = df.apply(traducao, axis=1)
print(resultado[0])


rotulos_completos = resultado.apply(lambda x: [f"{aspecto}|{categoria}" for aspecto,categoria in zip (x[0],x[1])])

df_ajustado = pd.DataFrame({
    'sentence': df['raw_words'],
    'rotulos': rotulos_completos   
 

})

df_ajustado.to_json('dataset_traduzido.json', orient='records', force_ascii=False, indent=2)
df_final = df_ajustado.to_dict('records')




resto, teste = train_test_split(df_final, test_size=0.1, random_state=42)
treino, validacao = train_test_split(resto, test_size=0.11, random_state=42)



with open('train.json', 'w', encoding='utf-8') as f:
    json.dump(treino, f, indent=4, ensure_ascii=False)

with open('val.json', 'w', encoding='utf-8') as f:
    json.dump(validacao, f, indent=4, ensure_ascii=False)

with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(teste, f, indent=4, ensure_ascii=False)
    
    
    
    
    
    