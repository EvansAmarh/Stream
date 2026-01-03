import streamlit as st 
import numpy as np
import pandas as pd

# np.random.seed(0)  # seed for reproducibility
# df = pd.DataFrame(np.random.randn(4, 3), columns=("Column 1", "Column 2", "Column 3"))
# st.subheader("Actual Dataframe")
# st.dataframe(df)
# # df = df[df["Column 1"] > -1] # Filtering dataframe - Mutating it
# df = df.assign(Column_4 = lambda x: x["Column 1"]*2)
# st.subheader("Mutated Dataframe")
# st.dataframe(df)


df = pd.DataFrame(np.random.randint(0, 101, size=(6, 3)), columns=("Exam 1", "Exam 2", "Exam 3"))
df["Name"] = ["Jerry", "Don", "Mickey", "Sam", "Helen", "Dave"]
df["Category"] = ["A", "A", "B", "A", "B", "A"]
st.subheader("Actual Dataframe")
st.dataframe(df)
df_grouped = df.groupby(["Name", "Category"]).first()
st.subheader("Mutated Dataframe")
st.dataframe(df_grouped)