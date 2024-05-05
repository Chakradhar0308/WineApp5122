import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
import average,datas,graph

@st.cache_data(experimental_allow_widgets=True) 
def mainFunction():
    wine_data = load_wine()
    df = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)
    df['Winetype'] = wine_data.target
    st.write(df)
    st.title(":Red[Wine Dataset] :green[Analysis] :tea: :coffee: :chart: :bar_chart:")
    st.markdown("Exploring the correlation between the componenets used in crafting different categories of Wines")

    tab1,tab2,tab3=st.tabs(['Data','Average','Graphs'])

    with tab1:
        datas.dataFunction(df)
    with tab2:
        average.avgFubction(df)
    with tab3:
        graph.graphFunction(df)


mainFunction()


#st.write(wine_dataset.DESCR)


     
