import pandas as pd

class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    def print_with_headers(self):
        step = 10
        total_rows = len(self)
        for i in range(0, total_rows, step):
            print("\nColumn headers:\n", ", ".join(self.columns))
            print(self.iloc[i:i+step])  # вывод 10 строк
            print("-" * 40)

# --- Mainline ---
if __name__ == "__main__":
    dfp = DFPlus.from_csv("../csv/products.csv")
    dfp.print_with_headers()
