import streamlit as st
import pandas as pd
from Q1_process_input import generate_output
import io

input_xlsx = st.file_uploader("Upload an Excel file", type=["xlsx"])

if input_xlsx:
    input_df = pd.read_excel(input_xlsx)
    output_df = generate_output(input_df)

    output = io.BytesIO()
    output_df.to_excel(output, index=False, engine='openpyxl')
    output.seek(0)
    st.download_button(
        label="Descargar archivo Excel",
        data=output,
        file_name="output.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )



