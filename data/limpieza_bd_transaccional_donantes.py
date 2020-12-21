#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


##########################################################################
########################Informe de contabilidad 2018######################
##########################################################################
df_2018 = pd.read_csv(
    './contabilidad/Auxiliar_Donantes_2018.csv')

# print(df_2018.isna().sum())

# borrar columna de cheque - borramos o no
df_2018.drop('num_che', axis=1, inplace=True)

# borrar tipo de documento 900, pues son documentos de correcciones a donación
index_names = df_2018[df_2018['tipo'] == 900].index
df_2018.drop(index_names, inplace=True)

#################################################################
# crear columnas para agrupar y categorizar los centros de costos
# y la columna de sucursales
#################################################################

# categorizar sucursales
# columna categorización de sucursales, basada en la columna cod_suc
conditions = [
    (df_2018['cod_suc'] == 0),
    (df_2018['cod_suc'] >= 5) & (df_2018['cod_suc'] <= 45),
    (df_2018['cod_suc'] == 50),
    (df_2018['cod_suc'] >= 55) & (df_2018['cod_suc'] <= 60),
    (df_2018['cod_suc'] >= 65) & (df_2018['cod_suc'] <= 80),
    (df_2018['cod_suc'] >= 85) & (df_2018['cod_suc'] <= 125),
    (df_2018['cod_suc'] >= 205) & (df_2018['cod_suc'] <= 360),
    (df_2018['cod_suc'] >= 380) & (df_2018['cod_suc'] <= 400),
]
values = [0, 1, 2, 1, 4, 1, 3, 5]

# create a new column. Asignar los valores dependiendo de las condiciones
df_2018['categoria_suc'] = np.select(conditions, values)


# categorizar centros de costos
# columna categorización de centros de costos, basada en la columna cod_cco
conditions = [
    (df_2018['cod_cco'] == 0),
    (df_2018['cod_cco'] == 20),
    (df_2018['cod_cco'] == 40),
    (df_2018['cod_cco'] == 50),
    (df_2018['cod_cco'] == 60),
    (df_2018['cod_cco'] >= 80) & (df_2018['cod_cco'] <= 100),
    (df_2018['cod_cco'] >= 120) & (df_2018['cod_cco'] <= 160),
    (df_2018['cod_cco'] >= 180) & (df_2018['cod_cco'] <= 200),
    (df_2018['cod_cco'] == 220),
    (df_2018['cod_cco'] == 240),
    (df_2018['cod_cco'] == 260),
    (df_2018['cod_cco'] >= 280) & (df_2018['cod_cco'] <= 320),
    (df_2018['cod_cco'] >= 340) & (df_2018['cod_cco'] <= 360),
    (df_2018['cod_cco'] >= 380) & (df_2018['cod_cco'] <= 480),
    (df_2018['cod_cco'] >= 500) & (df_2018['cod_cco'] <= 1100),
    (df_2018['cod_cco'] >= 1120) & (df_2018['cod_cco'] <= 1140),
    (df_2018['cod_cco'] >= 1160) & (df_2018['cod_cco'] <= 1200),
    (df_2018['cod_cco'] == 1220),
    (df_2018['cod_cco'] == 1240),
    (df_2018['cod_cco'] >= 1260) & (df_2018['cod_cco'] <= 1280),
    (df_2018['cod_cco'] == 1300),
    (df_2018['cod_cco'] == 1320),
    (df_2018['cod_cco'] >= 1340) & (df_2018['cod_cco'] <= 1360),
    (df_2018['cod_cco'] >= 1380) & (df_2018['cod_cco'] <= 1400),
    (df_2018['cod_cco'] == 1420),
    (df_2018['cod_cco'] == 1440),
    (df_2018['cod_cco'] == 1460),
    (df_2018['cod_cco'] == 1480),
    (df_2018['cod_cco'] >= 1500) & (df_2018['cod_cco'] <= 1560),
    (df_2018['cod_cco'] >= 1580) & (df_2018['cod_cco'] <= 1600),
    (df_2018['cod_cco'] >= 1620) & (df_2018['cod_cco'] <= 1680),
    (df_2018['cod_cco'] == 1700),
    (df_2018['cod_cco'] == 1720),
    (df_2018['cod_cco'] == 1740),
    (df_2018['cod_cco'] == 1760),
    (df_2018['cod_cco'] == 1780),
    (df_2018['cod_cco'] >= 1800) & (df_2018['cod_cco'] <= 1820),
    (df_2018['cod_cco'] == 1840),
    (df_2018['cod_cco'] == 1860),
    (df_2018['cod_cco'] == 1880),
    (df_2018['cod_cco'] == 1900),
    (df_2018['cod_cco'] >= 1920) & (df_2018['cod_cco'] <= 2120),
    (df_2018['cod_cco'] == 2140),
    (df_2018['cod_cco'] >= 2160) & (df_2018['cod_cco'] <= 2180),
    (df_2018['cod_cco'] >= 2200) & (df_2018['cod_cco'] <= 2220),
    (df_2018['cod_cco'] == 3005),
    (df_2018['cod_cco'] == 3010),
    (df_2018['cod_cco'] >= 3015) & (df_2018['cod_cco'] <= 3025),
    (df_2018['cod_cco'] >= 3030) & (df_2018['cod_cco'] <= 3045),
    (df_2018['cod_cco'] == 3050),
    (df_2018['cod_cco'] == 3055),
    (df_2018['cod_cco'] >= 3060) & (df_2018['cod_cco'] <= 3105),
    (df_2018['cod_cco'] >= 3110) & (df_2018['cod_cco'] <= 3115),
    (df_2018['cod_cco'] == 3120),
    (df_2018['cod_cco'] >= 3125) & (df_2018['cod_cco'] <= 3130),
    (df_2018['cod_cco'] == 3135),
    (df_2018['cod_cco'] == 3140),
    (df_2018['cod_cco'] == 4005),
    (df_2018['cod_cco'] >= 5005) & (df_2018['cod_cco'] <= 5035),
    (df_2018['cod_cco'] == 6005),
    (df_2018['cod_cco'] >= 6010) & (df_2018['cod_cco'] <= 6020),
    (df_2018['cod_cco'] >= 6025) & (df_2018['cod_cco'] <= 6065),
    (df_2018['cod_cco'] >= 6070) & (df_2018['cod_cco'] <= 6240),
    (df_2018['cod_cco'] == 7005),
    (df_2018['cod_cco'] == 7010),
    (df_2018['cod_cco'] == 7015),
    (df_2018['cod_cco'] == 7020),
    (df_2018['cod_cco'] == 7025),
]

values = [0, 21, 5, 1, 3, 22, 6, 23, 3, 7, 8, 4, 8, 6, 3, 6, 3, 6, 4,
          6, 3, 21, 22, 23, 6, 3, 6, 8, 4, 3, 6, 21, 23, 22, 23, 6, 22,
          6, 23, 22, 3, 8, 3, 22, 6, 21, 22, 9, 6, 9, 6, 8, 6, 8, 6,
          8, 23, 9, 8, 5, 4, 8, 3, 21, 22, 23, 8, 7]

# create a new column. Asignar los valores dependiendo de las condiciones
df_2018['categoria_cco'] = np.select(conditions, values)

###########################################################################
# Eliminar registros que no son donaciones en sí pero se contabilizan como tal

# número 3, categoría centro de costos: administración de terceros
index_names = df_2018[df_2018['categoria_cco'] == 3].index
df_2018.drop(index_names, inplace=True)

# número 5, categoría centro de costos: mensualidades de centros para impuestos y seguros
index_names = df_2018[df_2018['categoria_cco'] == 5].index
df_2018.drop(index_names, inplace=True)

# número 8, categoría sentro de costos: gastos
index_names = df_2018[df_2018['categoria_cco'] == 8].index
df_2018.drop(index_names, inplace=True)

# número 9, categoría sentro de costos: otros (gastos)
index_names = df_2018[df_2018['categoria_cco'] == 9].index
df_2018.drop(index_names, inplace=True)

# número 4, categoría sucursal: inmuebles que tiene la ACF
index_names = df_2018[df_2018['categoria_suc'] == 4].index
df_2018.drop(index_names, inplace=True)

# número 5, categoría sucursal: aliados de la ACF
index_names = df_2018[df_2018['categoria_suc'] == 5].index
df_2018.drop(index_names, inplace=True)

# eliminar des_mov anulados
index_names = df_2018[df_2018['des_mov'] == '-ANULADO-'].index
df_2018.drop(index_names, inplace=True)

##########################################
# canal usado para la donación
df_2018['canal'] = df_2018['des_mov'].str.split('-', expand=True)[0]
df_2018['canal'] = df_2018['canal'].str.split(' ', expand=True)[1]
# print(df_2018['canal'])

###########################################
# crear columna mes a partir de la columna periodo

conditions = [
    (df_2018['periodo'] == 1),
    (df_2018['periodo'] == 2),
    (df_2018['periodo'] == 3),
    (df_2018['periodo'] == 4),
    (df_2018['periodo'] == 5),
    (df_2018['periodo'] == 6),
    (df_2018['periodo'] == 7),
    (df_2018['periodo'] == 8),
    (df_2018['periodo'] == 9),
    (df_2018['periodo'] == 10),
    (df_2018['periodo'] == 11),
    (df_2018['periodo'] == 12),
]
values = ['enero', 'febrero', 'marzo', 'abril', 'mayo',
          'junio', 'julio', 'agosto', 'septiembre', 'octubre',
          'noviembre', 'diciembre']

# create a new column. Asignar los valores dependiendo de las condiciones
df_2018['mes'] = np.select(conditions, values)
# print(df_2018['mes'])

###########################################
# crear columna fuente de donación sa partir de categoria cco

conditions = [
    (df_2018['categoria_cco'] == 21),
    (df_2018['categoria_cco'] == 22),
    (df_2018['categoria_cco'] == 23),
    (df_2018['categoria_cco'] == 4),
    (df_2018['categoria_cco'] == 6)
]
values = ['D. Cooperadoras', 'D. Particulares', 'D. Empresas',
          'Mantenimineto Centros', 'Eventos, Actividades y Productos']

# create a new column. Asignar los valores dependiendo de las condiciones
df_2018['origen_donacion'] = np.select(conditions, values)

###########################################
# crear columna fuente de donación sa partir de categoria cco

conditions = [
    (df_2018['cod_suc'] == 0),
    (df_2018['cod_suc'] == 5),
    (df_2018['cod_suc'] == 10),
    (df_2018['cod_suc'] == 15),
    (df_2018['cod_suc'] == 20),
    (df_2018['cod_suc'] == 25),
    (df_2018['cod_suc'] == 30),
    (df_2018['cod_suc'] == 35),
    (df_2018['cod_suc'] == 40),
    (df_2018['cod_suc'] == 45),
    (df_2018['cod_suc'] == 50),
    (df_2018['cod_suc'] == 55),
    (df_2018['cod_suc'] == 60),
    (df_2018['cod_suc'] == 85),
    (df_2018['cod_suc'] == 90),
    (df_2018['cod_suc'] == 95),
    (df_2018['cod_suc'] == 100),
    (df_2018['cod_suc'] == 105),
    (df_2018['cod_suc'] == 110),
    (df_2018['cod_suc'] == 115),
    (df_2018['cod_suc'] == 120),
    (df_2018['cod_suc'] == 125),
    (df_2018['cod_suc'] == 205),
    (df_2018['cod_suc'] == 210),
    (df_2018['cod_suc'] == 215),
    (df_2018['cod_suc'] == 220),
    (df_2018['cod_suc'] == 225),
    (df_2018['cod_suc'] == 250),
    (df_2018['cod_suc'] == 300),
    (df_2018['cod_suc'] == 320),
    (df_2018['cod_suc'] == 340),
    (df_2018['cod_suc'] == 350),
    (df_2018['cod_suc'] == 360)
]
values = [
    "No Aplica", "Cedro",
    "Inaya", "Nogal", "Portones", "Torreon",
    "Yari", "Arboleda", "Cendal", "Ariza",
    "Entidad Gestora", "Narval", "Diagonal",
    "Nogal - Villavicencio", "Torreon - Curso Estudios",
    "El Cedro - Neiva", "Auxiliares Externas",
    "Belayes", "La Casona", "Mirabal", "Rocalla",
    "Serrania", "Icsef", "Colegio Integral Femenino",
    "Gimnasio Tundama", "Casanueva", "Fondo Sacerdotes",
    "Casanueva Admon", "Apartamiento 116",
    "Apoyo Venezuela", "Apoyo Familias Juventus",
    "Admon Terceros", "Mujeres Escasos Recursos"]
# create a new column. Asignar los valores dependiendo de las condiciones
df_2018['destino_donacion'] = np.select(conditions, values)

# print(df_2018.groupby(['categoria_suc']).first())

df_2018.to_csv('./contabilidad_limpios/Auxiliar_Donantes_2018.csv',
               index=False, encoding='utf-8')
print(df_2018.head())
print(df_2018.columns.values)
# print(len(df_2018.index))


##########################################################################
########################Informe de contabilidad 2019######################
##########################################################################
df_2019 = pd.read_csv(
    './contabilidad/Auxiliar_Donantes_2019.csv')
# print(df_2019.isna().sum())

# borrar columna de cheque - borramos o no
df_2019.drop('num_che', axis=1, inplace=True)

# borrar tipo de documento 900, pues son documentos de correcciones a donación
index_names = df_2019[df_2019['tipo'] == 900].index
df_2019.drop(index_names, inplace=True)

#################################################################
# crear columnas para agrupar y categorizar los centros de costos
# y la columna de sucursales
#################################################################

# categorizar sucursales
# columna categorización de sucursales, basada en la columna cod_suc
conditions = [
    (df_2019['cod_suc'] == 0),
    (df_2019['cod_suc'] >= 5) & (df_2019['cod_suc'] <= 45),
    (df_2019['cod_suc'] == 50),
    (df_2019['cod_suc'] >= 55) & (df_2019['cod_suc'] <= 60),
    (df_2019['cod_suc'] >= 65) & (df_2019['cod_suc'] <= 80),
    (df_2019['cod_suc'] >= 85) & (df_2019['cod_suc'] <= 125),
    (df_2019['cod_suc'] >= 205) & (df_2019['cod_suc'] <= 360),
    (df_2019['cod_suc'] >= 380) & (df_2019['cod_suc'] <= 400),
]
values = [0, 1, 2, 1, 4, 1, 3, 5]

# create a new column. Asignar los valores dependiendo de las condiciones
df_2019['categoria_suc'] = np.select(conditions, values)


# categorizar centros de costos
# columna categorización de centros de costos, basada en la columna cod_cco
conditions = [
    (df_2019['cod_cco'] == 0),
    (df_2019['cod_cco'] == 20),
    (df_2019['cod_cco'] == 40),
    (df_2019['cod_cco'] == 50),
    (df_2019['cod_cco'] == 60),
    (df_2019['cod_cco'] >= 80) & (df_2019['cod_cco'] <= 100),
    (df_2019['cod_cco'] >= 120) & (df_2019['cod_cco'] <= 160),
    (df_2019['cod_cco'] >= 180) & (df_2019['cod_cco'] <= 200),
    (df_2019['cod_cco'] == 220),
    (df_2019['cod_cco'] == 240),
    (df_2019['cod_cco'] == 260),
    (df_2019['cod_cco'] >= 280) & (df_2019['cod_cco'] <= 320),
    (df_2019['cod_cco'] >= 340) & (df_2019['cod_cco'] <= 360),
    (df_2019['cod_cco'] >= 380) & (df_2019['cod_cco'] <= 480),
    (df_2019['cod_cco'] >= 500) & (df_2019['cod_cco'] <= 1100),
    (df_2019['cod_cco'] >= 1120) & (df_2019['cod_cco'] <= 1140),
    (df_2019['cod_cco'] >= 1160) & (df_2019['cod_cco'] <= 1200),
    (df_2019['cod_cco'] == 1220),
    (df_2019['cod_cco'] == 1240),
    (df_2019['cod_cco'] >= 1260) & (df_2019['cod_cco'] <= 1280),
    (df_2019['cod_cco'] == 1300),
    (df_2019['cod_cco'] == 1320),
    (df_2019['cod_cco'] >= 1340) & (df_2019['cod_cco'] <= 1360),
    (df_2019['cod_cco'] >= 1380) & (df_2019['cod_cco'] <= 1400),
    (df_2019['cod_cco'] == 1420),
    (df_2019['cod_cco'] == 1440),
    (df_2019['cod_cco'] == 1460),
    (df_2019['cod_cco'] == 1480),
    (df_2019['cod_cco'] >= 1500) & (df_2019['cod_cco'] <= 1560),
    (df_2019['cod_cco'] >= 1580) & (df_2019['cod_cco'] <= 1600),
    (df_2019['cod_cco'] >= 1620) & (df_2019['cod_cco'] <= 1680),
    (df_2019['cod_cco'] == 1700),
    (df_2019['cod_cco'] == 1720),
    (df_2019['cod_cco'] == 1740),
    (df_2019['cod_cco'] == 1760),
    (df_2019['cod_cco'] == 1780),
    (df_2019['cod_cco'] >= 1800) & (df_2019['cod_cco'] <= 1820),
    (df_2019['cod_cco'] == 1840),
    (df_2019['cod_cco'] == 1860),
    (df_2019['cod_cco'] == 1880),
    (df_2019['cod_cco'] == 1900),
    (df_2019['cod_cco'] >= 1920) & (df_2019['cod_cco'] <= 2120),
    (df_2019['cod_cco'] == 2140),
    (df_2019['cod_cco'] >= 2160) & (df_2019['cod_cco'] <= 2180),
    (df_2019['cod_cco'] >= 2200) & (df_2019['cod_cco'] <= 2220),
    (df_2019['cod_cco'] == 3005),
    (df_2019['cod_cco'] == 3010),
    (df_2019['cod_cco'] >= 3015) & (df_2019['cod_cco'] <= 3025),
    (df_2019['cod_cco'] >= 3030) & (df_2019['cod_cco'] <= 3045),
    (df_2019['cod_cco'] == 3050),
    (df_2019['cod_cco'] == 3055),
    (df_2019['cod_cco'] >= 3060) & (df_2019['cod_cco'] <= 3105),
    (df_2019['cod_cco'] >= 3110) & (df_2019['cod_cco'] <= 3115),
    (df_2019['cod_cco'] == 3120),
    (df_2019['cod_cco'] >= 3125) & (df_2019['cod_cco'] <= 3130),
    (df_2019['cod_cco'] == 3135),
    (df_2019['cod_cco'] == 3140),
    (df_2019['cod_cco'] == 4005),
    (df_2019['cod_cco'] >= 5005) & (df_2019['cod_cco'] <= 5035),
    (df_2019['cod_cco'] == 6005),
    (df_2019['cod_cco'] >= 6010) & (df_2019['cod_cco'] <= 6020),
    (df_2019['cod_cco'] >= 6025) & (df_2019['cod_cco'] <= 6065),
    (df_2019['cod_cco'] >= 6070) & (df_2019['cod_cco'] <= 6240),
    (df_2019['cod_cco'] == 7005),
    (df_2019['cod_cco'] == 7010),
    (df_2019['cod_cco'] == 7015),
    (df_2019['cod_cco'] == 7020),
    (df_2019['cod_cco'] == 7025),
]

values = [0, 21, 5, 1, 3, 22, 6, 23, 3, 7, 8, 4, 8, 6, 3, 6, 3, 6, 4,
          6, 3, 21, 22, 23, 6, 3, 6, 8, 4, 3, 6, 21, 23, 22, 23, 6, 22,
          6, 23, 22, 3, 8, 3, 22, 6, 21, 22, 9, 6, 9, 6, 8, 6, 8, 6,
          8, 23, 9, 8, 5, 4, 8, 3, 21, 22, 23, 8, 7]

# create a new column. Asignar los valores dependiendo de las condiciones
df_2019['categoria_cco'] = np.select(conditions, values)


###########################################################################
# Eliminar registros que no son donaciones en sí pero se contabilizan como tal

# número 3, categoría centro de costos: administración de terceros
index_names = df_2019[df_2019['categoria_cco'] == 3].index
df_2019.drop(index_names, inplace=True)

# número 5, categoría centro de costos: mensualidades de centros para impuestos y seguros
index_names = df_2019[df_2019['categoria_cco'] == 5].index
df_2019.drop(index_names, inplace=True)

# número 8, categoría sentro de costos: gastos
index_names = df_2019[df_2019['categoria_cco'] == 8].index
df_2019.drop(index_names, inplace=True)

# número 9, categoría sentro de costos: otros (gastos)
index_names = df_2019[df_2019['categoria_cco'] == 9].index
df_2019.drop(index_names, inplace=True)

# número 4, categoría sucursal: inmuebles que tiene la ACF
index_names = df_2019[df_2019['categoria_suc'] == 4].index
df_2019.drop(index_names, inplace=True)

# número 5, categoría sucursal: aliados de la ACF
index_names = df_2019[df_2019['categoria_suc'] == 5].index
df_2019.drop(index_names, inplace=True)

# eliminar des_mov anulados
index_names = df_2019[df_2019['des_mov'] == '-ANULADO-'].index
df_2019.drop(index_names, inplace=True)

# print(df_2019.groupby(['categoria_suc']).first())

##########################################
# canal usado para la donación
df_2019['canal'] = df_2019['des_mov'].str.split('-', expand=True)[0]
df_2019['canal'] = df_2019['canal'].str.split(' ', expand=True)[1]
# print(df_2018['canal'])

###########################################
# crear columna mes a partir de la columna periodo

conditions = [
    (df_2019['periodo'] == 1),
    (df_2019['periodo'] == 2),
    (df_2019['periodo'] == 3),
    (df_2019['periodo'] == 4),
    (df_2019['periodo'] == 5),
    (df_2019['periodo'] == 6),
    (df_2019['periodo'] == 7),
    (df_2019['periodo'] == 8),
    (df_2019['periodo'] == 9),
    (df_2019['periodo'] == 10),
    (df_2019['periodo'] == 11),
    (df_2019['periodo'] == 12),
]
values = ['enero', 'febrero', 'marzo', 'abril', 'mayo',
          'junio', 'julio', 'agosto', 'septiembre', 'octubre',
          'noviembre', 'diciembre']

# create a new column. Asignar los valores dependiendo de las condiciones
df_2019['mes'] = np.select(conditions, values)
# print(df_2018['mes'])

###########################################
# crear columna fuente de donación sa partir de categoria cco

conditions = [
    (df_2019['categoria_cco'] == 21),
    (df_2019['categoria_cco'] == 22),
    (df_2019['categoria_cco'] == 23),
    (df_2019['categoria_cco'] == 4),
    (df_2019['categoria_cco'] == 6)
]
values = ['D. Cooperadoras', 'D. Particulares', 'D. Empresas',
          'Mantenimineto Centros', 'Eventos, Actividades y Productos']

# create a new column. Asignar los valores dependiendo de las condiciones
df_2019['origen_donacion'] = np.select(conditions, values)

###########################################
# crear columna fuente de donación sa partir de categoria cco

conditions = [
    (df_2019['cod_suc'] == 0),
    (df_2019['cod_suc'] == 5),
    (df_2019['cod_suc'] == 10),
    (df_2019['cod_suc'] == 15),
    (df_2019['cod_suc'] == 20),
    (df_2019['cod_suc'] == 25),
    (df_2019['cod_suc'] == 30),
    (df_2019['cod_suc'] == 35),
    (df_2019['cod_suc'] == 40),
    (df_2019['cod_suc'] == 45),
    (df_2019['cod_suc'] == 50),
    (df_2019['cod_suc'] == 55),
    (df_2019['cod_suc'] == 60),
    (df_2019['cod_suc'] == 85),
    (df_2019['cod_suc'] == 90),
    (df_2019['cod_suc'] == 95),
    (df_2019['cod_suc'] == 100),
    (df_2019['cod_suc'] == 105),
    (df_2019['cod_suc'] == 110),
    (df_2019['cod_suc'] == 115),
    (df_2019['cod_suc'] == 120),
    (df_2019['cod_suc'] == 125),
    (df_2019['cod_suc'] == 205),
    (df_2019['cod_suc'] == 210),
    (df_2019['cod_suc'] == 215),
    (df_2019['cod_suc'] == 220),
    (df_2019['cod_suc'] == 225),
    (df_2019['cod_suc'] == 250),
    (df_2019['cod_suc'] == 300),
    (df_2019['cod_suc'] == 320),
    (df_2019['cod_suc'] == 340),
    (df_2019['cod_suc'] == 350),
    (df_2019['cod_suc'] == 360)
]
values = [
    "No Aplica", "Cedro",
    "Inaya", "Nogal", "Portones", "Torreon",
    "Yari", "Arboleda", "Cendal", "Ariza",
    "Entidad Gestora", "Narval", "Diagonal",
    "Nogal - Villavicencio", "Torreon - Curso Estudios",
    "El Cedro - Neiva", "Auxiliares Externas",
    "Belayes", "La Casona", "Mirabal", "Rocalla",
    "Serrania", "Icsef", "Colegio Integral Femenino",
    "Gimnasio Tundama", "Casanueva", "Fondo Sacerdotes",
    "Casanueva Admon", "Apartamiento 116",
    "Apoyo Venezuela", "Apoyo Familias Juventus",
    "Admon Terceros", "Mujeres Escasos Recursos"]
# create a new column. Asignar los valores dependiendo de las condiciones
df_2019['destino_donacion'] = np.select(conditions, values)

df_2019.to_csv('./contabilidad_limpios/Auxiliar_Donantes_2019.csv',
               index=False, encoding='utf-8')
print(df_2019.head())
print(len(df_2019.index))


##########################################################################
########################Informe de contabilidad 2020######################
##########################################################################
df_2020 = pd.read_csv(
    './contabilidad/Auxiliar_Donantes_2020.csv')

# print(df_2020.isna().sum())

# borrar columna de cheque - borramos o no
df_2020.drop('num_che', axis=1, inplace=True)

# borrar tipo de documento 900, pues son documentos de correcciones a donación
index_names = df_2020[df_2020['tipo'] == 900].index
df_2020.drop(index_names, inplace=True)

#################################################################
# crear columnas para agrupar y categorizar los centros de costos
# y la columna de sucursales
#################################################################

# categorizar sucursales
# columna categorización de sucursales, basada en la columna cod_suc
conditions = [
    (df_2020['cod_suc'] == 0),
    (df_2020['cod_suc'] >= 5) & (df_2020['cod_suc'] <= 45),
    (df_2020['cod_suc'] == 50),
    (df_2020['cod_suc'] >= 55) & (df_2020['cod_suc'] <= 60),
    (df_2020['cod_suc'] >= 65) & (df_2020['cod_suc'] <= 80),
    (df_2020['cod_suc'] >= 85) & (df_2020['cod_suc'] <= 125),
    (df_2020['cod_suc'] >= 205) & (df_2020['cod_suc'] <= 360),
    (df_2020['cod_suc'] >= 380) & (df_2020['cod_suc'] <= 400),
]
values = [0, 1, 2, 1, 4, 1, 3, 5]

# create a new column. Asignar los valores dependiendo de las condiciones
df_2020['categoria_suc'] = np.select(conditions, values)


# categorizar centros de costos
# columna categorización de centros de costos, basada en la columna cod_cco
conditions = [
    (df_2020['cod_cco'] == 0),
    (df_2020['cod_cco'] == 20),
    (df_2020['cod_cco'] == 40),
    (df_2020['cod_cco'] == 50),
    (df_2020['cod_cco'] == 60),
    (df_2020['cod_cco'] >= 80) & (df_2020['cod_cco'] <= 100),
    (df_2020['cod_cco'] >= 120) & (df_2020['cod_cco'] <= 160),
    (df_2020['cod_cco'] >= 180) & (df_2020['cod_cco'] <= 200),
    (df_2020['cod_cco'] == 220),
    (df_2020['cod_cco'] == 240),
    (df_2020['cod_cco'] == 260),
    (df_2020['cod_cco'] >= 280) & (df_2020['cod_cco'] <= 320),
    (df_2020['cod_cco'] >= 340) & (df_2020['cod_cco'] <= 360),
    (df_2020['cod_cco'] >= 380) & (df_2020['cod_cco'] <= 480),
    (df_2020['cod_cco'] >= 500) & (df_2020['cod_cco'] <= 1100),
    (df_2020['cod_cco'] >= 1120) & (df_2020['cod_cco'] <= 1140),
    (df_2020['cod_cco'] >= 1160) & (df_2020['cod_cco'] <= 1200),
    (df_2020['cod_cco'] == 1220),
    (df_2020['cod_cco'] == 1240),
    (df_2020['cod_cco'] >= 1260) & (df_2020['cod_cco'] <= 1280),
    (df_2020['cod_cco'] == 1300),
    (df_2020['cod_cco'] == 1320),
    (df_2020['cod_cco'] >= 1340) & (df_2020['cod_cco'] <= 1360),
    (df_2020['cod_cco'] >= 1380) & (df_2020['cod_cco'] <= 1400),
    (df_2020['cod_cco'] == 1420),
    (df_2020['cod_cco'] == 1440),
    (df_2020['cod_cco'] == 1460),
    (df_2020['cod_cco'] == 1480),
    (df_2020['cod_cco'] >= 1500) & (df_2020['cod_cco'] <= 1560),
    (df_2020['cod_cco'] >= 1580) & (df_2020['cod_cco'] <= 1600),
    (df_2020['cod_cco'] >= 1620) & (df_2020['cod_cco'] <= 1680),
    (df_2020['cod_cco'] == 1700),
    (df_2020['cod_cco'] == 1720),
    (df_2020['cod_cco'] == 1740),
    (df_2020['cod_cco'] == 1760),
    (df_2020['cod_cco'] == 1780),
    (df_2020['cod_cco'] >= 1800) & (df_2020['cod_cco'] <= 1820),
    (df_2020['cod_cco'] == 1840),
    (df_2020['cod_cco'] == 1860),
    (df_2020['cod_cco'] == 1880),
    (df_2020['cod_cco'] == 1900),
    (df_2020['cod_cco'] >= 1920) & (df_2020['cod_cco'] <= 2120),
    (df_2020['cod_cco'] == 2140),
    (df_2020['cod_cco'] >= 2160) & (df_2020['cod_cco'] <= 2180),
    (df_2020['cod_cco'] >= 2200) & (df_2020['cod_cco'] <= 2220),
    (df_2020['cod_cco'] == 3005),
    (df_2020['cod_cco'] == 3010),
    (df_2020['cod_cco'] >= 3015) & (df_2020['cod_cco'] <= 3025),
    (df_2020['cod_cco'] >= 3030) & (df_2020['cod_cco'] <= 3045),
    (df_2020['cod_cco'] == 3050),
    (df_2020['cod_cco'] == 3055),
    (df_2020['cod_cco'] >= 3060) & (df_2020['cod_cco'] <= 3105),
    (df_2020['cod_cco'] >= 3110) & (df_2020['cod_cco'] <= 3115),
    (df_2020['cod_cco'] == 3120),
    (df_2020['cod_cco'] >= 3125) & (df_2020['cod_cco'] <= 3130),
    (df_2020['cod_cco'] == 3135),
    (df_2020['cod_cco'] == 3140),
    (df_2020['cod_cco'] == 4005),
    (df_2020['cod_cco'] >= 5005) & (df_2020['cod_cco'] <= 5035),
    (df_2020['cod_cco'] == 6005),
    (df_2020['cod_cco'] >= 6010) & (df_2020['cod_cco'] <= 6020),
    (df_2020['cod_cco'] >= 6025) & (df_2020['cod_cco'] <= 6065),
    (df_2020['cod_cco'] >= 6070) & (df_2020['cod_cco'] <= 6240),
    (df_2020['cod_cco'] == 7005),
    (df_2020['cod_cco'] == 7010),
    (df_2020['cod_cco'] == 7015),
    (df_2020['cod_cco'] == 7020),
    (df_2020['cod_cco'] == 7025),
]

values = [0, 21, 5, 1, 3, 22, 6, 23, 3, 7, 8, 4, 8, 6, 3, 6, 3, 6, 4,
          6, 3, 21, 22, 23, 6, 3, 6, 8, 4, 3, 6, 21, 23, 22, 23, 6, 22,
          6, 23, 22, 3, 8, 3, 22, 6, 21, 22, 9, 6, 9, 6, 8, 6, 8, 6,
          8, 23, 9, 8, 5, 4, 8, 3, 21, 22, 23, 8, 7]

# create a new column. Asignar los valores dependiendo de las condiciones
df_2020['categoria_cco'] = np.select(conditions, values)


###########################################################################
# Eliminar registros que no son donaciones en sí pero se contabilizan como tal

# número 3, categoría centro de costos: administración de terceros
index_names = df_2020[df_2020['categoria_cco'] == 3].index
df_2020.drop(index_names, inplace=True)

# número 5, categoría centro de costos: mensualidades de centros para impuestos y seguros
index_names = df_2020[df_2020['categoria_cco'] == 5].index
df_2020.drop(index_names, inplace=True)

# número 8, categoría sentro de costos: gastos
index_names = df_2020[df_2020['categoria_cco'] == 8].index
df_2020.drop(index_names, inplace=True)

# número 9, categoría sentro de costos: otros (gastos)
index_names = df_2020[df_2020['categoria_cco'] == 9].index
df_2020.drop(index_names, inplace=True)

# número 4, categoría sucursal: inmuebles que tiene la ACF
index_names = df_2020[df_2020['categoria_suc'] == 4].index
df_2020.drop(index_names, inplace=True)

# número 5, categoría sucursal: aliados de la ACF
index_names = df_2020[df_2020['categoria_suc'] == 5].index
df_2020.drop(index_names, inplace=True)

# eliminar des_mov anulados
index_names = df_2020[df_2020['des_mov'] == '-ANULADO-'].index
df_2020.drop(index_names, inplace=True)

# print(df_2020.groupby(['categoria_suc']).first())

##########################################
# canal usado para la donación
df_2020['canal'] = df_2020['des_mov'].str.split('-', expand=True)[0]
df_2020['canal'] = df_2020['canal'].str.split(' ', expand=True)[1]
# print(df_2020['canal'])

###########################################
# crear columna mes a partir de la columna periodo

conditions = [
    (df_2020['periodo'] == 1),
    (df_2020['periodo'] == 2),
    (df_2020['periodo'] == 3),
    (df_2020['periodo'] == 4),
    (df_2020['periodo'] == 5),
    (df_2020['periodo'] == 6),
    (df_2020['periodo'] == 7),
    (df_2020['periodo'] == 8),
    (df_2020['periodo'] == 9),
    (df_2020['periodo'] == 10),
    (df_2020['periodo'] == 11),
    (df_2020['periodo'] == 12),
]
values = ['enero', 'febrero', 'marzo', 'abril', 'mayo',
          'junio', 'julio', 'agosto', 'septiembre', 'octubre',
          'noviembre', 'diciembre']

# create a new column. Asignar los valores dependiendo de las condiciones
df_2020['mes'] = np.select(conditions, values)
# print(df_2020['mes'])

###########################################
# crear columna fuente de donación sa partir de categoria cco

conditions = [
    (df_2020['categoria_cco'] == 21),
    (df_2020['categoria_cco'] == 22),
    (df_2020['categoria_cco'] == 23),
    (df_2020['categoria_cco'] == 4),
    (df_2020['categoria_cco'] == 6)
]
values = ['D. Cooperadoras', 'D. Particulares', 'D. Empresas',
          'Mantenimineto Centros', 'Eventos, Actividades y Productos']

# create a new column. Asignar los valores dependiendo de las condiciones
df_2020['origen_donacion'] = np.select(conditions, values)

###########################################
# crear columna fuente de donación sa partir de categoria cco

conditions = [
    (df_2020['cod_suc'] == 0),
    (df_2020['cod_suc'] == 5),
    (df_2020['cod_suc'] == 10),
    (df_2020['cod_suc'] == 15),
    (df_2020['cod_suc'] == 20),
    (df_2020['cod_suc'] == 25),
    (df_2020['cod_suc'] == 30),
    (df_2020['cod_suc'] == 35),
    (df_2020['cod_suc'] == 40),
    (df_2020['cod_suc'] == 45),
    (df_2020['cod_suc'] == 50),
    (df_2020['cod_suc'] == 55),
    (df_2020['cod_suc'] == 60),
    (df_2020['cod_suc'] == 85),
    (df_2020['cod_suc'] == 90),
    (df_2020['cod_suc'] == 95),
    (df_2020['cod_suc'] == 100),
    (df_2020['cod_suc'] == 105),
    (df_2020['cod_suc'] == 110),
    (df_2020['cod_suc'] == 115),
    (df_2020['cod_suc'] == 120),
    (df_2020['cod_suc'] == 125),
    (df_2020['cod_suc'] == 205),
    (df_2020['cod_suc'] == 210),
    (df_2020['cod_suc'] == 215),
    (df_2020['cod_suc'] == 220),
    (df_2020['cod_suc'] == 225),
    (df_2020['cod_suc'] == 250),
    (df_2020['cod_suc'] == 300),
    (df_2020['cod_suc'] == 320),
    (df_2020['cod_suc'] == 340),
    (df_2020['cod_suc'] == 350),
    (df_2020['cod_suc'] == 360)
]
values = [
    "No Aplica", "Cedro",
    "Inaya", "Nogal", "Portones", "Torreon",
    "Yari", "Arboleda", "Cendal", "Ariza",
    "Entidad Gestora", "Narval", "Diagonal",
    "Nogal - Villavicencio", "Torreon - Curso Estudios",
    "El Cedro - Neiva", "Auxiliares Externas",
    "Belayes", "La Casona", "Mirabal", "Rocalla",
    "Serrania", "Icsef", "Colegio Integral Femenino",
    "Gimnasio Tundama", "Casanueva", "Fondo Sacerdotes",
    "Casanueva Admon", "Apartamiento 116",
    "Apoyo Venezuela", "Apoyo Familias Juventus",
    "Admon Terceros", "Mujeres Escasos Recursos"]
# create a new column. Asignar los valores dependiendo de las condiciones
df_2020['destino_donacion'] = np.select(conditions, values)

print(df_2020.tail())
print(len(df_2020.index))
print(df_2020.columns.values)

df_2020.to_csv('./contabilidad_limpios/Auxiliar_Donantes_2020.csv',
               index=False, encoding='utf-8')

###########################################################
# concat all the database
df_total = pd.concat([df_2018, df_2019, df_2020], ignore_index=True)
###########################################################
# eliminar a Limmat, casa atípico
index_names = df_total[df_total['cod_ter'] == 107300142].index
df_total.drop(index_names, inplace=True)
# eliminar donaciones de 0 pesos
index_names = df_total[df_total['cre_mov'] == 0].index
df_total.drop(index_names, inplace=True)

##############################################################
# columna rango de donacion
# cooperadoras
print("cooperadoras")
df1 = df_total.loc[df_total['categoria_cco'] == 21]
#minimo = df1['cre_mov'][df1['cre_mov'].ne(0)].min()
minimo = df1['cre_mov'].min()
maximo = df1['cre_mov'].max()
clases = (maximo - minimo) / 7
plt.hist(x=df1['cre_mov'], bins=30, color='#F2AB6D', rwidth=0.85)
plt.title('Histograma coop')
plt.xlabel('Total donación')
plt.ylabel('Frecuencia')
plt.show()
bins = [0, 450000, 900000, 1350000, 1800000, 2250000, 2700000, 3150000,
        3600000, 4050000, np.inf]
names = ['0-450k', '451k-900k', '901k-1.350k', '1.351k-1.800k', '1.801k-2.250k',
         '2.251k-2.700k', '2.701k-3.150k', '3.151k-3.600k', '3.601k-4.050k', '+4.051k']
df1['rango_donacion'] = pd.cut(df1['cre_mov'], bins, labels=names)
print(df1.groupby(['rango_donacion'])['rango_donacion'].count())
print(df1.groupby(['rango_donacion'])['cre_mov'].sum())

# supernumerarias
print("supernumerarias")
df2 = df_total.loc[df_total['categoria_cco'] == 22]
# minimo = df2['cre_mov'][df2['cre_mov'].ne(0)].min()
minimo = df2['cre_mov'].min()
maximo = df2['cre_mov'].max()
clases = (maximo - minimo) / 7
plt.hist(x=df2['cre_mov'], bins=30, color='#F2AB6D', rwidth=0.85)
plt.title('Histograma coop')
plt.xlabel('Total donación')
plt.ylabel('Frecuencia')
plt.show()
bins = [0, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000,
        8000000, np.inf]
names = ['0-1.000k', '1.001k-2.000k', '2.001k-3.000k', '3.001k-4.000k', '4.001k-5.000k',
         '5.001k-6.000k', '6.001k-7.000k', '7.001k-8.000k', '+8.001']
df2['rango_donacion'] = pd.cut(df2['cre_mov'], bins, labels=names)
print(df2.groupby(['rango_donacion'])['rango_donacion'].count())
print(df2.groupby(['rango_donacion'])['cre_mov'].sum())

# empresas
print("empresas")
df3 = df_total.loc[df_total['categoria_cco'] == 23]
# minimo = df3['cre_mov'][df3['cre_mov'].ne(0)].min()
minimo = df3['cre_mov'].min()
maximo = df3['cre_mov'].max()
clases = (maximo - minimo) / 7
print(clases)
plt.hist(x=df3['cre_mov'], bins=30, color='#F2AB6D', rwidth=0.85)
plt.title('Histograma coop')
plt.xlabel('Total donación')
plt.ylabel('Frecuencia')
plt.show()
bins = [0, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000,
        8000000, np.inf]
names = ['0-1.000k', '1.001k-2.000k', '2.001k-3.000k', '3.001k-4.000k', '4.001k-5.000k',
         '5.001k-6.000k', '6.001k-7.000k', '7.001k-8.000k', '+8.001']
df3['rango_donacion'] = pd.cut(df3['cre_mov'], bins, labels=names)
print(df3.groupby(['rango_donacion'])['rango_donacion'].count())
print(df3.groupby(['rango_donacion'])['cre_mov'].sum())

# mantenimiento
print("matenimiento")
df4 = df_total.loc[df_total['categoria_cco'] == 4]
# minimo = df3['cre_mov'][df3['cre_mov'].ne(0)].min()
minimo = df4['cre_mov'].min()
maximo = df4['cre_mov'].max()
clases = (maximo - minimo) / 7
print(minimo)
print(maximo)
plt.hist(x=df4['cre_mov'], bins=30, color='#F2AB6D', rwidth=0.85)
plt.title('Histograma coop')
plt.xlabel('Total donación')
plt.ylabel('Frecuencia')
plt.show()
bins = [0, 10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000,
        80000000, np.inf]
names = ['0-10.000k', '10.001k-20.000k', '20.001k-30.000k', '30.001k-40.000k', '40.001k-50.000k',
         '50.001k-60.000k', '60.001k-70.000k', '70.001k-80.000k', '+80.001']
df4['rango_donacion'] = pd.cut(df4['cre_mov'], bins, labels=names)
print(df4.groupby(['rango_donacion'])['rango_donacion'].count())
print(df4.groupby(['rango_donacion'])['cre_mov'].sum())

# eventos, actividades y productos
print("eventos, actividades, productos")
df5 = df_total.loc[df_total['categoria_cco'] == 6]
# minimo = df3['cre_mov'][df3['cre_mov'].ne(0)].min()
minimo = df5['cre_mov'].min()
maximo = df5['cre_mov'].max()
clases = (maximo - minimo) / 7
print(minimo)
print(maximo)
plt.hist(x=df5['cre_mov'], bins=30, color='#F2AB6D', rwidth=0.85)
plt.title('Histograma coop')
plt.xlabel('Total donación')
plt.ylabel('Frecuencia')
plt.show()
bins = [0, 450000, 900000, 1350000, 1800000, 2250000, 2700000, 3150000,
        3600000, 4050000, np.inf]
names = ['0-450k', '451k-900k', '901k-1.350k', '1.351k-1.800k', '1.801k-2.250k',
         '2.251k-2.700k', '2.701k-3.150k', '3.151k-3.600k', '3.601k-4.050k', '+4.051k']
df5['rango_donacion'] = pd.cut(df5['cre_mov'], bins, labels=names)
print(df5.groupby(['rango_donacion'])['rango_donacion'].count())
print(df5.groupby(['rango_donacion'])['cre_mov'].sum())


df_total = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)
print(df_total.columns.values)
df_total.to_csv('./contabilidad_limpios/Auxiliar_Donantes.csv',
                index=False, encoding='utf-8')
print("despues de limmat")
print(len(df_total))
# print(df_total.tail())
