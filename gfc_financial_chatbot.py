import pandas as pd


class GFCFinancialChatbot:
    """Rule-based financial chatbot prototype for Global Finance Corp. (GFC)
    backed by 10-K financial data (FY2023-FY2025) for Apple, Microsoft, and Tesla.
    """

    PREDEFINED_QUERIES = [
        "What is the total revenue?",
        "How has net income changed over the last year?",
        "What are the total assets and total liabilities?",
        "What is the cash flow from operating activities?",
        "Compare total revenue across companies",
    ]

    COMPANY_ALIASES = {
        "apple": "Apple",
        "aapl": "Apple",
        "microsoft": "Microsoft",
        "msft": "Microsoft",
        "tesla": "Tesla",
        "tsla": "Tesla",
    }

    def __init__(self, csv_path: str = "financial_data_10k_2023_2025.csv"):
        self.df = pd.read_csv(csv_path).sort_values(["Company", "Fiscal Year"]).reset_index(drop=True)
        self._prepare_metrics()
        self.state = {
            "last_company": "Microsoft",
            "last_year": 2025,
        }

    def _prepare_metrics(self) -> None:
        self.df["Revenue Growth (%)"] = (self.df.groupby("Company")["Total Revenue"].pct_change() * 100).round(2)
        self.df["Net Income Growth (%)"] = (self.df.groupby("Company")["Net Income"].pct_change() * 100).round(2)
        self.df["OCF Growth (%)"] = (
            self.df.groupby("Company")["Cash Flow from Operating Activities"].pct_change() * 100
        ).round(2)
        self.df["Net Margin (%)"] = ((self.df["Net Income"] / self.df["Total Revenue"]) * 100).round(2)

    def _detect_company(self, query: str) -> str:
        q_lower = query.lower()
        for alias, canonical in self.COMPANY_ALIASES.items():
            if alias in q_lower:
                self.state["last_company"] = canonical
                return canonical
        return self.state["last_company"]

    def _detect_year(self, query: str) -> int:
        for yr in [2023, 2024, 2025]:
            if str(yr) in query:
                self.state["last_year"] = yr
                return yr
        return self.state["last_year"]

    def _get_row(self, company: str, year: int) -> pd.Series:
        matches = self.df[(self.df["Company"] == company) & (self.df["Fiscal Year"] == year)]
        if matches.empty:
            matches = self.df[self.df["Company"] == company].sort_values("Fiscal Year").tail(1)
        return matches.iloc[0]

    def simple_chatbot(self, user_query: str) -> str:
        """Rule-based handler mapping predefined financial queries to verified 10-K metrics."""
        q = user_query.strip()
        q_norm = q.lower()
        company = self._detect_company(q)
        year = self._detect_year(q)
        row = self._get_row(company, year)

        if q == "What is the total revenue?" or ("total revenue" in q_norm and "compare" not in q_norm):
            rev = int(row["Total Revenue"])
            yoy = row["Revenue Growth (%)"]
            yoy_str = f" ({yoy:+.2f}% YoY)" if pd.notna(yoy) else " (base year in dataset)"
            return (
                f"The total revenue for {company} in FY{year} is ${rev:,} million{yoy_str}. "
                f"Insight: Top-line scale reflects {company}'s core demand trajectory in its 10-K filing."
            )

        elif q == "How has net income changed over the last year?" or (
            "net income" in q_norm and ("changed" in q_norm or "growth" in q_norm or "last year" in q_norm)
        ):
            ni = int(row["Net Income"])
            yoy = row["Net Income Growth (%)"]
            margin = row["Net Margin (%)"]
            if pd.notna(yoy):
                direction = "increased" if yoy >= 0 else "decreased"
                return (
                    f"For {company} in FY{year}, net income {direction} by {abs(yoy):.2f}% year-over-year "
                    f"to ${ni:,} million (Net Profit Margin: {margin:.2f}%). "
                    f"Insight: Compare bottom-line change against revenue growth to assess margin expansion or compression."
                )
            return (
                f"For {company} in FY{year} (earliest year in our 2023-2025 dataset), net income is ${ni:,} million "
                f"(Net Profit Margin: {margin:.2f}%). No prior-year YoY change is available before FY2023."
            )

        elif "total assets" in q_norm or "total liabilities" in q_norm:
            assets = int(row["Total Assets"])
            liab = int(row["Total Liabilities"])
            ratio = (liab / assets) * 100
            return (
                f"For {company} in FY{year}, Total Assets are ${assets:,} million and Total Liabilities are "
                f"${liab:,} million (Liabilities-to-Assets ratio: {ratio:.2f}%). "
                f"Insight: Balance sheet leverage should be interpreted alongside cash flow and capital return policies."
            )

        elif "operating cash flow" in q_norm or "cash flow from operating activities" in q_norm:
            ocf = int(row["Cash Flow from Operating Activities"])
            yoy = row["OCF Growth (%)"]
            yoy_str = f" ({yoy:+.2f}% YoY)" if pd.notna(yoy) else " (base year in dataset)"
            return (
                f"For {company} in FY{year}, Cash Flow from Operating Activities is ${ocf:,} million{yoy_str}. "
                f"Insight: Operating cash flow measures core cash generation supporting investments and liquidity."
            )

        elif "compare total revenue" in q_norm or ("compare" in q_norm and "revenue" in q_norm):
            sub = self.df[self.df["Fiscal Year"] == year].sort_values("Total Revenue", ascending=False)
            parts = [f"{r['Company']}: ${int(r['Total Revenue']):,}M" for _, r in sub.iterrows()]
            return (
                f"Total Revenue comparison across companies in FY{year}: " + " | ".join(parts) + ". "
                f"Insight: Highlighting scale differences helps GFC clients benchmark market leaders."
            )

        else:
            supported = "\n  - ".join(self.PREDEFINED_QUERIES)
            return (
                "Sorry, I can only provide information on predefined financial queries for Apple, Microsoft, "
                "and Tesla (FY2023-FY2025). Try asking:\n  - " + supported
            )


def run_tests() -> list[dict]:
    bot = GFCFinancialChatbot("financial_data_10k_2023_2025.csv")
    queries = [
        "What is the total revenue? Microsoft 2025",
        "How has net income changed over the last year? Tesla 2025",
        "What are the total assets and total liabilities? Apple 2025",
        "What is the cash flow from operating activities? Microsoft 2025",
        "Compare total revenue across companies in 2025",
        "What is Amazon's stock price tomorrow?",
    ]
    return [{"query": q, "response": bot.simple_chatbot(q)} for q in queries]


if __name__ == "__main__":
    for item in run_tests():
        print(f"Q: {item['query']}")
        print(f"A: {item['response']}")
        print("-" * 70)

    # Interactive CLI loop (uncomment to run interactively)
    # bot = GFCFinancialChatbot("financial_data_10k_2023_2025.csv")
    # while True:
    #     user_in = input("\nAsk GFC Chatbot (or type 'exit'): ")
    #     if user_in.strip().lower() == "exit":
    #         break
    #     print(bot.simple_chatbot(user_in))
