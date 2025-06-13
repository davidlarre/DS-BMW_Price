<p align="center">
  <img src="https://i.ebayimg.com/images/g/wSgAAOSw7D1mc-v3/s-l1200.jpg" alt="BMW logo" width="500"/>
</p>

# Proyecto de Preparación de Datos: Predicción de Precios de Vehículos BMW

---

## 🚀 Descripción del Proyecto

Este proyecto se enfoca en la fase crítica de **preparación de datos** para un dataset de vehículos BMW, con el objetivo final de establecer una base sólida para la futura predicción de precios. A través de un riguroso proceso de **limpieza, exploración y transformación de datos**, hemos abordado desafíos comunes en el mundo real para asegurar la calidad y utilidad del dataset.

El proyecto es parte del **Entregable 1: Data Preparation - BMW Pricing** y ha sido desarrollado por el equipo de **Lluís Miarnau, Ariadna Rubió, Sergio Vásquez y David Larré**.

---

## 🎯 Objetivos y Metodología

El proceso de preparación de datos se ha estructurado en las siguientes fases clave:

### 1. 🧹 Limpieza y Manejo Inicial de Datos
* **Inspección Inicial:** Se realizó una primera revisión del dataset para entender su estructura, tipos de datos y la presencia de valores nulos o atípicos.
* **Gestión de Columnas Irrelevantes:** Se identificó la columna `marca` que, al contener un único valor (`BMW`) o valores nulos (20.03%), no aporta valor predictivo y fue candidata para su eliminación para evitar redundancias y mejorar la eficiencia del modelo.
* **Identificación y Tratamiento de Outliers:** Se llevó a cabo una revisión de valores numéricos, como `km` (kilómetros), donde se identificó un valor mínimo erróneo (-64.0), que deberá ser corregido para asegurar la integridad de los datos.

### 2. 🕳️ Estrategias de Manejo de Valores Nulos

Se implementó una estrategia dual para abordar los valores nulos, basada en el porcentaje de datos faltantes en cada columna:

* **Eliminación de Filas (<1% Nulos):** Para columnas con menos del 1% de valores nulos (como `precio`, `tipo_gasolina`, `volante_regulable`, `modelo`, `camara_trasera`, `elevalunas_electrico`, `km`, `potencia`, `fecha_venta`), se optó por eliminar las filas correspondientes, ya que la pérdida de información es mínima y no compromete la calidad del dataset.
* **Imputación de Valores (>=1% Nulos):** Para columnas con un porcentaje de nulos igual o superior al 1% (como `asientos_traseros_plegables` (70%), `fecha_registro` (50%), `tipo_coche`, `marca`, `alerta_lim_velocidad`, `bluetooth`, `aire_acondicionado`, `color`), se aplicaron técnicas de imputación. La elección del método (ej. moda para categóricas, media/mediana para numéricas) se basó en el tipo de dato y la distribución de la columna para preservar la información relevante. *[Nota: El notebook debe detallar los métodos de imputación específicos aplicados a cada columna y su justificación.]*

### 3. 📊 Análisis Exploratorio de Datos (EDA)

* **Análisis Univariable:** Se exploró cada variable de forma individual para entender sus distribuciones, rangos y características. Se realizaron estadísticas descriptivas (`.describe()`) para variables numéricas y análisis de frecuencia para categóricas, como la distribución de `modelo` que reveló una predominancia del "modelo 320".
* **Análisis de Correlación Inicial:** Se realizó una evaluación de las relaciones entre las variables numéricas para identificar posibles correlaciones. *[Nota: Este paso debería incluir una matriz de correlación o un mapa de calor para las variables numéricas antes de las transformaciones.]*
* **Análisis Variable vs. Target (`precio`):** Se investigó cómo cada variable se relaciona con la variable objetivo `precio`. Este análisis es crucial para identificar características con un alto impacto en el precio del vehículo. *[Nota: Se recomienda incluir visualizaciones (scatter plots para numéricas vs. target, box plots para categóricas vs. target) para respaldar estos insights.]*

### 4. 🔄 Transformación y Escalamiento de Datos

* **Codificación de Variables Categóricas:** Las variables categóricas identificadas se transformaron en representaciones numéricas utilizando técnicas como `LabelEncoder` u `OrdinalEncoder`, o `One-Hot Encoding` donde no existía un orden intrínseco. *[Nota: El notebook debe especificar qué variables se codificaron y con qué técnica, justificando la elección.]*
* **Escalado de Variables Numéricas:** Se aplicó `MinMaxScaler` a las variables numéricas para normalizar su rango entre 0 y 1. Esto es fundamental para algoritmos de aprendizaje automático sensibles a la escala de las características.
* **Análisis de Correlación Final:** Tras el escalado, se realizó un nuevo análisis de correlación para observar cómo las transformaciones afectaron las relaciones entre las variables, incluyendo las recién codificadas. *[Nota: Se debe presentar una matriz de correlación final para todas las variables numéricas resultantes.]*

### 5. 📦 Entrega del Dataset Final

* **Generación del Dataset Final (`vfin`):** Se consolidaron todas las transformaciones y limpiezas en un dataframe final llamado `vfin`.
* **Documentación de Estructura:** Se proporcionó un pantallazo de `vfin.info()` para visualizar todas las columnas y sus tipos de datos, asegurando la trazabilidad del proceso.
* **Exportación de Muestra:** Se generó un archivo Excel (`output.xlsx`) con las primeras 50 filas del dataset `vfin`, ofreciendo una muestra del conjunto de datos procesado.
* **Código Fuente:** Se entregó el notebook `.ipynb` con todo el proceso de preparación de datos documentado y ejecutable.

---

## 🛠️ Herramientas y Tecnologías Utilizadas

* **Lenguaje de Programación:** Python
* **Bibliotecas Clave:**
    * `pandas`: Indispensable para la manipulación y análisis de datos.
    * `numpy`: Para operaciones numéricas eficientes.
    * `matplotlib` y `seaborn`: Utilizadas para la visualización de datos y la generación de gráficos explicativos.
    * `scikit-learn`: Para tareas de preprocesamiento, incluyendo la codificación de variables categóricas (`LabelEncoder`, `OrdinalEncoder`) y el escalado de características (`MinMaxScaler`).

---

## 📬 Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactar:

* **Autor Principal:** David Larré
* **GitHub:** [@davidlarre](https://github.com/davidlarre)

---
