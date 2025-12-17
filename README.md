# 🎬 Netflix Churn Prediction: End-to-End Pipeline

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📋 Sobre o Projeto

Este projeto consiste em uma solução completa de Machine Learning para prever o **Churn (cancelamento)** de usuários de um serviço de streaming (dados similares à Netflix).

O objetivo principal não foi apenas criar um modelo preditivo, mas construir um pipeline robusto seguindo boas práticas de **MLOps**, garantindo rastreabilidade dos experimentos e facilidade de deploy.

## 🚀 Destaques e Tecnologias

* **Análise Exploratória (EDA):** Identificação de padrões de comportamento e definição da variável target (Churn) baseada na inatividade do usuário.
* **Modelagem Preditiva:** Teste e seleção de algoritmos (ex: Random Forest, XGBoost) para maximizar a métrica de [F1 Score e ROC].
* **MLflow Tracking:** Utilizado para registrar parâmetros, métricas e versionar os modelos gerados durante os experimentos.
* **Docker:** O modelo final foi encapsulado em um container Docker, garantindo que a aplicação de inferência rode de forma isolada e reproduzível em qualquer ambiente.

## 🛠️ Arquitetura do Projeto

1.  **Ingestão & Processamento:** Limpeza de dados e Feature Engineering.
2.  **Treinamento:** Pipeline de treino com validação cruzada.
3.  **Tracking:** Logs automáticos via MLflow.
4.  **Deploy:** API servida via [Flask/FastAPI/Streamlit] dentro de um container Docker.

## 📦 Como Rodar

### Pré-requisitos
* Docker instalado
* Python 3.8+

### Passo a passo

1. Clone o repositório:
```bash
git clone [https://github.com/seu-usuario/netflix-churn-project.git](https://github.com/seu-usuario/netflix-churn-project.git)
cd netflix-churn-project
```

2. Construa a imagem Docker:

```
docker build -t netflix-churn-model .
```
3. Execute o container: 

```
docker run -p 5000:5000 netflix-churn-model
```


## 📊 Resultados

*Em breve*
