# %%

import pandas as pd

netflix = pd.read_csv("./Tabela/netflix1.csv")


netflix.to_excel("./Tabela/netflix.xlsx", index=False)

# %%