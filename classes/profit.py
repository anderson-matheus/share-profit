class Profit:
    def __init__(self, values):
        self.values = values

    def calculate_profit(self):
        profits = list()
        for index, value in enumerate(self.values):
            if index == 0:
                continue

            i = index
            while i >= 0:
                profits.append(self.values[index] - self.values[i])
                i -= 1
        return max(profits)