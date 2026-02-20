class ForecastEngine:

    def __init__(self, savingsPriority, annualIncomeGrowthRate):
        self.savingsPriority = savingsPriority
        self.annualIncomeGrowthRate = annualIncomeGrowthRate

    def simulate(self, state, months):
        currSavings = state.getSavingsBal()
        currDebt = state.getDebtBal()
        currIncome = state.getTotalMonthlyIncome()
        r = self.annualIncomeGrowthRate
        monthlyGrowthRate = (1 + r) ** (1/12) - 1
        results = []

        for x in range (months):
            surplus = currIncome - state.getTotalMonthlyExpense()
            if(self.savingsPriority):
                currSavings += surplus
            monthData = {
                "month": x + 1,
                "savings": currSavings,
                "debt": currDebt,
                "net_worth": currSavings - currDebt
            }
            results.append(monthData)
            currIncome *= (1 + monthlyGrowthRate)

        return results