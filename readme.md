# Inteligência Competitiva e a Voz do Consumidor: um framework baseado em modelos de língua para extração de aspectos de reclamações


Neste projeto foi realizada uma investigação acerca do desempenho das Largue Language Models (LLMs) em comparação a modelos já consolidados na área de Processamento de Linguagem Natural (PLN), como o Support Vector Machine (SVM) e o modelo BERT-Multilíngue (M-BERT), na tarefa de extração de aspectos e da respectiva categoria em datasets contendo reclamações de consumidores retiradas de plataformas online.

O trabalho foi organizado da seguinte forma:

Fase 1: Contendo a comparação entre os modelos de linguagem Gemma3:27b, LLama 3.1 70B Instruct, NVIDIA Nemotron 3 Ultra com os métodos SVM e M-BERT na tarefa específica de extração de aspectos do dataset Restaurant-ACOS, disponibilizado por (Cai, Xia e Yu) (2021).

Fase 2: Extração e avaliação dos modelos de LLMs que obtiveram os melhores resultados na 1ª fase, o Gemma3:27b e o modelo NVIDIA Nemotron 3 Ultra, comparados aos métodos estabelecidos como baseline do projeto, SVM e M-BERT na tarefa de identificação do par aspecto-categoria do dataset MEMD-ABSA, disponibilizado por (Cai et al.) ().

Fase 3: Rotulagem de um conjunto de dados extraído da plataforma 'consumidor.gov' contendo 9992 avaliações de usuários online pela LLM com o desempenho superior quando realizada a comparação somente entre os grandes modelos de linguagem e com o desempenho mais satisfatório quando comparado com os modelos SVM e M-BERT.

Ao final, o dataset disponibilizado foi estruturado da forma a seguir:

- Primeira coluna contendo as reclamações originais retiradas da plataforma online.

- Segunda coluna contendo os alvos que continham os principais focos das reclamações.

- Última coluna com todos os pares aspecto-categoria encontrados pelo modelo Gemma3:27b por alvo identificado. 

Datasets Utilizados:

Restaurant-ACOS:

Repositório oficial: https://github.com/NUSTM/ACOS
Link: https://doi.org/10.18653/v1/2021.acl-long.29

MEMD-ABSA:

Repositório oficial: https://github.com/NUSTM/MEMD-ABSA
Link: https://doi.org/10.48550/arXiv.2306.16956


