GFC FINANCIAL CHATBOT PROTOTYPE - DOCUMENTATION
================================================

1. HOW IT WORKS
- Loads verified 10-K financial data (financial_data_10k_2023_2025.csv, in USD millions) for Apple (AAPL), Microsoft (MSFT), and Tesla (TSLA) across FY2023-FY2025.
- Computes year-over-year (YoY) growth rates and net profit margins deterministically using pandas.
- Uses rule-based if-elif-else matching (simple_chatbot) along with company/year detection (Apple, Microsoft, Tesla; 2023-2025), basic conversation state tracking (last_company, last_year), and a clear fallback message for unrecognized queries.

2. PREDEFINED QUERIES SUPPORTED
- "What is the total revenue?"
- "How has net income changed over the last year?"
- "What are the total assets and total liabilities?"
- "What is the cash flow from operating activities?"
- "Compare total revenue across companies"

3. LIMITATIONS
- Rule-based intent matching does not handle open-ended natural language or narrative analysis of 10-K sections (MD&A, Risk Factors, footnotes).
- Limited to FY2023-FY2025 annual 10-K data for three companies; extending to 10-Q filings, additional tickers, and a hybrid RAG + tabular/SQL architecture is planned for production.
