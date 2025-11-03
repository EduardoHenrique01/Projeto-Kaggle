# %%

import pandas as pd

cafe = pd.read_csv("./Tabela/cafe.csv")


cafe.to_excel("./Tabela/cafe.xlsx", index=False)

# %%
cafe 