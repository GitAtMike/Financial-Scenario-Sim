from finance_engine import FinancialState, ForecastEngine

fs = FinancialState(monthlyIncome=4000,
                    fixedExpense={"rent": 1200, "insurance": 200},
                    varExpense={"food": 400, "gas": 150},
                    savingsBal=1000,
                    debtBal=2000)

fe = ForecastEngine(True, 0.3)

simulation = fe.simulate(fs, 3)

for month in simulation:
    print(month["month"],
          round(month["savings"], 2),
          round(month["debt"], 2),
          round(month["net_worth"], 2))