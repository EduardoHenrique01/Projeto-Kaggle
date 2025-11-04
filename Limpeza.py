# %%

import pandas as pd

cafe = pd.read_csv("./Tabela/cafe.csv")


cafe.to_excel("./Tabela/cafe.xlsx", index=False)

# %%

renamed_columns = {
                            "Transaction ID":"Id de Transação", "Quantity": "Quantidade", "Price Per Unit": "Preço por Unidade", "Total Spent": "Total Gasto", "Payment Method": "Forma de Pagamento", "Location": "Local", "Transaction Date": "Data de Transação"}
cafe.rename (columns=renamed_columns, inplace= True)
cafe

# %%

replace = {"UNKNOWN": "Informação não encontrada", "ERROR": "Incorreto", "Valor não encontrado": "0"}
cafe = cafe.replace(replace)
cafe = cafe.fillna({"Item" : "Item não encontrado","Quantidade": "0","Preço por Unidade": "0","Total Gasto": "0", "Forma de Pagamento" : "Pagamento não registrado", "Local":"Local não informado","Data de Trasação":"Data não encontrada" })

# %%
cafe["Total Gasto"] = cafe["Total Gasto"].astype(float)
top_10 = (cafe.sort_values(by= "Total Gasto", ascending=False)
         .head(10)["Id de Transação"])

top_10