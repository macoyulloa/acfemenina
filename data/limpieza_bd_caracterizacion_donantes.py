#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# cargando bases de dastos de caracticacion de cada tipo de donante
d_empresas = pd.read_csv('./donantes/donantes_empresas.csv')
d_coop_mercadeo = pd.read_csv('./donantes/donantes_cooperadoras_mercadeo.csv')
d_coop_terceros = pd.read_csv('./donantes/donantes_cooperadoras_terceros.csv')
d_sup_mercadeo = pd.read_csv(
    './donantes/donantes_supernumerarias_mercadeo.csv')
d_sup_terceros = pd.read_csv(
    './donantes/donantes_supernumerarias_terceros.csv')
d_terceros = pd.read_csv('./donantes/donantes_terceros_todos.csv')

d_coop_mercadeo.sort_values('num_doc', inplace=True, ascending=False)
d_coop_terceros.sort_values('num_doc', inplace=True, ascending=False)
d_sup_mercadeo.sort_values('num_doc', inplace=True, ascending=False)
d_sup_terceros.sort_values('num_doc', inplace=True, ascending=False)
# print(d_coop_terceros.head(20))
# print(d_coop_terceros.columns.values)

# Conoer el porcentaje de completitud de cada variable
# print("Base de Datos Donantes empresas: Nubia \n",
#      100 - (((d_empresas.isna().sum())/62)*100), "\n número de registros: \n",
#      len(d_empresas.index))
# print("Base de Datos Donantes cooperadoras terceros: ANTARES \n",
#      100 - (((d_coop_terceros.isna().sum())/573)
#             * 100), "\n número de registros: \n",
#      len(d_coop_terceros.index))
# print("Base de Datos Donantes cooperadoras mercadeo: ANTARES \n",
#      100 - (((d_coop_mercadeo.isna().sum())/573)
#             * 100), "\n número de registros: \n",
#      len(d_coop_mercadeo.index))
# print("Base de Datos Donantes supernumerarias terceros: ANTARES \n",
#      100 - (((d_sup_terceros.isna().sum())/548)
#             * 100), "\n número de registros: \n",
#      len(d_sup_terceros.index))
# print("Base de Datos Donantes supernumerarias mercadeo: ANTARES \n",
#      100 - (((d_coop_mercadeo.isna().sum())/548)
#             * 100), "\n número de registros: \n",
#      len(d_sup_mercadeo.index))
# print("Base de Datos TERCEROS: todo el que ha tenido registro contable\n",
#      d_terceros.isna().mean(), "\n número de registros: \n",
#      len(d_terceros.index))

# borrar nan de las bases de datos
d_empresas.dropna(subset=["cod_ter"], inplace=True)
print(d_empresas.head())
d_coop_terceros.dropna(subset=["num_doc"], inplace=True)
d_coop_mercadeo.dropna(subset=["num_doc"], inplace=True)
d_sup_terceros.dropna(subset=["num_doc"], inplace=True)
d_sup_mercadeo.dropna(subset=["num_doc"], inplace=True)

# juntas las dos bases de datos: terceros y mercadeo de cada tipo de donante
d_coop = d_coop_mercadeo.join(
    d_coop_terceros[['doc_num_2', 'telefono', 'celular', 'direccion', 'mail']])
d_sup = d_sup_mercadeo.join(
    d_sup_terceros[['telefono', 'celular', 'direccion', 'mail', 'validada']])
print(len(d_coop))
print(len(d_sup))
print(len(d_empresas))


# cambiar el dtype de la columna cod_ter de empresas
d_empresas['cod_ter'] = pd.to_numeric(d_empresas['cod_ter'], errors='coerce')

# renombrando las key columns para poder hacer los cruces
d_coop.rename(columns={'num_doc': 'cod_ter'}, inplace=True)
d_sup.rename(columns={'num_doc': 'cod_ter'}, inplace=True)

##########################################
# separar columnas centro y tipo de donante
d_coop['tipo_donante'] = d_coop['centro'].str.split('-', expand=True)[1]
d_coop['centro'] = d_coop['centro'].str.split('-', expand=True)[0]
d_sup['tipo_donante'] = d_sup['centro'].str.split('-', expand=True)[1]
d_sup['centro'] = d_sup['centro'].str.split('-', expand=True)[0]

#########################################
# rango de edades coop
d_coop['cod_ter'] = d_coop['cod_ter'].astype('int32', copy=False)
d_coop['fecha_nacimiento'] = pd.to_datetime(d_coop['fecha_nacimiento'],
                                            infer_datetime_format=True)
now = pd.Timestamp('now')
d_coop['edad'] = (now - d_coop['fecha_nacimiento']).astype('<m8[Y]')
bins = [0, 18, 30, 40, 50, 60, 70, np.inf]
names = ['<18', '19-30', '31-40', '41-50', '51-60', '61-70', '+71']
d_coop['rango_edades'] = pd.cut(d_coop['edad'], bins, labels=names)
# rango edades sup
d_sup['cod_ter'] = d_sup['cod_ter'].astype('int32', copy=False)
d_sup['fecha_nacimiento'] = pd.to_datetime(d_coop['fecha_nacimiento'],
                                           infer_datetime_format=True)
now = pd.Timestamp('now')
d_sup['edad'] = (now - d_sup['fecha_nacimiento']).astype('<m8[Y]')
bins = [0, 18, 30, 40, 50, 60, 70, np.inf]
names = ['<18', '19-30', '31-40', '41-50', '51-60', '61-70', '+71']
d_sup['rango_edades'] = pd.cut(d_sup['edad'], bins, labels=names)

# borrar todos los registros que no sean empresas con NIT y preparar las
# empresas que están dentor de la lista de codigos de terceros de contabili
# index_names = d_terceros[d_terceros['tdoc'] != 31].index
# d_terceros.drop(index_names, inplace=True)
# d_terceros.rename(columns={'nit_ter': 'cod_ter'}, inplace=True)
# d_terceros.drop(columns={'mae_ter', 'apl1', 'apl2',
#                         'dig_ver', 'nom1', 'nom2', 'tdoc'}, inplace=True)

# guardando los archivos de bases de datos limpios en el .csv
d_empresas.to_csv('./donantes_limpios/donantes_empresas.csv',
                  index=False, encoding='utf-8')
d_coop.to_csv('./donantes_limpios/donantes_cooperadoras.csv',
              index=False, encoding='utf-8')
d_sup.to_csv('./donantes_limpios/donantes_supernumerarias.csv',
             index=False, encoding='utf-8')
d_empresas.to_csv('./donantes_limpios/donantes_terceros_empresas.csv',
                  index=False, encoding='utf-8')

df = pd.concat([d_coop, d_sup], ignore_index=True)
# profesion cleaning up the column
df['profesion'] = df['profesion'].replace('Hogar', 'Ama de casa')
df['profesion'] = df['profesion'].replace(
    'Administradora de empresas', 'Administradora')
df['profesion'] = df['profesion'].replace(
    'Administradora de Empresas', 'Administradora')
df['profesion'] = df['profesion'].replace('Contadora Publica', 'Contadora')
df['profesion'] = df['profesion'].replace(
    'Administradora en bienes raíces', 'Administradora')
df['profesion'] = df['profesion'].replace(
    'Administradora de instituciones de servicio', 'Administradora')
df['profesion'] = df['profesion'].replace(
    'Educadora', 'Profesora')
df['profesion'] = df['profesion'].replace(
    'Docente', 'Profesora')
df['profesion'] = df['profesion'].replace(
    'Medico', 'Médico')
df['profesion'] = df['profesion'].replace(
    'Medica', 'Médico')
df['profesion'] = df['profesion'].replace(
    'Psicologa', 'Psicóloga')
df['profesion'] = df['profesion'].replace(
    'Comunicadora Social', 'Comunicadora social')

print(df.head())
print(df.tail())
df.to_csv('./donantes_limpios/donantes.csv',
          index=False, encoding='utf-8')
