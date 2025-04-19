import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Page Config
st.set_page_config(page_title="Data Visualization", page_icon="📊")

st.title("📊 Data Visualization Page")

if "data" in st.session_state:
    data = st.session_state.data

    st.markdown("### 📊 1. Visualize Numeric Variables")
    numeric_columns = data.select_dtypes(include='number').columns

    if len(numeric_columns) > 0:
        st.write("Visualize the distribution and relationships of numeric variables.")

        # Histogram for Numeric Variables
        with st.expander("📈 Histogram"):
            column = st.selectbox('Select a numeric column for histogram', numeric_columns)
            st.write(f"Histogram of column: {column}")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.histplot(data[column], kde=True, ax=ax)
            st.pyplot(fig)

        # Boxplot for Numeric Variables
        with st.expander("📦 Box Plot"):
            column = st.selectbox('Select a numeric column for boxplot', numeric_columns)
            st.write(f"Boxplot of column: {column}")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.boxplot(data[column], ax=ax)
            st.pyplot(fig)

        # Correlation Heatmap
        with st.expander("🔗 Correlation Heatmap"):
            if len(numeric_columns) >= 2:
                corr = data[numeric_columns].corr()
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
                st.pyplot(fig)
            else:
                st.warning("Not enough numeric columns for correlation analysis.")

    else:
        st.warning("No numeric columns found in the dataset.")

    st.markdown("### 📊 2. Visualize Categorical Variables")
    categorical_columns = data.select_dtypes(include=['object', 'category', 'string']).columns

    if len(categorical_columns) > 0:
        st.write("Visualize the distribution of categorical variables.")

        # Bar Plot for Categorical Variables
        with st.expander("📊 Bar Chart"):
            column = st.selectbox('Select a categorical column for bar chart', categorical_columns)
            st.write(f"Bar chart of column: {column}")
            value_counts = data[column].value_counts().reset_index()
            value_counts.columns = [column, 'count']
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(x=column, y='count', data=value_counts, ax=ax)
            plt.xticks(rotation=45)
            st.pyplot(fig)

        # Pie Chart for Categorical Variables
        with st.expander("🍰 Pie Chart"):
            column = st.selectbox('Select a categorical column for pie chart', categorical_columns)
            st.write(f"Pie chart of column: {column}")
            pie_data = data[column].value_counts()
            fig = px.pie(names=pie_data.index, values=pie_data.values, title=f"Pie Chart of {column}")
            st.plotly_chart(fig)
    else:
        st.warning("No categorical columns found in the dataset.")

    st.markdown("### 📊 3. Visualize Relationships Between Variables")

    if len(numeric_columns) >= 2:
        # Scatter Plot for Numeric vs Numeric
        with st.expander("🪶 Scatter Plot"):
            x_column = st.selectbox('Select x-axis column', numeric_columns)
            y_column = st.selectbox('Select y-axis column', numeric_columns)
            st.write(f"Scatter plot of {x_column} vs {y_column}")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.scatterplot(data=data, x=x_column, y=y_column, ax=ax)
            st.pyplot(fig)

    # Pairplot for Multiple Numeric Variables
    with st.expander("🔗 Pair Plot"):
        if len(numeric_columns) >= 3:
            st.write("Pair plot of multiple numeric variables")
            pairplot_data = st.multiselect('Select numeric columns for pairplot', numeric_columns)
            if len(pairplot_data) > 1:
                sns.pairplot(data[pairplot_data])
                st.pyplot()
            else:
                st.warning("Please select more than one column for pairplot.")
        else:
            st.warning("Not enough numeric columns for pairplot.")

    st.markdown("### 📊 4. Custom Interactive Plot with Plotly")
    st.write("Explore interactive plots using Plotly.")

    plot_choice = st.selectbox("Choose a plot type", ["Scatter Plot", "Bar Chart", "Line Chart"])
    
    if plot_choice == "Scatter Plot":
        if len(numeric_columns) >= 2:
            x_column = st.selectbox('Select x-axis for scatter plot', numeric_columns)
            y_column = st.selectbox('Select y-axis for scatter plot', numeric_columns)
            st.write(f"Interactive Scatter plot of {x_column} vs {y_column}")
            fig = px.scatter(data, x=x_column, y=y_column, title=f"{x_column} vs {y_column}")
            st.plotly_chart(fig)
        else:
            st.warning("Please upload numeric data for scatter plot.")
    
    elif plot_choice == "Bar Chart":
        if len(categorical_columns) > 0:
            column = st.selectbox('Select a categorical column for bar chart', categorical_columns)
            st.write(f"Interactive Bar chart of column: {column}")
            value_counts = data[column].value_counts().reset_index()
            value_counts.columns = [column, 'count']
            fig = px.bar(value_counts, x=column, y='count', title=f"Bar chart of {column}")
            st.plotly_chart(fig)
        else:
            st.warning("Please upload categorical data for bar chart.")

    elif plot_choice == "Line Chart":
        if len(numeric_columns) >= 2:
            x_column = st.selectbox('Select x-axis for line chart', numeric_columns)
            y_column = st.selectbox('Select y-axis for line chart', numeric_columns)
            st.write(f"Interactive Line chart of {x_column} vs {y_column}")
            fig = px.line(data, x=x_column, y=y_column, title=f"{x_column} vs {y_column}")
            st.plotly_chart(fig)
        else:
            st.warning("Please upload numeric data for line chart.")

else:
    st.warning("No data found. Go to the upload data page and upload your excel file.")
