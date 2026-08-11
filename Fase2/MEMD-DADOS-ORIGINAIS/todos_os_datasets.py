import json
import pandas as pd
with open('/home/cecilia/Documentos/PIBIC/Fase2/MEMD-DADOS-ORIGINAIS/Restaurant/Dev.json', 'r', encoding='utf-8') as arquivo:
    dev = json.load(arquivo)


with open('/home/cecilia/Documentos/PIBIC/Fase2/MEMD-DADOS-ORIGINAIS/Restaurant/Test.json', 'r', encoding='utf-8') as arquivo:
    test = json.load(arquivo)


with open('/home/cecilia/Documentos/PIBIC/Fase2/MEMD-DADOS-ORIGINAIS/Restaurant/Train.json', 'r', encoding='utf-8') as arquivo:
    train = json.load(arquivo)

df1= pd.DataFrame(dev)

df2 = pd.DataFrame(test)


df3 = pd.DataFrame(train)
resultado_books = pd.concat([df1,df2,df3])

resultado_books.to_csv('Dataset_Restaurant.csv', index=False)

df_rest = pd.read_csv('/home/cecilia/Documentos/PIBIC/Fase2/MEMD-DADOS-ORIGINAIS/Dataset_Restaurant.csv')
df_books = pd.read_csv('/home/cecilia/Documentos/PIBIC/Fase2/MEMD-DADOS-ORIGINAIS/Dataset_Books.csv')
df_cloth = pd.read_csv('/home/cecilia/Documentos/PIBIC/Fase2/MEMD-DADOS-ORIGINAIS/Dataset_Clothing.csv')
df_hotel = pd.read_csv('/home/cecilia/Documentos/PIBIC/Fase2/MEMD-DADOS-ORIGINAIS/Dataset_Hotel.csv')
df_lap = pd.read_csv('/home/cecilia/Documentos/PIBIC/Fase2/MEMD-DADOS-ORIGINAIS/Dataset_Laptop.csv')




dataset_completo = pd.concat([df_books,df_cloth,df_hotel,df_lap,df_rest])
df_memd = dataset_completo.reset_index(drop=True)


df_memd.to_csv('dataset_Memd(1).csv')

