import streamlit as st
from sklearn.datasets import load_wine
import pandas as pd

@st.cache_data
def data_load(w_df): ## Dataset
    w = load_wine()
    #w_df = pd.DataFrame(w.data, columns=w.feature_names) 
    w_df["WineType"] = [w.target_names[t] for t in w.target]
    mapping = {0: "class_0", 1: "class_1", 2: "class_2"}
    w_df["Winetype"] = w_df["Winetype"].map(mapping)
    return w_df

def avgFubction(w_df):
    w_df = data_load(w_df)
    ingredients = w_df.drop(columns=["WineType"]).columns

    avg_wine_df = w_df.groupby("WineType").mean().reset_index() ## Avg Ingredients.

    st.sidebar.header("Choose Ingredients per Wine Type.")

    bar_multiselect = st.sidebar.multiselect(label="Ingredients", options=ingredients, default=["alcohol", "malic_acid", "ash"])

    st.bar_chart(avg_wine_df, x="WineType", y=bar_multiselect, height=500, use_container_width=True)