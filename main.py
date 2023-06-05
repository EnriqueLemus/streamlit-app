
import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go


st.title("Reto Ivan Preeliminar")
st.header("ITD Equipazo")

col16, col17, col18, col19 = st.columns(4)

col17.caption('Enrique Lemus')
col17.caption('Javier Morales')
col18.caption('Jessica Vazquez')
col18.caption('Sebastian Escobedo')

st.write("### Datos Trafico")
st.write("A continuación, se presentan las primeras filas del dataframe a manera de poder conocer las columnas que lo componen y los distintos datos que contienen")
# data will be in cache
@st.cache
def get_data():
    return pd.read_csv('base.csv')
df = pd.read_csv('base.csv') #get_data()
st.dataframe(df.head())

df.isna().sum()

#Five Number Summary
st.header("Five Number Summary")
st.write("Debajo se presenta un *Five Number Analisis* de los datos numéricos del Dataframe.")
st.write(" Se compone de un recuernto de todos los valores que hay en una determinada columna, eñ promedio de estos, la desviación estandar, el valor mínimo y el máximo asi como los Cuartiles del 25%, 50% y 75%")
five = df.describe()

st.write(five)
st.write("A continuación se presentan los Five Number Analisis de las columnas con valores numéricos que podrían ser más valiosas por ahora")

col1, col2, col3 = st.columns(3)
anio5 = df.anio.describe()

col1.subheader("Año")
col1.write(anio5)

dia5 = df.dia.describe()
col2.subheader("Dia del mes")
col2.write(dia5)

num_mes5 = df.num_mes.describe()
col3.subheader("Mes del año")
col3.write(num_mes5)

## Box plot
st.write("De la misma manera, se presentan los respectivos Boxplot (Cajas y bigotes) de los valores anteriormente mencionados")
col4, col5, col6 = st.columns([1,1,1])

col4.write("### Boxplot de año")
fig = px.box(df, y="anio",height=755, width=200)
col4.plotly_chart(fig)

col5.write("### Boxplot de Dia del mes")
fig = px.box(df, y="dia", height=700, width=200)
col5.plotly_chart(fig)

col6.write("### Boxplot de Mes del año")
fig = px.box(df, y="num_mes", height=750, width=200)
col6.plotly_chart(fig)




# HistPlot DistPlot
#(Skewness y Kurtosis)
st.write("## Analisis de distribuciones")

st.subheader("Skewness y Kurtosis de los Datos")
st.write("Aquí se presentan 2 tablas distintas, una para el valor de Skewness de cada columna numérica del dataframe y otra para lso valores de Kurtosis")
st.write("*Skewness* indica la tendencia u orientación de la distribución de la curva. Un valor de Skewness de o cercano a 0 corresponde a una distribución normal. Por otra parte, un valor menor a 0 resulta en un skewness positivo, una distribución cargada a la izquierda. Un valor de Skewness mayor a 1, indica un Skewness negativo, es decir una distribución cargada a la derecha.")
st.write("*Kurtosis* representa qué tan 'puntiaguda' es la distribución. Un valor alto de Kurtosis imdica una mayor concentración de valores en el promedio (punta) de la distribución. Un valor de 0 o muy cercano, supone una distribuión normal, un calor mayor a 0 es una distribución muy puntiaguda, mientras que un valor menor a 0 es una distribución muy plana/alargada")


skewnessdf = df.skew()
kurtosisdf = df.kurt() 
col20, col21, col22, col23 = st.columns(4)

col21.write(skewnessdf.to_frame().rename(columns={0: "Skewness"}), unsafe_allow_html=True)
col22.write(kurtosisdf.to_frame().rename(columns={0: "Kurtosis"}), unsafe_allow_html=True)


#Distribución de años
st.write("### ")
st.write("### Distribución de los Años")
st.write("##### A continuación se muestra una curva de densidad y un histograma de los accidentes del 2015 al 2021")
st.write(" Si deseas cambiar los años mostrados en el histograma, por favor, ajusta lso parámetros en el slider de *'Años'* en el menu sidebar")
skewness_anio = df.anio.skew()
kurtosis_anio = df.anio.kurt()
col7, col8, col9= st.columns(3)

#Kde
fig, ax = plt.subplots(figsize = (5,5))
sns.kdeplot(data=df, x="anio", ax=ax)
ax.set_xlabel("Año")
ax.set_ylabel("Densidad")
ax.grid(True)
col7.plotly_chart(fig)

#Histograma
values = st.sidebar.slider("Años", int(df.anio.min()), int(df.anio.max()), (int(df.anio.min()), int(df.anio.max())), step=1)
filtered_df = df[(df['anio'] >= values[0]) & (df['anio'] <= values[1])]
hist = px.histogram(filtered_df, x="anio", nbins=7)
hist.update_traces(marker_line_width=2, marker_line_color='black')
hist.update_xaxes(title="Años")
hist.update_yaxes(title="Número de Accidentes")
fig1 = go.Figure(data=hist)
fig1.update_layout(width=500, height=525)
col9.plotly_chart(fig1)

#Skewness y Kurtosis de Años
st.write("El valor de skewness para Anio es: %.2f" % skewness_anio)
st.write("El valor de kurtosis para Anio es: %.2f" % kurtosis_anio)


#Distribución de meses
st.write("### ")
st.write("### Distribución de los Meses")
st.write("##### A continuación se muestra una curva de densidad y un histograma de los accidentes de los meses del 2015 al los del 2021")
st.write(" Si deseas cambiar los años mostrados en el histograma, por favor, ajusta lso parámetros en el slider de *'Meses del año'* en el menu sidebar")

skewness_mes = df.num_mes.skew()
kurtosis_mes = df.num_mes.kurt()
col10, col11, col12= st.columns(3)

#Kde
fig2, ax2 = plt.subplots(figsize = (5,5))
sns.kdeplot(data=df, x="num_mes", ax=ax2)
ax2.set_xlabel("Mes del año")
ax2.set_ylabel("Densidad")
ax2.grid(True)
col10.plotly_chart(fig2)

#Histograma
values2 = st.sidebar.slider("Meses del año", int(df.num_mes.min()), int(df.num_mes.max()), (int(df.num_mes.min()), int(df.num_mes.max())), step=1)
filtered_df2 = df[(df['num_mes'] >= values2[0]) & (df['num_mes'] <= values2[1])]
hist2 = px.histogram(filtered_df2, x="num_mes", nbins=12)
hist2.update_traces(marker_line_width=2, marker_line_color='black')
hist2.update_xaxes(title="Meses")
hist2.update_yaxes(title="Número de Accidentes")
fig3 = go.Figure(data=hist2)
fig3.update_layout(width=500, height=525)
col12.plotly_chart(fig3)

#Skewness y Kurtosis de Meses2
st.write("El valor de skewness para los meses del año es: %.2f" % skewness_mes)
st.write("El valor de kurtosis para los meses del año es: %.2f" % kurtosis_mes)


#Distribución de Días
st.write("### ")
st.write("### Distribución de los Días")
st.write("##### A continuación se muestra una curva de densidad y un histograma de los accidentes por día del 2015 al 2021")
st.write(" Si deseas cambiar los años mostrados en el histograma, por favor, ajusta loo parámetros en el slider de *'Días del mes'* en el menu sidebar")

col13, col14, col15= st.columns(3)

skewness_dia = df.dia.skew()
kurtosis_dia = df.dia.kurt()

#Kde
fig4, ax3 = plt.subplots(figsize = (5,5))
sns.kdeplot(data=df, x="dia", ax=ax3)
ax3.set_xlabel("dia")
ax3.set_ylabel("Densidad")
ax3.grid(True)
col13.plotly_chart(fig4)

#Histograma
values3 = st.sidebar.slider("Días del mes", int(df.dia.min()), int(df.dia.max()), (int(df.dia.min()), int(df.dia.max())), step=1)
filtered_df3 = df[(df['dia'] >= values3[0]) & (df['dia'] <= values3[1])]
hist3 = px.histogram(filtered_df2, x="dia", nbins=31)
hist3.update_traces(marker_line_width=2, marker_line_color='black')
hist3.update_xaxes(title="Dias")
hist3.update_yaxes(title="Número de Accidentes")
fig5 = go.Figure(data=hist3)
fig5.update_layout(width=500, height=525)
col15.plotly_chart(fig5)

st.write("El valor de skewness para los días es: %.2f" % skewness_dia)
st.write("El valor de kurtosis para los días es: %.2f" % kurtosis_dia)


#Visualización del Mapa de accidentes
st.header("Mapa de accidentes")
df = df.rename(columns={'y': 'LAT', 'x': 'LON'})
anios = df["anio"].unique()
meses = df["num_mes"].unique()
st.caption("### En el mapa podemos visualizar todos los accidentes registrados en parte de la ZMG")
st.caption("### Si deseas ver los accidentes de uno o más años o meses en particular, por favor, ajusta los filtros en el menú sidebar")
st.caption("Si no se selecciona un año(s) o mes(es) específico, lo que se presenta en el mapa son todos los accidentes regristrados del 2015 al 2021")

seleccion_anios = st.sidebar.multiselect("Selecciona uno o varios años", anios)
seleccion_meses = st.sidebar.multiselect("Selecciona uno o varios meses", meses)
filtered_df = df.copy()
if seleccion_anios:
    filtered_df = filtered_df[filtered_df["anio"].isin(seleccion_anios)]
if seleccion_meses:
    filtered_df = filtered_df[filtered_df["num_mes"].isin(seleccion_meses)]
st.map(filtered_df[["LAT", "LON"]].dropna(how="any"))


st.subheader("Análisis de Outliers")



#Outliers de num_mes

IQR = df.num_mes.quantile(0.75) - df.num_mes.quantile(0.25)

lower = df.num_mes.quantile(0.25) - 1.5 * IQR
upper = df.num_mes.quantile(0.75) + 1.5 * IQR

outliers = []

for x in df.num_mes:
    if x < lower or x > upper:
        outliers.append(x)


if len(outliers) > 0:
    st.write("Valores atípicos (outliers) en la columna 'num_mes':")
    st.table(outliers)
else:
    st.write("No se encontraron valores atípicos en la columna 'num_mes'.")
    


#Outliers de clave_mun

IQR = df.clave_mun.quantile(0.75) - df.clave_mun.quantile(0.25)

lower = df.clave_mun.quantile(0.25) - 1.5 * IQR
upper = df.clave_mun.quantile(0.75) + 1.5 * IQR

outliers = []

for x in df.clave_mun:
    if x < lower or x > upper:
        outliers.append(x)



if len(outliers) > 0:
    st.write("Valores atípicos (outliers) en la columna 'clave_mun':")
    st.table(outliers)
else:
    st.write("No se encontraron valores atípicos en la columna 'clave_mun'.")


# Definir los rangos de hora
rango_inicio = 8
rango_fin = 17

# Crear el diccionario de mapeo para los rangos de hora
rangos_hora = {}
for hora in range(rango_inicio, rango_fin+1):
    rango_texto = f"{hora:02d}:00 a {hora:02d}:59"
    rangos_hora[rango_texto] = hora

# Crear una nueva columna 'rango_hora_numerico' con los valores convertidos
df['rango_hora_numerico'] = df['rango_hora'].map(rangos_hora)

IQR = df.rango_hora_numerico.quantile(0.75) - df.rango_hora_numerico.quantile(0.25)
lower = df.rango_hora_numerico.quantile(0.25) - 1.5 * IQR
upper = df.rango_hora_numerico.quantile(0.75) + 1.5 * IQR

outliers = []

for x in df.rango_hora_numerico:
    if x < lower or x > upper:
        outliers.append(x)


if len(outliers) > 0:
    st.write("Valores atípicos (outliers) en la columna 'rango_hora_numerico':")
    st.table(outliers)
else:
    st.write("No se encontraron valores atípicos en la columna 'rango_hora_numerico'.")



st.subheader("Análisis de Correlaciones")

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)


#'''
#step 1 sort
#st.subheader("Sorting in tables")
#st.text("The top five of minimun of nights")
#st.write(df.query("minimum_nights>=0").sort_values("minimum_nights", ascending=False).head())

#step 3 - column filter
#st.subheader("Select a column to see")
#default_cols = ["name", "host_id", "price"]
#cols = st.multiselect("Columns", df.columns.tolist(), default=default_cols)
#st.dataframe(df[cols].head(10))

#step 4 -  Static grouping
#st.subheader("Avg minimum for a room type")
#st.table(df.groupby("room_type").minimum_nights.mean().reset_index().sort_values("minimum_nights", ascending=False))



#step 6 -   Radio buttons
#neighbourhood = st.radio("Neighbourhood", df.neighbourhood_group.unique())

#@st.cache
#def get_availability(neighbourhood):
 #   return df.query("""neighbourhood_group==@neighbourhood\
  #      and availability_365>0""").availability_365.describe(\
   #         percentiles=[.1, .25, .5, .75, .9, .99]).to_frame().T

#st.table(get_availability(neighbourhood))
#'''
