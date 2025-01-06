import pandas as pd
import plotly.express as px
import streamlit as st

# Function to read the CSV file with error handling
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        st.error(f"Error: The file '{file_path}' was not found. Please ensure the file is in the project directory.")
        st.stop()  # Stop execution if the file is not found
    except pd.errors.EmptyDataError:
        st.error(f"Error: The file '{file_path}' is empty. Please provide a valid CSV file.")
        st.stop()
    except pd.errors.ParserError:
        st.error(f"Error: There was a problem parsing the file '{file_path}'. Please ensure it is in a valid format.")
        st.stop()

# Load the dataset
car_data = load_data('vehicles_us.csv')  # Ensure the file is in the same directory

# Title of the application
st.header("Análisis del Conjunto de Datos de Vehículos")

# Create checkboxes to allow users to select which graph to display
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

# Creating the histogram
if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Check if 'odometer' column exists before creating the histogram
    if "odometer" in car_data.columns:
        fig = px.histogram(car_data, x="odometer")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Error: The column 'odometer' does not exist in the dataset.")

# Creating the scatter plot
if build_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos')
    
    # Check if both 'odometer' and 'price' columns exist before creating the scatter plot
    if "odometer" in car_data.columns and "price" in car_data.columns:
        fig_scatter = px.scatter(car_data, x="odometer", y="price")
        st.plotly_chart(fig_scatter, use_container_width=True)
    else:
        st.error("Error: One of the specified columns ('odometer' or 'price') does not exist in the dataset.")

# Handle potential warning related to ScriptRunContext
if not st.session_state.get('script_run_context', None):
    st.warning("Warning: Missing ScriptRunContext! This warning can be ignored when running in bare mode.")
