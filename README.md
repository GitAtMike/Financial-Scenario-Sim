# Financial Scenario Simulator

A Python-based financial planning tool that models your monthly cash flow and forecasts savings and debt payoff over time. Built with Streamlit for an interactive web interface.

## Features

- Input monthly income, fixed expenses, and variable expenses
- Track savings balance and debt balance
- Calculate monthly surplus after all expenses
- Forecast financial outcomes across multiple scenarios
- Interactive UI built with Streamlit

## Tech Stack

- **Language:** Python
- **UI:** Streamlit
- **Architecture:** Modular finance engine (models, forecasting, simulation)
- **Testing:** pytest unit tests

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/GitAtMike/Financial-Scenario-Sim.git
cd Financial-Scenario-Sim
pip install -r requirements.txt
streamlit run app/app.py
```

## Project Structure
Financial-Scenario-Sim/
├── app/
│   └── app.py              # Streamlit UI entry point
├── finance_engine/
│   ├── models.py           # FinancialState class (income, expenses, balances)
│   ├── forecast.py         # Forecasting logic
│   └── simulator.py        # Scenario simulation engine
└── tests/
└── test_forecast.py    # Unit tests

## Roadmap

- [ ] Add charts to visualize savings growth and debt payoff over time
- [ ] Support multiple income sources
- [ ] Export forecast results to CSV
- [ ] Add side-by-side scenario comparison view
- [ ] Deploy as a live web app via Streamlit Cloud
