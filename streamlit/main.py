import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns


#st.title("Data Analysis and Visualization ")
st.set_page_config(layout="wide")
df_variables = pd.read_csv("./data/diabetes_variables.csv")
df_origin = pd.read_csv("./data/diabetes_data.csv")

st.session_state["df_variables"] = df_variables
st.session_state["df_origin"] = df_origin
show_pages = {
    "Variable Explorations":[
        st.Page("./pages/variable_exploration.py",title="Variable Explorations",icon="📊"),
        st.Page("./pages/categorical_variable_frequency_table.py",title="Categorical Variable Frequency Table",icon="📋"),
        st.Page("./pages/descriptive_stats_table.py",title="Descriptive Statistics Table",icon="📈"),
        st.Page("./pages/missing_values_by_variable.py",title="Missing Values by Variable",icon="❓"),
        st.Page("./pages/unique_values_by_variable.py",title="Unique Values by Variable",icon="🔢"),
    ],
    "Univariate Analysis":[
        st.Page("./pages/histograms_of_counts.py",title="Histograms of Counts for Categorical Features",icon="🔢"),
        st.Page("./pages/Kernel_density_plot.py",title="Kernel Density Plot for Numeric Features",icon="📊"),
        st.Page("./pages/swarm_plot_for_outliers.py",title="Swarm Plot for Outliers",icon="📉"),
    ],
    "Bivariate Analysis":[
        st.Page("./pages/pair_plot_for_showing_the_distribution.py",title="Pair Plot for Showing the Distribution",icon="📉"),
        st.Page("./pages/Boxplot_for_showing_the_distribution.py",title="Box Plot for Showing the Distribution",icon="🧊"),
    ],
    "Multivariate Analysis":[
        st.Page("./pages/Correlation_Heatmap.py",title="Correlation Heatmap",icon="📊"),
    ]

}

pg =st.navigation(show_pages)
pg.run()