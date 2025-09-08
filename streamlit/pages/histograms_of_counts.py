import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Variable Distribution Histograms")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]

df_variable_categorical = df_variables[df_variables["type"] == "Categorical"]["name"]
nrows = len(df_variable_categorical)//2
ncols = 2
fig, axes = plt.subplots(nrows, ncols, figsize=(14, 6*nrows))

for idx, col in enumerate(df_variable_categorical):
    row = idx // ncols
    col_idx = idx % ncols
    sns.histplot(df_origin[col], bins=20, ax=axes[row, col_idx], color='skyblue')
    axes[row, col_idx].set_title(f'Distribution of {col}')

plt.tight_layout()
st.pyplot(fig)