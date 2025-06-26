import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="MLB College Dashboard", layout="wide")

# Загружаем данные
df = pd.read_csv("my_mlb_data.csv")
df["End Year"] = df["End Year"].astype(str).str.extract(r'(\d{4})')  # Извлекаем только год
df.dropna(subset=["End Year"], inplace=True)

# Преобразуем в числовой тип для фильтров
df["End Year"] = df["End Year"].astype(int)
df["Players Qty"] = pd.to_numeric(df["Players Qty"], errors="coerce")
df.dropna(subset=["Players Qty"], inplace=True)

st.title("\U0001F3EB MLB College Player Dashboard")

# === Фильтры ===
st.sidebar.header("\U0001F50D Filters")

# Фильтр по колледжу
all_colleges = sorted(df["College"].unique().tolist())
selected_college = st.sidebar.selectbox("Select a college (or All)", ["All"] + all_colleges)

# Фильтр по количеству игроков
min_qty = df["Players Qty"].astype(int).min()
max_qty = df["Players Qty"].astype(int).max()

if min_qty < max_qty:
    qty_range = st.sidebar.slider(
        "Number of Players (College Total)",
        min_value=min_qty,
        max_value=max_qty,
        value=(min_qty, max_qty)
    )
else:
    st.sidebar.write(f"Only one player count value available: {min_qty}")
    qty_range = (min_qty, max_qty)

# Фильтр по диапазону лет
min_year = int(df["End Year"].min())
max_year = int(df["End Year"].max())
year_range = st.sidebar.slider("Year range", min_value=min_year, max_value=max_year, value=(min_year, max_year))

# Фильтр по имени игрока
name_query = st.sidebar.text_input("Search by Player Name (optional)").strip().lower()

# === Применение фильтров ===
filtered_df = df[
    (df["Players Qty"].between(*qty_range)) &
    (df["End Year"].between(*year_range))
]

if name_query:
    filtered_df = filtered_df[filtered_df["Player"].str.lower().str.contains(name_query)]

# === Основной дашборд ===
st.subheader("\U0001F4CA College Summary")

college_summary = (
    filtered_df.groupby("College")
    .agg(Total_Players=("Player", "count"), Total_Qty=("Players Qty", "first"))
    .reset_index()
    .sort_values("Total_Players", ascending=False)
)

st.dataframe(college_summary, use_container_width=True)

# === Если выбран колледж — показать детали ===
if selected_college != "All":
    college_data = filtered_df[filtered_df["College"] == selected_college]

    st.subheader(f"\U0001F393 Players from {selected_college}")

    view_mode = st.radio(
        "Select view mode:",
        ["\U0001F4CB Table", "\U0001F4CA Charts"],
        horizontal=True,
        key="view_mode_radio"
    )

    if view_mode == "\U0001F4CB Table":
        st.markdown("**Player Table**")
        st.dataframe(college_data[["Player", "End Year"]].sort_values("End Year"), use_container_width=True)

    elif view_mode == "\U0001F4CA Charts":
        st.markdown("**Number of Players per Year**")
        year_players = (
            college_data.groupby("End Year")["Player"]
            .apply(lambda names: "<br>".join(names))
            .reset_index(name="Players")
        )
        year_players["Count"] = year_players["Players"].str.count("<br>") + 1

        fig = px.bar(
            year_players,
            x="End Year",
            y="Count",
            title=f"Yearly Player Distribution for {selected_college}",
            hover_data={"Players": True, "Count": False}
        )
        fig.update_traces(hovertemplate="<b>%{x}</b><br>%{customdata[0]}")
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Select a specific college to explore player details and visualizations.")
