import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Función para resumen de variable booleana
def resumen_variable(df, var, nombre_display):
    total = len(df)
    presentes = df[var].sum()
    ausentes = total - presentes
    prop = presentes / total * 100
    
    print(f"""
##### **{nombre_display.upper()}**
<p align="center" style="font-size:16px;">
  <b>Presente:</b> <span style="color:#2a9d8f;">{presentes} vehículos</span> &nbsp;&nbsp;|&nbsp;&nbsp; 
  <b>No presente:</b> <span style="color:#e76f51;">{ausentes} vehículos</span> &nbsp;&nbsp;|&nbsp;&nbsp; 
  <b>Proporción:</b> <span style="color:#f4a261;">{prop:.1f}% con {nombre_display}</span>
</p>

---

<p style="max-width:1200px; margin:auto; line-height:1.5; text-align: justify;">
La variable <b>{var}</b> indica si el vehículo dispone de {nombre_display.lower()}. De los {total} registros, un total de <b>{presentes} vehículos ({prop:.1f}%)</b> cuentan con esta funcionalidad, mientras que el <b>{100-prop:.1f}%</b> restante no la incluye.<br><br>
Esto puede reflejar la antigüedad, gama o características tecnológicas de los vehículos.<br><br>
La variable no contiene valores nulos, permitiendo su uso directo en análisis y modelado.
</p>
""")
    
    print(f"# Estadísticas descriptivas para {var}")
    print(df[var].describe())
    
    plt.figure(figsize=(6,4))
    pal = ['#e76f51', '#2a9d8f'] if var == 'bluetooth' else ['#D4D2D2', '#348F07']
    sns.countplot(x=var, data=df, palette=pal)
    plt.title(f'Distribución de {nombre_display}')
    plt.xlabel(f'¿Tiene {nombre_display.lower()}?')
    plt.ylabel('')
    plt.xticks([0, 1], ['No', 'Sí'])
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
    
    modelos_con_var = df[df[var] == True]['modelo']
    modelo_mas_comun = modelos_con_var.mode()[0] if not modelos_con_var.empty else None
    
    edad_min = df[df[var] == True]['edad_coche'].min() if 'edad_coche' in df.columns else None
    
    potencia_min = df[df[var] == True]['potencia'].min() if 'potencia' in df.columns else None
    
    print(f"Modelo más común con {nombre_display.lower()}: {modelo_mas_comun}")
    print(f"Edad mínima del coche con {nombre_display.lower()}: {edad_min}")
    print(f"Potencia mínima con {nombre_display.lower()}: {potencia_min} CV")
    
    df_var_true = df[df[var] == True]
    if not df_var_true.empty:
        modelo_mas_caro = df_var_true.loc[df_var_true['precio'].idxmax()]['modelo']
        precio_max = df_var_true['precio'].max()
        modelo_mas_km = df_var_true.loc[df_var_true['km'].idxmax()]['modelo']
        km_max = df_var_true['km'].max()
    else:
        modelo_mas_caro = precio_max = modelo_mas_km = km_max = None
    
    print(f"Modelo más caro con {nombre_display.lower()}: {modelo_mas_caro} ({precio_max} €)")
    print(f"Modelo con más km con {nombre_display.lower()}: {modelo_mas_km} ({km_max} km)")
    print("\n" + "-"*60 + "\n")

    
# Variables a analizar con su nombre para display
variables_info = [
    ('volante_regulable', 'volante regulable'),
    ('aire_acondicionado', 'aire acondicionado'),
    ('camara_trasera', 'cámara trasera'),
    ('elevalunas_electrico', 'elevalunas eléctrico'),
    ('bluetooth', 'Bluetooth'),
    ('alerta_lim_velocidad', 'alerta límite de velocidad'),
    ('color_estandar', 'color estándar'),
]

# Asegúrate que color_estandar sea bool
df_bmw['color_estandar'] = df_bmw['color_estandar'].astype(bool)

# Ejecutamos resumen para cada variable
for var, display_name in variables_info:
    if var in df_bmw.columns:
        resumen_variable(df_bmw, var, display_name)
    else:
        print(f"La variable '{var}' no está en el dataframe.\n")