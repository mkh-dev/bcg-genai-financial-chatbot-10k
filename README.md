# 📊 BCG GenAI Consulting Job Simulation — 10-K Financial Analytics & Chatbot Prototype

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/Data-pandas-150458.svg)](https://pandas.pydata.org/)
[![Domain](https://img.shields.io/badge/Domain-Finance%20%26%20GenAI-0A66C2.svg)]()
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()

Completed a job simulation involving AI-powered financial chatbot development for BCG's GenAI Consulting team.  
Gained experience in Python programming, including the use of libraries such as `pandas` for data manipulation.  
Integrated and interpreted complex financial data from 10-K and 10-Q reports, employing rule-based logic to create a chatbot that provides user-friendly financial insights and analysis.

---

## 🎯 Objectifs & contexte métier

Dans le cadre d'une simulation pour **Global Finance Corp. (GFC)** au sein de l'équipe **GenAI Consulting de BCG**, ce projet vise à :
* Extraire, nettoyer et normaliser (en millions de dollars USD `$M`) des données financières issues des rapports annuels **10-K (FY2023–FY2025)** pour **Apple (`AAPL`)**, **Microsoft (`MSFT`)** et **Tesla (`TSLA`)**.
* Calculer de manière déterministe les variations annuelles (**YoY %**) et les ratios financiers clés (*Net Profit Margin*, *Liabilities-to-Assets*, *Operating Cash Flow*) avec `pandas`.
* Concevoir et tester un prototype de chatbot financier (`GFCFinancialChatbot`) combinant logique à base de règles (`if-elif-else`), détection d'entités (entreprise et exercice fiscal), gestion d'état (`state`) et gestion claire des requêtes hors périmètre.

---

## 📁 Contenu du dépôt

```text
├── financial_data_10k_2023_2025.csv      # Données 10-K normalisées (FY2023-FY2025, en $M)
├── financial_analysis_10k_2023_2025.xlsx  # Classeur Excel d'analyse comparative et de tendances
├── financial_analysis_10k_gfc.ipynb       # Notebook Jupyter d'exploration et de calcul de métriques
├── gfc_financial_chatbot.py               # Prototype du chatbot financier et suite de tests
├── test_results.txt                       # Résultats d'exécution sur les requêtes tests
├── README_chatbot.txt                     # Documentation technique du prototype
└── gfc_financial_chatbot.zip              # Archive de soumission regroupant les livrables du chatbot
```

---

## 📈 Aperçu des données 10-K analysées (FY2023–FY2025, en `$M`)

| Entreprise (`Ticker`) | Exercice | Total Revenue (`$M`) | Net Income (`$M`) | Total Assets (`$M`) | Total Liabilities (`$M`) | Operating Cash Flow (`$M`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Apple** (`AAPL`) | 2023 | 383,285 | 96,995 | 352,583 | 290,437 | 110,543 |
| **Apple** (`AAPL`) | 2024 | 391,035 | 93,736 | 364,980 | 308,030 | 118,254 |
| **Apple** (`AAPL`) | 2025 | 416,161 | 112,010 | 359,241 | 285,508 | 111,482 |
| **Microsoft** (`MSFT`) | 2023 | 211,915 | 72,361 | 411,976 | 205,753 | 87,582 |
| **Microsoft** (`MSFT`) | 2024 | 245,122 | 88,136 | 512,163 | 243,686 | 118,548 |
| **Microsoft** (`MSFT`) | 2025 | 281,724 | 101,832 | 619,003 | 275,524 | 136,162 |
| **Tesla** (`TSLA`) | 2023 | 96,773 | 14,974 | 106,618 | 43,009 | 13,256 |
| **Tesla** (`TSLA`) | 2024 | 97,690 | 7,153 | 122,070 | 48,390 | 14,923 |
| **Tesla** (`TSLA`) | 2025 | 94,827 | 3,794 | 137,806 | 54,941 | 14,747 |

---

## 🚀 Installation & exécution

### 1. Installer les dépendances
```bash
pip install pandas jupyter openpyxl
```

### 2. Lancer le notebook d'analyse
```bash
jupyter notebook financial_analysis_10k_gfc.ipynb
```

### 3. Tester le chatbot financier
```bash
python gfc_financial_chatbot.py
```

Requêtes prédéfinies gérées par le prototype :
* `"What is the total revenue?"`
* `"How has net income changed over the last year?"`
* `"What are the total assets and total liabilities?"`
* `"What is the cash flow from operating activities?"`
* `"Compare total revenue across companies"`

---

## ⚠️ Limites & évolutions futures

* **Limites actuelles :** La logique reposant sur des règles (`if-elif-else`) et des données structurées annuelles (`FY2023–FY2025`) ne couvre pas encore l'analyse fine des sections narratives (MD&A, facteurs de risque, notes annexes) ni les rapports trimestriels 10-Q.
* **Évolution envisagée :** Faire évoluer le prototype vers une architecture hybride combinant données structurées/SQL et **RAG** sur les documents financiers avec citations sources.

---

## 👤 Auteur

**Malek Khelil** — À la recherche d'un stage en **Data Science / Data Analytics / IA**.  
* LinkedIn : `https://www.linkedin.com/` *(à compléter)*  
* Email : `ton.email@exemple.com` *(à compléter)*
