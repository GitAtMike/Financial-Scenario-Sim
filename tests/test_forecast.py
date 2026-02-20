from finance_engine import FinancialState, ForecastEngine

fs = FinancialState(4000,
                    {"rent": 1200, "insurance": 200},
                    {"food": 400, "gas": 150},
                    1000,
                    2000)

fe = ForecastEngine(True)

simulation = fe.simulate(fs, 3)

print(simulation)