# Inteligência Competitiva e a Voz do Consumidor: um framework baseado em modelos de língua para extração de aspectos de reclamações

Neste projeto foi realizada uma investigação acerca do desempenho das Large Language Models (LLMs) em comparação a modelos já consolidados na área de Processamento de Linguagem Natural (PLN), como o Support Vector Machine (SVM) e o modelo BERT-Multilíngue (M-BERT), na tarefa de extração de aspectos e da respectiva categoria em datasets contendo reclamações de consumidores retiradas de plataformas online.

O trabalho foi organizado da seguinte forma:

Fase 1: Contendo a comparação entre os modelos de linguagem Gemma3:27b, LLama 3.1 70B Instruct, NVIDIA Nemotron 3 Ultra com os métodos SVM e M-BERT na tarefa específica de extração de aspectos do dataset Restaurant-ACOS, disponibilizado por (Cai, Xia e Yu) (2021).

Fase 2: Extração e avaliação dos modelos de LLMs que obtiveram os melhores resultados na 1ª fase, o Gemma3:27b e o modelo NVIDIA Nemotron 3 Ultra, comparados aos métodos estabelecidos como baseline do projeto, SVM e M-BERT na tarefa de identificação do par aspecto-categoria do dataset MEMD-ABSA, disponibilizado por (Cai et al.) (2023).

Fase 3: Rotulagem de um conjunto de dados extraído da plataforma 'consumidor.gov' contendo avaliações de usuários online pela LLM com o desempenho superior quando realizada a comparação somente entre os grandes modelos de linguagem e com o desempenho mais satisfatório quando comparado com os modelos SVM e M-BERT.

Fase 4: Aplicação da técnica de destilação de conhecimento (knowledge distillation) na abordagem teacher-student, com o objetivo de transferir a capacidade de extração de um modelo de linguagem de grande porte para um modelo consideravelmente menor. Nesta fase, o modelo Qwen2.5-72B-Instruct atuou como professor, sendo responsável pela nova rotulagem do conjunto de dados, gerando os pseudo-rótulos utilizados no treinamento. O modelo Qwen2.5-7B-Instruct atuou como aluno, sendo ajustado por fine-tuning supervisionado (Low-Rank Adaptation (LoRA)) a partir das saídas geradas pelo professor, seguindo os conceitos da técnica Sequence-Level Knowledge Distillation (Kim e Rush, 2016). O desempenho do aluno foi avaliado em um conjunto de teste reservado, antes e depois do fine-tuning, utilizando as métricas de precisão, revocação, F1-score e acurácia, permitindo mensurar o ganho obtido exclusivamente pelo ajuste dos pesos do modelo.


Ao final, o dataset disponibilizado foi estruturado da forma a seguir:

- Primeira coluna contendo as reclamações originais retiradas da plataforma online.

- Segunda coluna contendo os alvos que continham os principais focos das reclamações.

- Última coluna com todos os pares aspecto-categoria encontrados pelo modelo Gemma3:27b por alvo identificado.

Em relação a fase 4: O modelo aluno apresentou melhora em todas as métricas após o fine-tuning: a precisão passou de 1,3% para 5,5%, a revocação de 0,8% para 5,7%, o F1-score de 1,0% para 5,6% e a acurácia de 0,5% para 2,9%. Dessa forma, foi identificado que o treinamento com o padrão de extração do modelo professor proporcionou um ganho expressivo na capacidade do modelo aluno em identificar os alvos e os pares contendo aspecto e categoria em cenários de grande volume de textos opinativos.

Datasets Utilizados:

Restaurant-ACOS:

Repositório oficial: https://github.com/NUSTM/ACOS Link: https://doi.org/10.18653/v1/2021.acl-long.29

MEMD-ABSA:

Repositório oficial: https://github.com/NUSTM/MEMD-ABSA Link: https://doi.org/10.48550/arXiv.2306.16956

Técnica de fine-tuning utilizada:
Kim, Y., & Rush, A. M. (2016). Sequence-Level Knowledge Distillation. Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing (EMNLP), 1317–1327. https://doi.org/10.18653/v1/D16-1139


