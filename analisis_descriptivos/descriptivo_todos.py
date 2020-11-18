#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.gridspec as gridspec


# colores de las gráficas
cmap = plt.cm.rainbow
color = cmap(np.linspace(0., 1., 12))

#######################################################
###### Gráficos Descriptivos Datos año a año ##########
#######################################################
# cargo los archivos de bases de datos de cooperadoras
df_ext = pd.read_csv(
    '../bd_finales/part_ext_transaccional_caracterizacion_ano_ano.csv')
# cargo los archivos de bases de datos de cooperadoras
df_int = pd.read_csv(
    '../bd_finales/part_int_transaccional_caracterizacion_ano_ano.csv')
df_co = pd.read_csv(
    '../bd_finales/cooperadoras_transaccional_caracterizacion_ano_ano.csv')
# cargo los archivos de bases de datos de cooperadoras
df_emp = pd.read_csv(
    '../bd_finales/empresas_transaccional_caracterizacion_ano_ano.csv')

# tendencia de donación año a año en monto de donación
fig, (ax1) = plt.subplots(1, figsize=(20, 10))
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante cooperadoras')
df_co1 = df_co[['total_2018', 'total_2019', 'total_2020']
               ].sum().to_frame()
df_co1.rename(columns={0: 'donante cooperadoras'}, inplace=True)
df_int1 = df_int[['total_2018', 'total_2019', 'total_2020']
                 ].sum().to_frame()
df_int1.rename(columns={0: 'donante particulares internas'}, inplace=True)
df_ext1 = df_ext[['total_2018', 'total_2019', 'total_2020']
                 ].sum().to_frame()
df_ext1.rename(columns={0: 'donante particulares externas'}, inplace=True)
df_emp1 = df_emp[['total_2018', 'total_2019', 'total_2020']
                 ].sum().to_frame()
df_emp1.rename(columns={0: 'donante empresas'}, inplace=True)
for frame in [df_co1, df_int1, df_ext1, df_emp1]:
    frame.plot(ax=ax1)
ax1.set_xlabel('Año')
ax1.set_ylabel('Monto donado en miles de millones de pesos')
ax1.set_title("Tendencia del monto de donación acumulado año a año")
plt.xticks(rotation=30)
fig.savefig('./images/todos/descriptivo_1.png')
# plt.show()



##########################################################
##### gráficas usando la base de datos master ############
##########################################################
# cargo los archivos de bases de datos de cooperadoras
df_ext = pd.read_csv(
    '../bd_finales/part_ext_transaccional_caracterizacion.csv')
# cargo los archivos de bases de datos de cooperadoras
df_int = pd.read_csv(
    '../bd_finales/part_int_transaccional_caracterizacion.csv')
df_co = pd.read_csv(
    '../bd_finales/cooperadoras_transaccional_caracterizacion.csv')
# cargo los archivos de bases de datos de cooperadoras
df_emp = pd.read_csv(
    '../bd_finales/empresas_transaccional_caracterizacion.csv')


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
fig.suptitle(
    'Insights: información caracteristica vs transaccional donante particulares externas')
bins = [1, 3, 6, 9, 12, 15, 18]
names = ['1-3', '4-6', '7-9', '10-12', '13-15', '16-18']
df_ext['rango_n_transac'] = pd.cut(df_ext['recurrencia_prom'], bins, labels=names)
df_ext1 =  df_ext.groupby(['rango_n_transac']).size().to_frame()
df_ext1.rename(columns={0: 'donante particulares externas'}, inplace=True)
# print(df_ext1)
df_int['rango_n_transac'] = pd.cut(df_int['recurrencia_prom'], bins, labels=names)
df_int1 =  df_int.groupby(['rango_n_transac']).size().to_frame()
df_int1.rename(columns={0: 'donante particulares internas'}, inplace=True)
df_co['rango_n_transac'] = pd.cut(df_co['recurrencia_prom'], bins, labels=names)
df_co1 =  df_co.groupby(['rango_n_transac']).size().to_frame()
df_co1.rename(columns={0: 'donante cooperadoras'}, inplace=True)
df_emp['rango_n_transac'] = pd.cut(df_emp['recurrencia_prom'], bins, labels=names)
df_emp1 =  df_emp.groupby(['rango_n_transac']).size().to_frame()
df_emp1.rename(columns={0: 'donante empresas'}, inplace=True)
for frame in [df_co1, df_int1, df_ext1, df_emp1]:
    frame.plot(ax=ax1)
ax1.set_xlabel('Número de transacciones promedio al año')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Número promedio de transacciones al año de donantes")
df_ext1 =  df_ext.groupby(['rango_n_transac'])['donacion_total'].sum().to_frame()
df_ext1.rename(columns={'donacion_total': 'donante particulares externas'}, inplace=True)
# print(df_ext1)
df_int1 =  df_int.groupby(['rango_n_transac'])['donacion_total'].sum().to_frame()
df_int1.rename(columns={'donacion_total': 'donante particulares internas'}, inplace=True)
df_co1 =  df_co.groupby(['rango_n_transac'])['donacion_total'].sum().to_frame()
df_co1.rename(columns={'donacion_total': 'donante cooperadoras'}, inplace=True)
df_emp1 =  df_emp.groupby(['rango_n_transac'])['donacion_total'].sum().to_frame()
df_emp1.rename(columns={'donacion_total': 'donante empresas'}, inplace=True)
for frame in [df_co1, df_int1, df_ext1, df_emp1]:
    frame.plot(ax=ax2)
ax2.set_ylabel('Monto acumulado (en miles de millones)')
ax2.set_xlabel('Número de transacciones promedio al año')
ax2.set_title("Monto total acumulado por transacciones")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=0)
fig.savefig('./images/todos/descriptivo_14.png')
