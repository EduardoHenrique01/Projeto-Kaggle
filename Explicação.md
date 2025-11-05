# Projeto de Limpeza e Análise Preliminar de Dados: Cafe

## 📊 Descrição Geral
Este projeto demonstra um fluxo de trabalho completo para limpeza de dados, desde a identificação de um dataset inconsistente até a preparação para análises. O objetivo principal foi transformar dados brutos e "sujos" em uma base de dados limpa e estruturada, pronta para gerar insights. Como parte da análise preliminar, foi explorado o perfil de gasto dos clientes.

## 🚀 Tecnologias Utilizadas
* **Python:** Linguagem principal para manipulação e limpeza de dados.
    * **Pandas:** Biblioteca essencial para DataFrames, tratamento e transformação de dados.
    * **Ambiente Virtual (`.venv`):** Para gerenciamento de dependências do projeto.

## ⚙️ Etapas de Processamento de Dados (ETL - Extract, Transform, Load)

### 1. **Setup do Ambiente**
* Criação de um ambiente virtual (`.venv`) para isolar as dependências do projeto.
* Ativação do ambiente virtual.

### 2. **Aquisição e Carga de Dados**
* Localização e carregamento de um dataset contendo informações dadas como "ERROR", ou celulas nulas.
    * *Desafio Principal:* O dataset apresentava dados bagunçados, valores inconsistentes e formatos inadequados.

### 3. **Limpeza e Transformação de Dados**
Esta fase focou em garantir a qualidade e a usabilidade dos dados:

* **Padronização de Nomes de Colunas:** Renomeação de colunas para garantir clareza e consistência no dataset.
* **Tratamento de Valores Ausentes e Erros:**
    * Identificação e substituição de valores nulos ou erros por dados consistentes e reais (ou uma estratégia definida como média/mediana/moda, conforme aplicável).
* **Ajuste de Tipos de Dados:**
    * Conversão da coluna `Total Gasto` de *string* para o tipo numérico (`float`) para permitir operações matemáticas.
### 4. **Análise Preliminar**

Após a limpeza, uma análise exploratória inicial foi realizada:

<<<<<<< HEAD
* **Identificação dos Clientes de Maior Gasto:** Ordenação do dataset para identificar e exibir o top 10 clientes que mais contribuíram em termos de gasto total.
=======
* **Identificação dos Clientes de Maior Gasto:** Ordenação do dataset para identificar e exibir o top 10 clientes que mais contribuíram em termos de gasto total.
>>>>>>> 33064fb91f68777ec79e1788f334b0b3d74348c6
