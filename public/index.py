import plotly.express as px
import pandas as pd
import streamlit as st
import plotly

# Read Data From Excel and store in a variable df [dataframe]
df = pd.read_excel("data-penindakan-pelanggaran-lalu-lintas-dan-angkutan-jalan-tahun-2021-bulan-januari.xlsx", usecols="A:C")
df.dropna(inplace=True)

# Store each column in a seperate varibale.
wilayah = df["wilayah"]
bap_tilang = df["bap_tilang"]


# Create Animated Bar Chart and store figure as fig
fig = px.bar(
    df,
    x=wilayah,
    y=bap_tilang,
    color=wilayah,
    animation_group=wilayah,
    range_y=[0, 200],
)

# Save Chart and export to HTML
plotly.offline.plot(fig, filename="index.html")  