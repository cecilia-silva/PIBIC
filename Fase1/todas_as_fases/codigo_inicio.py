import pandas as pd
import json







with open('/home/cecilia/Documentos/extracao_absa/dataset_acos_concatenado.tsv', 'r', encoding='utf-8') as f: 
   dados_processados = []
   for linha in f:
       proxima_frase = linha.strip('\n') 
       frases_divididas = proxima_frase.split('\t') 
       
       sentencas = frases_divididas[0] 
       tokens = sentencas.split()
       quadruplos = frases_divididas[1:] 
       
       lista_temporaria_quadruplos = [] 
   
       
       
       
       
   
       for quadruplo in quadruplos: 
           partes = quadruplo.split() 
           
           if len(partes) < 4: 
               continue
           
           
           indices_aspecto = partes[0]
           categoria = partes[1]
           sentimento = partes[2]
           indices_opiniao = partes[3]
          
           if indices_aspecto == '-1,-1': 
               palavra_aspecto = 'implicit'
               
           else: 
               indices_formatados = (indices_aspecto.split(',')) 
               indice_1 = int(indices_formatados[0])
               indice_2 = int(indices_formatados[1]) 
               palavra_aspecto = " ".join(tokens[indice_1 : indice_2]) 

           
           
           
           if indices_opiniao == '-1,-1':
               palavra_opiniao = 'implicit'
               
           else:
               indice_opiniao_novo = indices_opiniao.split(',')
               indice_opiniao_1 = int(indice_opiniao_novo[0])
               indice_opiniao_2 = int(indice_opiniao_novo[1])
               palavra_opiniao = " ".join(tokens[indice_opiniao_1 : indice_opiniao_2])
           
           if sentimento == '0':
               sentimento_texto = 'negativo'
           elif sentimento == '1':
               sentimento_texto = 'neutro'
           elif sentimento == '2':
               sentimento_texto = 'positivo'
           else:
               sentimento_texto = 'desconhecido'
           
                
                
           lista_rotulos = {
               'Aspect term': palavra_aspecto,
               'Aspect category': categoria,
               'Opinion term': palavra_opiniao,
               'Sentiment Polarity': sentimento_texto
           }
           
           lista_temporaria_quadruplos.append(lista_rotulos)
           
      
           dicionario_frase = {
               'frase': sentencas,
               'quadruplos': lista_temporaria_quadruplos
            }
       
    
       dados_processados.append(dicionario_frase)
           
           
           
           
           
           

           
  
with open('dados_fase1.json', 'w', encoding='utf-8') as f: #
    json.dump(dados_processados, f, indent=4, ensure_ascii=False)