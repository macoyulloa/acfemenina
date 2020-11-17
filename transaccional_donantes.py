#!/usr/bin/env python3
import pandas as pd
import numpy as np


###############################################
#########Informe de contabilidad 2018##########
###############################################
df1_2018 = pd.read_csv(
    './data/contabilidad_limpios/Auxiliar_Donantes_2018.csv')
# print(df1_2018.columns.values)
df1_2018.sort_values('cod_ter', inplace=True, ascending=False)
# print(df1_2018.head())
# df = df1_2018.groupby(['cod_ter', 'categoria_suc', 'cod_suc', 'categoria_cco',
#                        'cod_cco'], as_index=False)['cre_mov'].sum()
#df.set_index('cod_ter', inplace=True)
# print(df)

df_2018 = df1_2018.groupby(['cod_ter'])['cre_mov'].sum().to_frame()
# columna recurrencia: número de transacciones 2018
recurrencia = df1_2018['cod_ter'].value_counts().sort_index().to_frame()
df_2018 = df_2018.join(recurrencia)
# cambiando nombre de las columnas por las que debería ser
df_2018.rename(columns={'cod_ter': 'recurrencia_2018',
                        'cre_mov': 'total_2018'}, inplace=True)
# columna promedio mensual donación 2018
df_2018['prom_mensual_2018'] = df_2018['total_2018'] / 12
# columna recurrencia pocentual, porcentaje del año que donó
df_2018['recurrencia_%_2018'] = (df_2018['recurrencia_2018'] / 12) * 100
# columna categoría de sucursal de la donacion: centros, ACF, labores sociales
df_2018 = df_2018.join((df1_2018.groupby(['cod_ter']).first())[
                       'categoria_suc'].to_frame().rename(
                           columns={'categoria_suc': 'categ_suc_2018'}))
# columna categoría de centro de costo, destino, donación.
df_2018 = df_2018.join((df1_2018.groupby(['cod_ter']).first())[
                       'categoria_cco'].to_frame().rename(
                           columns={'categoria_cco': 'categ_cco_2018'}))
# columna codigo de sucursal
df_2018 = df_2018.join((df1_2018.groupby(['cod_ter']).first())[
                       'cod_suc'].to_frame().rename(
                           columns={'cod_suc': 'cod_suc_2018'}))
# columna codigo de centro de costo
df_2018 = df_2018.join((df1_2018.groupby(['cod_ter']).first())[
                       'cod_cco'].to_frame().rename(
                           columns={'cod_cco': 'cod_cco_2018'}))

print(df_2018.head())


###############################################
#########Informe de contabilidad 2019##########
###############################################
df1_2019 = pd.read_csv(
    './data/contabilidad_limpios/Auxiliar_Donantes_2019.csv')
# print(df1_2019.columns.values)
df1_2019.sort_values('cod_ter', inplace=True, ascending=False)
# print(df1_2019.head())
# df = df1_2019.groupby(['cod_ter', 'categoria_suc', 'cod_suc', 'categoria_cco',
#                        'cod_cco'], as_index=False)['cre_mov'].sum()
#df.set_index('cod_ter', inplace=True)
# print(df)

df_2019 = df1_2019.groupby(['cod_ter'])['cre_mov'].sum().to_frame()
# columna recurrencia: número de transacciones 2019
recurrencia = df1_2019['cod_ter'].value_counts().sort_index().to_frame()
df_2019 = df_2019.join(recurrencia)
# cambiando nombre de las columnas por las que debería ser
df_2019.rename(columns={'cod_ter': 'recurrencia_2019',
                        'cre_mov': 'total_2019'}, inplace=True)
# columna promedio mensual donación 2019
df_2019['prom_mensual_2019'] = df_2019['total_2019'] / 12
# columna recurrencia pocentual, porcentaje del año que donó
df_2019['recurrencia_%_2019'] = (df_2019['recurrencia_2019'] / 12) * 100
# columna categoría de sucursal de la donacion: centros, ACF, labores sociales
df_2019 = df_2019.join((df1_2019.groupby(['cod_ter']).first())[
                       'categoria_suc'].to_frame().rename(
                           columns={'categoria_suc': 'categ_suc_2019'}))
# columna categoría de centro de costo, destino, donación.
df_2019 = df_2019.join((df1_2019.groupby(['cod_ter']).first())[
                       'categoria_cco'].to_frame().rename(
                           columns={'categoria_cco': 'categ_cco_2019'}))
# columna codigo de sucursal
df_2019 = df_2019.join((df1_2019.groupby(['cod_ter']).first())[
                       'cod_suc'].to_frame().rename(
                           columns={'cod_suc': 'cod_suc_2019'}))
# columna codigo de centro de costo
df_2019 = df_2019.join((df1_2019.groupby(['cod_ter']).first())[
                       'cod_cco'].to_frame().rename(
                           columns={'cod_cco': 'cod_cco_2019'}))

print(df_2019.head())


###############################################
#########Informe de contabilidad 2020##########
###############################################
df1_2020 = pd.read_csv(
    './data/contabilidad_limpios/Auxiliar_Donantes_2020.csv')
# print(df1_2020.columns.values)
df1_2020.sort_values('cod_ter', inplace=True, ascending=False)
# print(df1_2020.head())
# df = df1_2020.groupby(['cod_ter', 'categoria_suc', 'cod_suc', 'categoria_cco',
#                        'cod_cco'], as_index=False)['cre_mov'].sum()
#df.set_index('cod_ter', inplace=True)
# print(df)

df_2020 = df1_2020.groupby(['cod_ter'])['cre_mov'].sum().to_frame()
# columna recurrencia: número de transacciones 2020
recurrencia = df1_2020['cod_ter'].value_counts().sort_index().to_frame()
df_2020 = df_2020.join(recurrencia)
# cambiando nombre de las columnas por las que debería ser
df_2020.rename(columns={'cod_ter': 'recurrencia_2020',
                        'cre_mov': 'total_2020'}, inplace=True)
# columna promedio mensual donación 2020
df_2020['prom_mensual_2020'] = df_2020['total_2020'] / 12
# columna recurrencia pocentual, porcentaje del año que donó
df_2020['recurrencia_%_2020'] = (df_2020['recurrencia_2020'] / 12) * 100
# columna categoría de sucursal de la donacion: centros, ACF, labores sociales
df_2020 = df_2020.join((df1_2020.groupby(['cod_ter']).first())[
                       'categoria_suc'].to_frame().rename(
                           columns={'categoria_suc': 'categ_suc_2020'}))
# columna categoría de centro de costo, destino, donación.
df_2020 = df_2020.join((df1_2020.groupby(['cod_ter']).first())[
                       'categoria_cco'].to_frame().rename(
                           columns={'categoria_cco': 'categ_cco_2020'}))
# columna codigo de sucursal
df_2020 = df_2020.join((df1_2020.groupby(['cod_ter']).first())[
                       'cod_suc'].to_frame().rename(
                           columns={'cod_suc': 'cod_suc_2020'}))
# columna codigo de centro de costo
df_2020 = df_2020.join((df1_2020.groupby(['cod_ter']).first())[
                       'cod_cco'].to_frame().rename(
                           columns={'cod_cco': 'cod_cco_2020'}))
print(df_2020.columns.values)
print(df_2020.head())


#############################################################
############ Unión de las tres bases de datos ###############
#############################################################
df_total = pd.merge(df_2018, df_2019, on='cod_ter', how='outer')
df_total = pd.merge(df_total, df_2020, on='cod_ter', how='outer')
df_total.fillna(0, inplace=True)
# print(df_total)
# print(len(df_total))

# columnas calculadas, consolidando la base de datos maestra
df_total['variacion_2018-2019'] = df_total['total_2019'] - \
    df_total['total_2018']
df_total['variacion_2019-2020'] = df_total['total_2020'] - \
    df_total['total_2019']
df_total['variacion_%_2018-2019'] = (df_total['variacion_2018-2019'] /
                                     df_total['total_2018']) * 100
df_total['variacion_%_2019-2020'] = (df_total['variacion_2019-2020'] /
                                     df_total['total_2019']) * 100
df_total.fillna(0, inplace=True)
print(df_total.columns.values)

df_total.to_csv('./bd_finales/bd_transaccional_donantes_ano_ano.csv',
                encoding='utf-8')

###############################################
##Consolidación final de las bases de datos ###
###############################################

df_final = pd.DataFrame()
df_final['misma_sucursal'] = df_total[['categ_suc_2018',
                                       'categ_suc_2019',
                                       'categ_suc_2020']].all(axis='columns')
df_final['misma_causa'] = df_total[['categ_cco_2018',
                                    'categ_cco_2019',
                                    'categ_cco_2020']].all(axis='columns')
df_final['donacion_total'] = df_total['total_2018'] + \
    df_total['total_2019'] + df_total['total_2020']
df_final['variacion_promedio'] = (df_total['variacion_2019-2020'] +
                                  df_total['variacion_2018-2019']) / 2
df_final['variacion_2019-2020'] = df_total['variacion_2019-2020']
df_final['variacion_promedio_%'] = (df_total['variacion_%_2019-2020'] +
                                    df_total['variacion_%_2018-2019']) / 2
df_final['variacion_%_2019-2020'] = df_total['variacion_%_2019-2020']
df_final['recurrencia_prom'] = ((
    df_total['recurrencia_2018'] + df_total['recurrencia_2019'] +
    df_total['recurrencia_2020']) / 3).round().astype(int)
#df_final['recurrencia_prom'] = df_final['recurrencia_prom'].round().astype(int)
# columna frecuencia de donaciones, basada en la columna recurrencia
conditions = [
    (df_final['recurrencia_prom'] == 1),
    (df_final['recurrencia_prom'] == 2),
    (df_final['recurrencia_prom'] == 3),
    (df_final['recurrencia_prom'] == 4),
    (df_final['recurrencia_prom'] == 5),
    (df_final['recurrencia_prom'] == 6),
    (df_final['recurrencia_prom'] == 7),
    (df_final['recurrencia_prom'] == 8),
    (df_final['recurrencia_prom'] == 9),
    (df_final['recurrencia_prom'] == 10),
    (df_final['recurrencia_prom'] == 11),
    (df_final['recurrencia_prom'] == 12),
]

# create a list of the values we want to assign for each condition
values = ['mensual', 'bimensual', 'trimestral', 'cuatrimestre',
          'quin', 'semestre', 'septimestre', 'octimestre', 'nonamestre',
          'decamestre', 'oncemestre', 'anual']
# create a new column and use np.select to assign values to it using our
# lists as arguments
df_final['reccurencia'] = np.select(conditions, values)
print(df_final)
print(df_final.sort_values(
    'donacion_total', inplace=False, ascending=False).head())

df_final.to_csv('./bd_finales/bd_transaccional_donantes.csv',
                encoding='utf-8')

# print(df_total.head())
# print(df_final.columns.values)

# print(df_final.head())
# print(len(df_final))
