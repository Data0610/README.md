import pandas as pd
import plotly.express as px
import streamlit as st

# Helper function to check installed packages
def check_installed_packages():
    import importlib
    packages = ['streamlit', 'pandas', 'plotly']
    for package in packages:
        try:
            importlib.import_module(package)
        except ImportError:
            st.error(f"Error: The package '{package}' is not installed. Please install it using pip.")
            return False
    return True

# Check if necessary packages are installed
if not check_installed_packages():
    st.stop()  # Stop the execution if packages are missing

# Try reading the CSV file and handle errors
try:
    car_data = pd.read_csv('vehicles_us.csv')  # Make sure the file exists in the same directory
except FileNotFoundError:
    st.error("Error: The file 'vehicles_us.csv' was not found. Please ensure the file is in the project directory.")
    st.stop()  # Stop the execution if the file is not found

# Title of the application
st.header("Análisis del Conjunto de Datos de Vehículos")

# Button to create a histogram
hist_button = st.button('Construir histograma')

if hist_button:  # When the button is clicked
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Create a histogram using 'odometer' as x
    fig = px.histogram(car_data, x="odometer")
    
    # Show an interactive Plotly chart
    st.plotly_chart(fig, use_container_width=True)

# Button to create a scatter plot
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # When the button is clicked
    st.write('Creación de un gráfico de dispersión para el conjunto de datos')
    
    try:
        # Create a scatter plot using 'odometer' and 'price'
        fig_scatter = px.scatter(car_data, x="odometer", y="price")  # Make sure 'price' is a valid column
        st.plotly_chart(fig_scatter, use_container_width=True)
    except ValueError:
        st.error("Error: One of the specified columns ('odometer' or 'price') does not exist in the dataset.")

# Optional: Checkboxes for creating graphs
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_histogram:  # If the checkbox for the histogram is selected
    st.write('Creación de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:  # If the checkbox for the scatter plot is selected
    st.write('Creación de un gráfico de dispersión para el conjunto de datos')
    try:
        fig_scatter = px.scatter(car_data, x="odometer", y="price")  # Ensure 'price' is valid
        st.plotly_chart(fig_scatter, use_container_width=True)
    except ValueError:
        st.error("Error: One of the specified columns ('odometer' or 'price') does not exist in the dataset.")
