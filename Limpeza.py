# %%

import pandas as pd

cafe = pd.read_csv("./Tabela/cafe.csv")


cafe.to_excel("./Tabela/cafe.xlsx", index=False)

# %%

renamed_columns = {
                            "Transaction ID":"Id de Transação", "Quantity": "Quantidade", "Price Per Unit": "Preço por Unidade", "Total Spend": "Total Gasto", "Payment Method": "Forma de Pagamento", "Location": "Local", "Transaction Date": "Data de Transação"}
cafe.rename (columns=renamed_columns, inplace= True)
cafe

# %%

replace = {"UNKNOWN": "Informação não encontrada", "ERROR": "Incorreto"}
cafe = cafe.replace(replace)
cafe.fillna({"Forma de Pagamento" : "Item não encontrado", "Item" : "Pagamento não registrado" })