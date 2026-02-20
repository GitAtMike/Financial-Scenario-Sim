class FinancialState:

    def __init__(self, monthlyIncome, fixedExpense, varExpense, savingsBal, debtBal):
        self.monthlyIncome = monthlyIncome
        self.fixedExpense = fixedExpense
        self.varExpense = varExpense
        self.savingsBal = savingsBal
        self.debtBal = debtBal


    def getTotalFixed(self):
        return sum(self.fixedExpense.values())

    def getTotalVar(self):
        return sum(self.varExpense.values())

    def getTotalMonthlyExpense(self):
        return self.getTotalFixed() + self.getTotalVar()

    def getTotalMonthlyIncome(self):
        return self.monthlyIncome

    def getSavingsBal(self):
        return self.savingsBal

    def getDebtBal(self):
        return self.debtBal

    def getMonthlySurplus(self):
        return self.getTotalMonthlyIncome() - self.getTotalMonthlyExpense()