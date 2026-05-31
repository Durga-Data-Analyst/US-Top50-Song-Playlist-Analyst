import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="US Top50 Music Analytics",layout="wide")

df=pd.read_csv("featured_playlist.csv")
metrics=pd.read_csv("song_metrics.csv")

df["date"]=pd.to_datetime(df["date"])

st.sidebar.header("Filters")

artist=st.sidebar.multiselect(
"Artist",
df["artist"].unique()
)

rank=st.sidebar.slider(
"Rank Range",
1,50,(1,50)
)

album=st.sidebar.multiselect(
"Album Type",
df["album_type"].unique(),
default=df["album_type"].unique()
)

filtered=df[
(df["position"]>=rank[0]) &
(df["position"]<=rank[1]) &
(df["album_type"].isin(album))
]

if artist:
  filtered=filtered[filtered["artist"].isin(artist)]

tab1,tab2,tab3,tab4,tab5=(
st.tabs([
"KPI Overview",
"Timeline",
"Song Trends",
"Artist Leaderboard",
"Popularity"
])
)

with tab1:
  st.metric("Songs",filtered["song"].nunique())
  st.metric("Artists",filtered["artist"].nunique())
  st.metric("Avg Popularity",round(filtered["popularity"].mean(),2))

with tab2:
  chart=filtered.groupby("date")["position"].mean()

  fig,ax=plt.subplots()
  ax.plot(chart.index,chart.values)
  ax.set_title("Daily Average Rank")
  st.pyplot(fig)

with tab3:
  top=metrics.sort_values(
  "Days_on_chart",
  ascending=False
  ).head(10)

  st.dataframe(top)

with tab4:
  leader=(filtered.groupby("artist")
  ["song"].nunique()
  .sort_values(ascending=False)
  .head(10))

  fig,ax=plt.subplots()
  ax.bar(leader.index,leader.values)
  plt.xticks(rotation=90)

  st.pyplot(fig)

with tab5:
  fig,ax=plt.subplots()

  ax.scatter(
  filtered["popularity"],
  filtered["position"]
  )

  ax.set_xlabel("Popularity")
  ax.set_ylabel("Rank")

  st.pyplot(fig)
