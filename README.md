# 🚢 Análise Exploratória de Dados — Base Titanic

## 📌 1. Contextualização

Este projeto foi desenvolvido como parte da atividade prática extra do curso **Introdução ao Data Science (IP 20h A)**, com o objetivo de aplicar conceitos fundamentais de Análise Exploratória de Dados (AED) utilizando a base pública do Titanic.

A proposta consiste em importar, organizar, tratar e analisar o conjunto de dados, buscando identificar padrões, relações entre variáveis e possíveis fatores associados à sobrevivência dos passageiros.

---

## 📂 2. Estrutura do Projeto

```
titanic-aed/
├── main.py
├── requirements.txt
├── README.md
├── insights.txt
├── data/
│   └── titanic.csv
└── outputs/
    ├── sobrevivencia_por_sexo.png
    ├── sobrevivencia_por_classe.png
    └── sobrevivencia_por_sexo_e_classe.png
```


---

## 🧠 3. Etapas Realizadas

### 3.1 Importação e Compreensão dos Dados

- Leitura do arquivo CSV
- Verificação da estrutura do dataset (linhas e colunas)
- Identificação de tipos de dados
- Análise de valores nulos
- Verificação de registros duplicados

---

### 3.2 Tratamento e Preparação

- Remoção de registros duplicados
- Preenchimento de valores nulos em `Embarked` com a moda
- Preenchimento de valores nulos em `Fare` com a mediana
- Criação da variável auxiliar `PossuiCabine`
- Organização estrutural para facilitar a análise

---

### 3.3 Análise Exploratória

Foram aplicadas técnicas de:

- Filtros
- Ordenações
- Agrupamentos (`groupby`)
- Cálculo de taxas percentuais

Principais investigações realizadas:

- Taxa de sobrevivência por sexo
- Taxa de sobrevivência por classe social
- Análise combinada de sexo e classe

---

## 📊 4. Visualizações

Foram gerados três gráficos:

1. **Sobrevivência por Sexo**
2. **Sobrevivência por Classe**
3. **Sobrevivência por Sexo e Classe (Análise Combinada)**

As visualizações permitem identificar padrões claros relacionados à desigualdade de sobrevivência entre grupos.

---

## 🔎 5. Principais Insights Obtidos

- Passageiras do sexo feminino apresentaram taxa de sobrevivência significativamente superior aos homens.
- Passageiros da 1ª classe tiveram maior probabilidade de sobreviver.
- A combinação *mulher + 1ª classe* apresentou a maior taxa de sobrevivência.
- Passageiros homens da 3ª classe apresentaram as menores taxas de sobrevivência.

Esses resultados indicam forte influência de fatores sociais e estruturais na probabilidade de sobrevivência.

Os insights detalhados encontram-se no arquivo `insights.txt`.

---

## ⚙️ 6. Tecnologias Utilizadas

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  

---

## ▶️ 7. Como Executar o Projeto

No terminal, dentro da pasta do projeto:

```bash
py -m pip install -r requirements.txt
py main.py
```
