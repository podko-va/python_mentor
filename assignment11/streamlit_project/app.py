import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np      # Helps generate random numbers
import plotly.express as px

# Заголовок
st.title("Пример интерактивного приложения на Streamlit")

# Ввод текста
name = st.text_input("Введите ваше имя:")
if name:
    st.success(f"Привет, {name}! 👋")

# Кнопка
if st.button("Нажми меня"):
    st.info("Кнопка нажата!")

# Чекбокс
if st.checkbox("Показать таблицу"):
    data = pd.DataFrame({
        'Число': [1, 2, 3, 4, 5],
        'Квадрат': [i**2 for i in range(1, 6)]
    })
    st.dataframe(data)

# График
st.markdown("### 📈 Пример графика")
chart_data = pd.DataFrame({
    'x': range(1, 11),
    'y': [i ** 2 for i in range(1, 11)]
})
fig, ax = plt.subplots()
ax.plot(chart_data['x'], chart_data['y'], marker='o')
ax.set_title("График y = x²")
ax.set_xlabel("x")
ax.set_ylabel("y")
st.pyplot(fig)



# Basic text elements
st.title("My First Streamlit App")  # Adds a big title at the top of the app
st.header("Section 1")  # Adds a section header — good for breaking content into parts
st.subheader("Header")  # Slightly smaller than header — useful for structure
st.subheader("Subheader")  # Another level down — keeps things organized
st.text("Simple text")  # Displays plain, unformatted text — like a basic message
st.markdown("**Bold** and *italic* text")  # Markdown lets you add simple formatting like bold and italics

# Display data
st.write("Automatic data display")  # Streamlit's flexible method — handles strings, numbers, dataframes, and more
st.code("print('Hello World')", language='python')  # Nicely formats code blocks with syntax highlighting
st.latex(r"\int_{a}^{b} x^2 dx")  # Renders LaTeX math formulas — great for equations

# Text input
st.header("Section 2")  # A new section to group interactive input components
name = st.text_input("Enter your name", "John Doe")  # Simple text field with a default value
description = st.text_area("Description", "Write something...")  # Multi-line text box for longer input

# Numeric input
age = st.number_input("Age", min_value=0, max_value=120, value=25)  # Number picker with min/max range
score = st.slider("Score", 0, 100, 50)  # Slider to pick a number in a range — great for ratings or scores

# Selection widgets
option = st.selectbox("Choose an option", ["A", "B", "C"])  # Dropdown menu — user picks one option
options = st.multiselect("Multiple options", ["X", "Y", "Z"])  # Allows multiple selections at once

# Date and time
date = st.date_input("Select date")  # Calendar-style date picker
time = st.time_input("Select time")  # Clock-style time picker

# Buttons and checkbox
if st.button("Click me"):  # A button that runs code when clicked
    st.write("Button clicked!")  # Responds when the button is pressed
    
if st.checkbox("Show/Hide"):  # Checkbox to toggle something on/off
    st.write("Visible content")  # Displays this text only if the box is checked

st.header("Section 3")

# Create two side-by-side columns
col1, col2 = st.columns(2)

with col1:  # Everything under this goes into the left column
    st.header("Column 1")
    st.write("Content for column 1")

with col2:  # Everything under this goes into the right column
    st.header("Column 2")
    st.write("Content for column 2")

# Expandable sections
with st.expander("Click to expand"):
    st.write("Expanded content here")

# Sidebar
st.sidebar.title("Sidebar")
sidebar_option = st.sidebar.selectbox("Select option", ["A", "B", "C"])

with col1:
    st.write("Some content")


# Create sample data — just faking some numbers to simulate a small product dataset
np.random.seed(42)  # Setting a seed so results are consistent every time you run
sample_data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Sales': np.random.randint(100, 500, size=4),   # Random sales numbers
    'Profit': np.random.randint(20, 100, size=4)    # Random profit numbers
}
df = pd.DataFrame(sample_data)  # Convert the data into a DataFrame for easy handling

# Sidebar filters — this shows up in the sidebar for user interaction
st.sidebar.header('Filter Options')  # Sidebar title
selected_product = st.sidebar.selectbox('Select Product', df['Product'])  # Dropdown to choose a product

# Filter the data based on the user's selection
filtered_df = df[df['Product'] == selected_product]  # Show only the row that matches the selected product

# Main app content starts here
st.title('Simple Product Dashboard')  # Big title for the dashboard

# Display key numbers using metrics — side-by-side using columns
col1, col2 = st.columns(2)  # Create two columns for layout
with col1:
    st.metric('Sales', f"${filtered_df['Sales'].values[0]:,}")  # Show sales in a pretty format
with col2:
    st.metric('Profit', f"${filtered_df['Profit'].values[0]:,}")  # Show profit similarly

# Add a bar chart comparing all products — gives full context beyond the filter
st.subheader('Sales and Profit Comparison')  # Subheading for the chart
bar_chart = px.bar(df, x='Product', y=['Sales', 'Profit'], barmode='group')  # Grouped bar chart
st.plotly_chart(bar_chart)  # Render the chart in the app