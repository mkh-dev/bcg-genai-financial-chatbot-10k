# 📊 BCG GenAI Consulting Job Simulation — 10-K Financial Analytics & Chatbot Prototype

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/Data-pandas-150458.svg)](https://pandas.pydata.org/)
[![Domain](https://img.shields.io/badge/Domain-Finance%20%26%20GenAI-0A66C2.svg)]()
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()

Completed a job simulation involving AI-powered financial chatbot development for BCG's GenAI Consulting team.  
Gained experience in Python programming, including the use of libraries such as `pandas` for data manipulation.  
Integrated and interpreted complex financial data from 10-K and 10-Q reports, employing rule-based logic to create a chatbot that provides user-friendly financial insights and analysis.

---

## 🎯 Project Overview & Business Context

Built as part of a **BCG GenAI Consulting** simulation for **Global Finance Corp. (GFC)**, this project demonstrates how structured financial data and deterministic analytics can power a reliable, transparent financial assistant:

* **SEC 10-K Data Extraction & Normalization (`FY2023–FY2025`):** Standardized five core financial metrics in USD millions (`$M`) across **Apple (`AAPL`)**, **Microsoft (`MSFT`)**, and **Tesla (`TSLA`)**: *Total Revenue*, *Net Income*, *Total Assets*, *Total Liabilities*, and *Cash Flow from Operating Activities*.
* **Deterministic Financial Analytics (`Python` & `pandas`):** Calculated year-over-year (**YoY %**) growth rates, net profit margins, and balance sheet leverage ratios prior to response generation to prevent calculation errors and numerical hallucinations.
* **Rule-Based Financial Chatbot Prototype (`GFCFinancialChatbot`):** Implemented intent/rule routing (`if-elif-else`), company and fiscal year detection, conversation state tracking (`state`), clear business takeaways, and explicit fallback handling for out-of-scope queries.

---

## 🖼️ Visual Walkthrough & Screenshots

> **Tip for recruiters & GitHub visitors:** Save your screenshots inside an `assets/` folder at the root of this repository and keep the filenames below so they render automatically on GitHub.

### 1. Chatbot CLI Execution & Test Validation
*Add a screenshot of your PowerShell/terminal output showing predefined financial queries and the fallback response for an out-of-scope query.*

![Chatbot CLI Execution in PowerShell](assets/chatbot_cli_output.png)

### 2. Multi-Year 10-K Trend & Comparison Visuals
*Add a screenshot or exported chart from your Jupyter Notebook or Excel workbook comparing revenue, net income, or cash flow across FY2023–FY2025.*

![10-K Financial Trends Across Apple, Microsoft, and Tesla](assets/financial_trends_chart.png)

---

## 📁 Repository Structure

```text
├── assets/                                # Screenshots and visual charts for the README
├── financial_data_10k_2023_2025.csv       # Normalized 10-K dataset (FY2023-FY2025, in $M)
├── financial_analysis_10k_2023_2025.xlsx   # Excel workbook with YoY metrics, ratios, and charts
├── financial_analysis_10k_gfc.ipynb        # Jupyter Notebook for exploratory & comparative analysis
├── gfc_financial_chatbot.py                # Rule-based financial chatbot prototype & test runner
├── test_results.txt                        # Saved test outputs across target & edge-case prompts
├── README_chatbot.txt                      # Technical documentation for the chatbot prototype
└── gfc_financial_chatbot.zip               # Packaged submission archive of chatbot deliverables
```

---

## 📈 Key 10-K Financial Metrics (`FY2023–FY2025`, in `$M`)

| Company (`Ticker`) | Fiscal Year | Total Revenue (`$M`) | Net Income (`$M`) | Total Assets (`$M`) | Total Liabilities (`$M`) | Operating Cash Flow (`$M`) |
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

### Key Takeaways
* **Microsoft (`MSFT`):** Consistent top-line and bottom-line expansion (`$211,915M` to `$281,724M` revenue; `$72,361M` to `$101,832M` net income) backed by strong operating cash flow (`$136,162M` in FY2025).
* **Apple (`AAPL`):** Largest revenue scale (`$416,161M` in FY2025) and robust operating cash flow (`$111,482M`), with liabilities-to-assets reflecting capital return dynamics rather than operational distress.
* **Tesla (`TSLA`):** Near-flat revenue across FY2024–FY2025 (`$94,827M` in FY2025) and net margin compression (`$3,794M` net income), while maintaining positive operating cash flow (`$14,747M`) and a conservative debt profile.

---

## 🚀 Setup & Usage

### 1. Install Dependencies
```bash
pip install pandas jupyter openpyxl
```

### 2. Run the Financial Analysis Notebook
```bash
jupyter notebook financial_analysis_10k_gfc.ipynb
```

### 3. Run the Chatbot Prototype
```bash
python gfc_financial_chatbot.py
```

Supported predefined queries:
* `"What is the total revenue?"`
* `"How has net income changed over the last year?"`
* `"What are the total assets and total liabilities?"`
* `"What is the cash flow from operating activities?"`
* `"Compare total revenue across companies"`

---

## ⚠️ Limitations & Future Roadmap

* **Current Limitations:** Deterministic `if-elif-else` rule matching and annual structured metrics (`FY2023–FY2025`) do not yet parse narrative 10-K sections (MD&A, risk factors, footnotes) or quarterly `10-Q` filings.
* **Next Steps:** Evolve toward a hybrid architecture combining structured queries/SQL with **RAG** over filing narratives (with source citations) and automated unit tests (`pytest`).
