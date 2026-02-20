class ForecastEngine:

    def __init__(self, savingsPriority):
        self.savingsPriority = savingsPriority

    def simulate(self, state, months):
        currSavings = state.getSavingsBal()
        currDebt = state.getDebtBal()
        results = []

        for x in range (months):
            surplus = state.getMonthlySurplus()
            if(self.savingsPriority):
                currSavings += surplus
            monthData = {
                "month": x + 1,
                "savings": currSavings,
                "debt": currDebt,
                "net_worth": currSavings - currDebt
            }
            results.append(monthData)

        return results