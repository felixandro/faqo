# Diccionario División - Zona
div_zona_dict = {
    "FC00" : 'Chillán',
    "FT01" : 'Constitución',
    "BC01" : 'Arauco',
    "FS01" : 'Valdivia'
}

# Diccionario Centro - Procedencia
procedencia_dict = {
    "FNCC" : 'Compras',
    "FTCC" : 'Compras',
    "FTOC" : 'Compras',
    "FNOC" : 'Compras'
}

# Diccionario Canal - Tipo Venta
t_venta_dict = {
    20 : 'V Internas',
    25 : 'Canal 25',
    30 : 'V Terceros'
}

# Diccionario Elemento de coste -  Agrup CC
agrup_CC_dict = {
    1: 'M Prima',
    2: 'Volteo',
    3: 'Flete',
    4: 'Procesamiento',
    5: 'Caminos',
    6: 'VVJusto',
    7: 'M Prima',
    8: 'Volteo',
    9: 'Flete',
    10: 'Caminos',
    11: 'Procesamiento',
    12: 'VVJusto'
}

def generate_output(input_df):

    output_df = input_df.copy()

    # Columna "Zona"
    output_df["Zona"] = output_df["División"].map(div_zona_dict)

    # Columna "División_2"
    output_df["División_2"] = output_df["División"].copy()
    filtro_div2 = output_df["Centro"].str.contains("Y", na=False)
    output_df.loc[filtro_div2, "División_2"] = output_df.loc[filtro_div2, "División_2"] + " fcho"
    
    # Columna "Procedencia"
    output_df["Procedencia"] = output_df["Centro"].map(procedencia_dict)
    output_df["Procedencia"] = output_df["Procedencia"].fillna("Producción")

    # Columna Tipo Venta
    output_df["T Venta"] = output_df["Canal distribución"].map(t_venta_dict)

    # Columna Agrupación CC
    output_df["Agrup CC"] = output_df["Elemento de coste"].map(agrup_CC_dict)

    return output_df
