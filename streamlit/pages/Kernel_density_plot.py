import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Kernel Density Plot for Numeric Features")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]


df_variables_integer = df_variables[df_variables["type"] == "Integer"]["name"]
nrows = np.ceil(len(df_variables_integer)//2)
ncols = 2
fig,axes=plt.subplots(nrows,ncols,figsize=(12, 8*nrows))
for idx,col in enumerate(df_variables_integer):
    r = idx // ncols
    c = idx % ncols
    sns.histplot(df_origin[col], ax=axes[r,c], bins=20, color='skyblue',kde=True)
    axes[r,c].set_title(f'Distribution of {col} | Skewness: {df_origin[col].skew():.2f} | Kurtosis: {df_origin[col].kurtosis():.2f}')
plt.tight_layout() 
st.pyplot(fig)