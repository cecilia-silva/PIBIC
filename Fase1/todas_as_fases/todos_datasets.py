import pandas as pd
import os

arquivos_entrada = {
    'train': '/home/cecilia/Documentos/extracao_absa/ACOS/data/Restaurant-ACOS/rest16_quad_train.tsv',
    'val': '/home/cecilia/Documentos/extracao_absa/ACOS/data/Restaurant-ACOS/rest16_quad_dev.tsv',
    'test': '/home/cecilia/Documentos/extracao_absa/ACOS/data/Restaurant-ACOS/rest16_quad_test.tsv'
}

arquivo_saida = "dataset_acos_concatenado.tsv" 

colunas = ['sentence', 'aspect', 'category', 'opinion', 'sentiment']


def processar_datasets():
    lista_dfs = []
    print("Iniciando a leitura dos ficheiros...")

    for split, nome_arquivo in arquivos_entrada.items():
        if os.path.exists(nome_arquivo):
            try:
                df = pd.read_csv(
                    nome_arquivo, 
                    sep='\t', 
                    header=None, 
                    names=colunas, 
                    on_bad_lines='skip', 
                    quoting=3,
                    engine='python' 
                )
                df['split_origem'] = split
                lista_dfs.append(df)
                print(f"{nome_arquivo} carregado: {len(df)} linhas.")
            except Exception as e:
                print(f" Erro inesperado ao ler {nome_arquivo}: {e}")
        else:
            print(f"✖ Erro: O ficheiro {nome_arquivo} não foi encontrado.")

    if lista_dfs:
        df_total = pd.concat(lista_dfs, ignore_index=True)
        # Salvando em TSV padrão
        df_total.drop(columns=['split_origem']).to_csv(
            arquivo_saida, sep='\t', index=False, header=None, encoding='utf-8'
        )
        
        print(f"Ficheiro guardado em: {os.path.abspath(arquivo_saida)}")

if __name__ == "__main__":
    processar_datasets()