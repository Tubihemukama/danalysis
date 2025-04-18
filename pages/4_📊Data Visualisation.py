

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="visuals page",
    page_icon= "🅰📊"
)


st.title("📊 Visualization Page")
st.write("Create plots and charts here.")

#Basic Statistics
if "data" in st.session_state:
    data = st.session_state.data
    st.write('Some statistics')
        
    #Visualisation

    
    numeric_columns = data.select_dtypes(include='number').columns

    #Histogram for each numeric variable
    st.write('Data Visualisation')
    column = st.selectbox('Selecet a column to visualise ', numeric_columns)
    #Display histogram
    st.write(f"Histogram of Column {column}")
    plt.figure(figsize=(10,5))
    sns.histplot(data[column], kde=True)
    st.pyplot(plt)

    #Bar graph
    # Bar graph
   
    non_numeric_columns = data.select_dtypes(include=["object", "string", "category"]).columns

    # Bar plot for each non-numeric column
    st.write('**Bar Graphs**')
    column = st.selectbox('Select a column to visualize', non_numeric_columns)

    # Count occurrences of each unique value
    value_counts = data[column].value_counts().reset_index()
    value_counts.columns = [column, 'count']

    # Display bar chart
    st.write(f"Bar chart of column: {column}")
    plt.figure(figsize=(10, 5))
    sns.barplot(x=column, y='count', data=value_counts)
    plt.xticks(rotation=45)
    st.pyplot(plt)


    #Display scatterplot for numeric variables
  
    st.write("**Scatter Plots**")
    numeric_columns = data.select_dtypes(include='number').columns
    st.write('scatter plot')
    x_column = st.selectbox('Select x-axis for the scatter plot ', numeric_columns)
    y_column = st.selectbox('Select y-axis for the scatter plot ', numeric_columns)
    plt.figure(figsize=(10,5))
    sns.scatterplot(data= data, x = x_column, y = y_column)
    st.pyplot(plt)




else:
    st.warning("No data found. Go to the upload data page and upload your excel file")
