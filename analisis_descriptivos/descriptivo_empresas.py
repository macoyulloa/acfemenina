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
df = pd.read_csv(
    '../bd_finales/empresas_transaccional_caracterizacion_ano_ano.csv')
# coop.set_index('cod_ter', inplace=True)
d_2018 = pd.read_csv(
    '../data/contabilidad_limpios/Auxiliar_Donantes_2018.csv')
d_2019 = pd.read_csv(
    '../data/contabilidad_limpios/Auxiliar_Donantes_2019.csv')
d_2020 = pd.read_csv(
    '../data/contabilidad_limpios/Auxiliar_Donantes_2020.csv')
print(df.columns.values)

# tendencia de donación año a año en monto de donación
fig, (ax1) = plt.subplots(1)
fig.suptitle(
    'Insights: información caracteristica vs transaccional del donante empresas')
df[['total_2018', 'total_2019', 'total_2020']
   ].sum().plot(ax=ax1, figsize=(20, 10))
ax1.set_xlabel('Año')
ax1.set_ylabel('Monto donado en 00.000.000 COP')
ax1.set_title("Tendencia del monto de donación acumulado año a año")
plt.xticks(rotation=30)
fig.savefig('./images/empresas/empresas_descriptivo_1.png')
# plt.show()

# sucrsal fuente de cada donacion año a año
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional del donante empresas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_suc_2018'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False)
# print(df1)
df1['sucursal'] = ['no aplica', 'ACF', 'centros', 'labores sociales']
df1.reset_index(inplace=True)
df1.drop(columns=['categ_suc_2018'], inplace=True)
df1.set_index('sucursal', inplace=True)
df1.plot.bar(ax=ax1, figsize=(20, 10), colors=color, legend=False)
ax1.set_xlabel('Destino donación')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Para quién o qué van las donaciones 2018")
ax2 = fig.add_subplot(gs[0, 1])
df1 = df.groupby(['categ_suc_2019'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False)
# print(df1)
df1['sucursal'] = ['no aplica', 'ACF', 'labores sociales', 'centros']
df1.reset_index(inplace=True)
df1.drop(columns=['categ_suc_2019'], inplace=True)
df1.set_index('sucursal', inplace=True)
df1.plot.bar(ax=ax2, figsize=(20, 10), colors=color, legend=False)
ax2.set_xlabel('Destino donación')
ax2.set_ylabel('Cantidad de donantes')
ax2.set_title("Para quién o qué van las donaciones 2019")
ax3 = fig.add_subplot(gs[1, :])
df1 = df.groupby(['categ_suc_2020'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False)
# print(df1)
df1['sucursal'] = ['no aplica', 'ACF', 'labores sociales', 'centros']
df1.reset_index(inplace=True)
df1.drop(columns=['categ_suc_2020'], inplace=True)
df1.set_index('sucursal', inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10), colors=color, legend=False)
ax3.set_xlabel('Destino donación')
ax3.set_ylabel('Cantidad de donantes')
ax3.set_title("Para quién o qué van las donaciones 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=0)
fig.savefig('./images/empresas/empresas_descriptivo_3_1.png')
# plt.show()

# Top sucursal: centor cultural fuente de cada donacion año a año
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante empresas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_suc_2018'])['total_2018'].sum().to_frame()
df1['sucursal'] = ['no aplica', 'centros', 'ACF', 'labores sociales']
df1.reset_index(inplace=True)
df1.drop(columns=['categ_suc_2018'], inplace=True)
df1.set_index('sucursal', inplace=True)
df1.plot.bar(ax=ax1, figsize=(20, 10), colors=color, legend=False)
ax1.set_xlabel('Destino donación')
ax1.set_ylabel('Monto donado COP(+ 00.000.000)')
ax1.set_title("Monto total donado a cada destino 2018")
ax2 = fig.add_subplot(gs[0, 1])
df1 = df.groupby(['categ_suc_2019'])['total_2019'].sum().to_frame()
df1['sucursal'] = ['no aplica', 'centros', 'ACF', 'labores sociales']
df1.reset_index(inplace=True)
df1.drop(columns=['categ_suc_2019'], inplace=True)
df1.set_index('sucursal', inplace=True)
df1.plot.bar(ax=ax2, figsize=(20, 10), colors=color, legend=False)
ax2.set_xlabel('Destino donación')
ax2.set_ylabel('Monto donado COP (+ 00.000.000)')
ax2.set_title("Monto total donado a cada destino 2019")
ax3 = fig.add_subplot(gs[1, :])
df1 = df.groupby(['categ_suc_2020'])['total_2020'].sum().to_frame()
df1['sucursal'] = ['no aplica', 'centros', 'ACF', 'labores sociales']
df1.reset_index(inplace=True)
df1.drop(columns=['categ_suc_2020'], inplace=True)
df1.set_index('sucursal', inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10), colors=color, legend=False)
ax3.set_xlabel('Destino donación')
ax3.set_ylabel('Monto donado COP')
ax3.set_title("Monto total donado a cada destino 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=0)
fig.savefig('./images/empresas/empresas_descriptivo_3_2.png')
# plt.show()

# Top sucursal: centor cultural fuente de cada donacion año a año
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante empresas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_suc_2018', 'cod_suc_2018'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_suc_2018'] == 3.0]
# print(df1)
df1['nom_suc'] = ['ICSEF', 'Casanueva (JUV)', 'Fondo Sacerdotes']
df1.drop(columns=['categ_suc_2018', 'cod_suc_2018'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax1, legend=False)
ax1.set_xlabel('Labor social')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Destino Donación: Labor Social 2018")
ax2 = fig.add_subplot(gs[0, 1])
df1 = df.groupby(['categ_suc_2019', 'cod_suc_2019'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_suc_2019'] == 3.0]
# print(df1)
df1['nom_suc'] = ['Casanueva (JUV)']
df1.drop(columns=['categ_suc_2019', 'cod_suc_2019'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax2, figsize=(20, 10), legend=False)
ax2.set_xlabel('Labor social')
ax2.set_ylabel('Cantidad de donantes')
ax2.set_title("Destino Donación: Labor Social 2019")
ax3 = fig.add_subplot(gs[1, :])
df1 = df.groupby(['categ_suc_2020', 'cod_suc_2020'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_suc_2020'] == 3.0]
# print(df1)
df1['nom_suc'] = ['Casanueva (JUV)']
df1.drop(columns=['categ_suc_2020', 'cod_suc_2020'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10), legend=False)
ax3.set_xlabel('Labor Social')
ax3.set_ylabel('Cantidad de donantes')
ax3.set_title("Destino Donación: Labor Social 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=15)
fig.savefig('./images/empresas/empresas_descriptivo_3_1_1.png')
# plt.show()

# Top sucursal: centor cultural fuente de cada donacion año a año
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante empresas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_suc_2018', 'cod_suc_2018'])[
    'total_2018'].sum().reset_index()
df1 = df1.loc[df1['categ_suc_2018'] == 3.0]
# print(df1)
df1['nom_suc'] = ['ICSEF', 'Casanueva (JUV)', 'Fondo Sacerdotes']
df1.drop(columns=['categ_suc_2018', 'cod_suc_2018'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax1, legend=False)
ax1.set_xlabel('Labor social')
ax1.set_ylabel('Monto donado COP (+ 00.000.000)')
ax1.set_title("Destino Donación: Labor Social 2018")
ax2 = fig.add_subplot(gs[0, 1])
df1 = df.groupby(['categ_suc_2019', 'cod_suc_2019'])[
    'total_2019'].sum().reset_index()
df1 = df1.loc[df1['categ_suc_2019'] == 3.0]
# print(df1)
df1['nom_suc'] = ['Casanueva (JUV)']
df1.drop(columns=['categ_suc_2019', 'cod_suc_2019'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax2, figsize=(20, 10), legend=False)
ax2.set_xlabel('Labor social')
ax2.set_ylabel('Monto donado COP (+ 0.000.000)')
ax2.set_title("Destino Donación: Labor Social 2019")
ax3 = fig.add_subplot(gs[1, :])
df1 = df.groupby(['categ_suc_2020', 'cod_suc_2020'])[
    'total_2020'].sum().reset_index()
df1 = df1.loc[df1['categ_suc_2020'] == 3.0]
# print(df1)
df1['nom_suc'] = ['Casanueva (JUV)']
df1.drop(columns=['categ_suc_2020', 'cod_suc_2020'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10), legend=False)
ax3.set_xlabel('Labor Social')
ax3.set_ylabel('Monto donado COP')
ax3.set_title("Destino Donación: Labor Social 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=0)
fig.savefig('./images/empresas/empresas_descriptivo_3_2_1.png')
# plt.show()

# Top sucursal: centor cultural fuente de cada donacion año a año
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante empresas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_suc_2018', 'cod_suc_2018'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_suc_2018'] == 1.0]
# print(df1)
df1['nom_suc'] = ['Cedro', 'Nogal', 'Torreon']
df1.drop(columns=['categ_suc_2018', 'cod_suc_2018'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax1, legend=False)
ax1.set_xlabel('Centro cultural')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Destino Donación: Centro Cultural 2018")
ax2 = fig.add_subplot(gs[0, 1])
df1 = df.groupby(['categ_suc_2019', 'cod_suc_2019'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_suc_2019'] == 1.0]
# print(df1)
df1['nom_suc'] = ['Naval']
df1.drop(columns=['categ_suc_2019', 'cod_suc_2019'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax2, figsize=(20, 10), legend=False)
ax2.set_xlabel('Centro cultural')
ax2.set_ylabel('Cantidad de donantes')
ax2.set_title("Destino Donación: Centro cultural 2019")
ax3 = fig.add_subplot(gs[1, :])
df1 = df.groupby(['categ_suc_2020', 'cod_suc_2020'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_suc_2020'] == 1.0]
# print(df1)
df1['nom_suc'] = ['Cedro', 'Belayes']
df1.drop(columns=['categ_suc_2020', 'cod_suc_2020'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10), legend=False)
ax3.set_xlabel('Centro cultural')
ax3.set_ylabel('Cantidad de donantes')
ax3.set_title("Destino Donación: Centro cultural 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=15)
fig.savefig('./images/empresas/empresas_descriptivo_3_1_2.png')
# plt.show()

# Top sucursal: centor cultural fuente de cada donacion año a año
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante empresas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_suc_2018', 'cod_suc_2018'])[
    'total_2018'].sum().reset_index()
df1 = df1.loc[df1['categ_suc_2018'] == 1.0]
# print(df1)
df1['nom_suc'] = ['Cedro', 'Nogal', 'Torreon']
df1.drop(columns=['categ_suc_2018', 'cod_suc_2018'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax1, legend=False)
ax1.set_xlabel('Centro cultural')
ax1.set_ylabel('Monto donado COP (+ 0.000.000)')
ax1.set_title("Destino Donación: Centro Cultural 2018")
ax2 = fig.add_subplot(gs[0, 1])
df1 = df.groupby(['categ_suc_2019', 'cod_suc_2019'])[
    'total_2019'].sum().reset_index()
df1 = df1.loc[df1['categ_suc_2019'] == 1.0]
# print(df1)
df1['nom_suc'] = ['Naval']
df1.drop(columns=['categ_suc_2019', 'cod_suc_2019'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax2, figsize=(20, 10), legend=False)
ax2.set_xlabel('Centro cultural')
ax2.set_ylabel('Monto donado COP (+ 00.000.000)')
ax2.set_title("Destino Donación: Centro cultural 2019")
ax3 = fig.add_subplot(gs[1, :])
df1 = df.groupby(['categ_suc_2020', 'cod_suc_2020'])[
    'total_2020'].sum().reset_index()
df1 = df1.loc[df1['categ_suc_2020'] == 1.0]
# print(df1)
df1['nom_suc'] = ['Cedro', 'Belayes']
df1.drop(columns=['categ_suc_2020', 'cod_suc_2020'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10), legend=False)
ax3.set_xlabel('Centro cultural')
ax3.set_ylabel('Monto donado COP')
ax3.set_title("Destino Donación: Centro cultural 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=0)
fig.savefig('./images/empresas/empresas_descriptivo_3_2_2.png')
# plt.show()

# centro de costos destino de cada donacion
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional del donante empresas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_cco_2018'])['cod_ter'].count().to_frame(
).sort_values('cod_ter', ascending=False).reset_index()
# print(df1)
df1['cco'] = ['No Aplica', 'Eventos/Act/Prod',  'D Empresas',
              'Manten centros', 'D Particulares']
df1.drop(columns=['categ_cco_2018'], inplace=True)
df1.set_index('cco', inplace=True)
df1.plot.bar(ax=ax1, legend=False, figsize=(20, 10))
ax1.set_xlabel('Origen de la Donación')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Origen de cada Donación 2018")
ax2 = fig.add_subplot(gs[0, 1])  # row 0, col 1
df1 = df.groupby(['categ_cco_2019'])['cod_ter'].count().to_frame(
).sort_values('cod_ter', ascending=False).reset_index()
# print(df1)
df1['cco'] = ['No Aplica', 'Eventos/Act/Prod', 'D Particulares',
              'Manten centros', 'D Cooperadoras', 'D Empresas']
df1.drop(columns=['categ_cco_2019'], inplace=True)
df1.set_index('cco', inplace=True)
df1.plot.bar(ax=ax2, figsize=(20, 10), legend=False)
ax2.set_xlabel('Origen de la Donación')
ax2.set_ylabel('Cantidad de donantes')
ax2.set_title("Origen de cada Donación 2019")
ax3 = fig.add_subplot(gs[1, :])  # row 1, span all columns
df1 = df.groupby(['categ_cco_2020'])['cod_ter'].count().to_frame(
).sort_values('cod_ter', ascending=False).reset_index()
# print(df1)
df1['cco'] = ['No Aplica', 'D Particulares',
              'Eventos/Act/Prod', 'Manten centros']
df1.drop(columns=['categ_cco_2020'], inplace=True)
df1.set_index('cco', inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10), legend=False)
ax3.set_xlabel('Origen de la Donación')
ax3.set_ylabel('Cantidad de donantes')
ax3.set_title("Origen de cada Donación 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=0)
fig.savefig('./images/empresas/empresas_descriptivo_4.png')
# plt.show()

# Top centro de costo: destino de cada donacion año a año
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante empresas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_cco_2018', 'cod_cco_2018'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2018'] == 6.0]
# print(df1)
df1['nom_cco'] = ['Bonos Donacion', 'Evento Solidario', 'Cantarte']
df1.drop(columns=['categ_cco_2018', 'cod_cco_2018'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax1, legend=False)
ax1.set_xlabel('')
ax1.set_ylabel('Número de Donaciones')
ax1.set_title("Origen donación: Eventos, Actividades y Productos 2018")
ax2 = fig.add_subplot(gs[0, 1])
df1 = df.groupby(['categ_cco_2019', 'cod_cco_2019'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2019'] == 6.0]
# print(df1)
df1['nom_cco'] = ['Libros-Navidad', 'CD Nav', 'Taller Imagen']
df1.drop(columns=['categ_cco_2019', 'cod_cco_2019'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax2, legend=False)
ax2.set_xlabel('')
ax2.set_ylabel('Cantidad de donantes')
ax2.set_title("Origen donación: Eventos, Actividades y Productos 2019")
ax3 = fig.add_subplot(gs[1, :])
df1 = df.groupby(['categ_cco_2020', 'cod_cco_2020'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2020'] == 6.0]
# print(df1)
df1['nom_cco'] = ['Bonos Donacion', 'Acción de Gracias']
df1.drop(columns=['categ_cco_2020', 'cod_cco_2020'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10), legend=False)
ax3.set_xlabel('CCO Donante Particulares')
ax3.set_ylabel('Cantidad de donantes')
ax3.set_title("Origen donación: Eventos, Actividades y Productos 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=15)
plt.xticks(rotation=0)
fig.savefig('./images/empresas/empresas_descriptivo_4_1.png')
# plt.show()

# Top centro de costo: destino de cada donacion año a año
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante empresas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_cco_2018', 'cod_cco_2018'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2018'] == 4.0]
# print(df1)
df1['nom_cco'] = ['Fondo Nogal']
df1.drop(columns=['categ_cco_2018', 'cod_cco_2018'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax1, legend=False)
ax1.set_xlabel('')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Origen donación: Mantenimiento de Centros 2018")
ax2 = fig.add_subplot(gs[0, 1])
df1 = df.groupby(['categ_cco_2019', 'cod_cco_2019'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2019'] == 4.0]
# print(df1)
df1['nom_cco'] = ['C Mantenimiento Particulares']
df1.drop(columns=['categ_cco_2019', 'cod_cco_2019'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax2, legend=False)
ax2.set_xlabel('')
ax2.set_ylabel('Cantidad de donantes')
ax2.set_title("Origen donación: Mantenimiento de Centros 2019")
ax3 = fig.add_subplot(gs[1, :])
df1 = df.groupby(['categ_cco_2020', 'cod_cco_2020'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2020'] == 4.0]
# print(df1)
df1['nom_cco'] = ['C Mantenimiento Numerarias', 'C Mantenimiento Particulares']
df1.drop(columns=['categ_cco_2020', 'cod_cco_2020'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10), legend=False)
ax3.set_xlabel('Mantenimiento de Centros')
ax3.set_ylabel('Cantidad de donantes')
ax3.set_title("Origen donación: Mantenimiento de Centros 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=15)
plt.xticks(rotation=0)
fig.savefig('./images/empresas/empresas_descriptivo_4_2.png')
# plt.show()

# Top centro de costo: destino de cada donacion año a año
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante empresas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_cco_2018', 'cod_cco_2018'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2018'] == 22.0]
# print(df1)
df1['nom_cco'] = ['Limmat Donaciones']
df1.drop(columns=['categ_cco_2018', 'cod_cco_2018'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax1, legend=False)
ax1.set_xlabel('')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Origen donación: Donante Particulares 2018")
ax2 = fig.add_subplot(gs[0, 1])
df1 = df.groupby(['categ_cco_2019', 'cod_cco_2019'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2019'] == 22.0]
# print(df1)
df1['nom_cco'] = ['Becas JUV', 'Limmat Donaciones']
df1.drop(columns=['categ_cco_2019', 'cod_cco_2019'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax2, legend=False)
ax2.set_xlabel('')
ax2.set_ylabel('Cantidad de donantes')
ax2.set_title("Origen donación: Donante Particulares 2019")
ax3 = fig.add_subplot(gs[1, :])
df1 = df.groupby(['categ_cco_2020', 'cod_cco_2020'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2020'] == 22.0]
# print(df1)
df1['nom_cco'] = ['Becas JUV', 'Limmat Donaciones', 'F Particulares']
df1.drop(columns=['categ_cco_2020', 'cod_cco_2020'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10), legend=False)
ax3.set_xlabel('Donante Particulares')
ax3.set_ylabel('Cantidad de donantes')
ax3.set_title("Origen donación: Donante Particulares 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=15)
plt.xticks(rotation=0)
fig.savefig('./images/empresas/empresas_descriptivo_4_3.png')
# plt.show()

# Top centro de costo: destino de cada donacion año a año
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante empresas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_cco_2018', 'cod_cco_2018'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2018'] == 23.0]
# print(df1)
df1['nom_cco'] = ['Empresas Nacional', 'Limmat Ingresos']
df1.drop(columns=['categ_cco_2018', 'cod_cco_2018'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax1, legend=False, figsize=(20, 10))
ax1.set_xlabel('')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Origen donación: Donante Empresas 2018")
ax2 = fig.add_subplot(gs[0, 1])
df1 = df.groupby(['categ_cco_2019', 'cod_cco_2019'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2019'] == 23.0]
# print(df1)
df1['nom_cco'] = ['P Empresas']
df1.drop(columns=['categ_cco_2019', 'cod_cco_2019'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax2, legend=False)
ax2.set_xlabel('')
ax2.set_ylabel('Cantidad de donantes')
ax2.set_title("Origen donación: Donante Empresas 2019")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=15)
plt.xticks(rotation=0)
fig.savefig('./images/empresas/empresas_descriptivo_4_4.png')

# cuantos donaron mas de 1 vez
# cuantas cooperadoras donaron más de a una causa
d_2018 = d_2018.merge(df, on='cod_ter', how='inner')
d_2018 = d_2018.groupby(['cod_ter', 'categoria_suc'])['categoria_suc'].count(
).sort_values(ascending=False).to_frame()
n_donantes_2018 = len(d_2018)
d_2018.rename(columns={'categoria_suc': 'n_donacion'}, inplace=True)
d_2018.reset_index(inplace=True)
d_2018 = d_2018.groupby(['cod_ter'])['cod_ter'].count(
).sort_values(ascending=False).to_frame()
d_2018.rename(columns={'cod_ter': 'n_donacion'}, inplace=True)
index_names = d_2018[d_2018['n_donacion'] == 1].index
d_2018.drop(index_names, inplace=True)
n_donantes_causas_2018 = len(d_2018)
# cuantas cooperadoras donaron más de a una causa
d_2019 = d_2019.merge(df, on='cod_ter', how='inner')
d_2019 = d_2019.groupby(['cod_ter', 'categoria_suc'])['categoria_suc'].count(
).sort_values(ascending=False).to_frame()
n_donantes_2019 = len(d_2019)
d_2019.rename(columns={'categoria_suc': 'n_donacion'}, inplace=True)
d_2019.reset_index(inplace=True)
d_2019 = d_2019.groupby(['cod_ter'])['cod_ter'].count(
).sort_values(ascending=False).to_frame()
d_2019.rename(columns={'cod_ter': 'n_donacion'}, inplace=True)
index_names = d_2019[d_2019['n_donacion'] == 1].index
d_2019.drop(index_names, inplace=True)
n_donantes_causas_2019 = len(d_2019)
# cuantas cooperadoras donaron más de a una causa
d_2020 = d_2020.merge(df, on='cod_ter', how='inner')
d_2020 = d_2020.groupby(['cod_ter', 'categoria_suc'])['categoria_suc'].count(
).sort_values(ascending=False).to_frame()
n_donantes_2020 = len(d_2020)
d_2020.rename(columns={'categoria_suc': 'n_donacion'}, inplace=True)
d_2020.reset_index(inplace=True)
d_2020 = d_2020.groupby(['cod_ter'])['cod_ter'].count(
).sort_values(ascending=False).to_frame()
d_2020.rename(columns={'cod_ter': 'n_donacion'}, inplace=True)
index_names = d_2020[d_2020['n_donacion'] == 1].index
d_2020.drop(index_names, inplace=True)
n_donantes_causas_2020 = len(d_2020)
# dataframe y descripivo
data = {'total_donantes':  [n_donantes_2018, n_donantes_2019, n_donantes_2020],
        'donaciones a más de un destino': [n_donantes_causas_2018, n_donantes_causas_2019,
                                           n_donantes_causas_2020]
        }
df_1 = pd.DataFrame(data, index=['2018', '2019', '2020'],
                    columns=['total_donantes', 'donaciones a más de un destino'])
# descriptivo, cuantos donaron a muchas causas año a año
fig, ax = plt.subplots(figsize=(20, 10))
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante cooperadoras')
df_1.plot.bar(ax=ax)
ax.set_xlabel('Año')
ax.set_ylabel('Cantidad de donantes')
ax.set_title("Donantes con más de un destino")
ax.legend(title="Donantes",
          ncol=1, loc='upper left', prop={'size': 10})
plt.xticks(rotation=0)
fig.savefig('./images/empresas/empresas_descriptivo_5.png')
# plt.show()

##########################################################
##### gráficas usando la base de datos master ############
##########################################################

# cargo los archivos de bases de datos de cooperadoras
df = pd.read_csv(
    '../bd_finales/empresas_transaccional_caracterizacion.csv')
# coop.set_index('cod_ter', inplace=True)
print(df.columns.values)
# print(coop)
df['cod_ter'] = df['cod_ter'].astype('int32', copy=False)
# colores de las gráficas
cmap = plt.cm.rainbow
color = cmap(np.linspace(0., 1., 12))

# graficos de tamamno y ciudad, con monto donado
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional donante empresas')
df.groupby(['ciudad']).size().plot.bar(ax=ax1, colors=color,
                                       figsize=(20, 10))
ax1.set_xlabel('Ciudad')
ax1.set_ylabel('Número de donantes (empresas)')
ax1.set_title("¿De qué ciudad son?")
df.groupby(['tamano']).size().plot.bar(ax=ax2, colors=color,
                                       figsize=(20, 10))
ax2.set_xlabel('Tamaño')
ax2.set_ylabel('Número de donantes (empresas)')
ax2.set_title("Tamaño de las Empresas Donantes")
df.groupby(['tamano'])['donacion_total'].sum().plot.bar(ax=ax3, colors=color,
                                                        figsize=(20, 10))
ax3.set_xlabel('Tamaño')
ax3.set_ylabel('Monto donado en 00.000.000 COP')
ax3.set_title("Tamaño del Donante empresas VS el monto total donado")
df.groupby(['tamano', 'recurrencia_prom'])['donacion_total'].sum().plot.bar(
    ax=ax4, colors=color, figsize=(20, 10))
ax4.set_xlabel('Tamaño y Recurrencia')
ax4.set_ylabel('Monto donado en 0.000.000 COP')
ax4.set_title("Tamaño y Recurrencia VS monto total donado")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=0)
plt.xticks(rotation=10)
fig.savefig('./images/empresas/empresas_descriptivo_2.png')

# gráficos de ventas
fig, (ax2, ax3) = plt.subplots(1, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional donante empresas')
df.groupby(['ventas']).size().sort_values(ascending=False).plot.bar(
    ax=ax2, colors=color, figsize=(20, 10))
ax2.set_xlabel('Rango de Ventas')
ax2.set_ylabel('Número de donantes (empresas)')
ax2.set_title("Rango de ventas de las Empresas Donantes")
df.groupby(['ventas'])['donacion_total'].sum().sort_values(ascending=False).plot.bar(
    ax=ax3, colors=color, figsize=(20, 10))
ax3.set_xlabel('Rango de Ventas')
ax3.set_ylabel('Monto donado en 00.000.000 COP')
ax3.set_title("Rango de ventas de la empresa VS el monto total donado")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=20)
fig.savefig('./images/empresas/empresas_descriptivo_5.png')

# aderencia con la causa y los montos donados
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional donante empresas')
df.groupby(['misma_sucursal']).size().plot.pie(ax=ax1,
                                               autopct='%1.1f%%',
                                               counterclock=False)
ax1.set_title("Fidelización del donante con el destino")
df.groupby(['misma_sucursal'])[
    'donacion_total'].sum().plot.bar(ax=ax2)
ax2.set_xlabel('')
ax2.set_ylabel('Monto donado en 0.000.000 COP')
ax2.set_title("Monto total donado recibido por donantes fidelizados y no")
df.groupby(['misma_causa']).size().plot.pie(ax=ax3, figsize=(20, 10),
                                            autopct='%1.1f%%',
                                            counterclock=False)
ax3.set_title("¿La donación tuve el mismo origen durante los 3 años?")
df.groupby(['misma_causa'])[
    'donacion_total'].sum().plot.bar(ax=ax4)
ax4.set_xlabel('¿mismo origen del dinero durante los 3 años?')
ax4.set_ylabel('Monto donado en 0.000.000 COP')
ax4.set_title("Monto total donado recibido de un mismo destino")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=0)
fig.savefig('./images/empresas/empresas_descriptivo_7.png')
# plt.show()

# top 15 de donantes más recurrentes y que más donan $
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Top 15 de donantes empresas que más...')
df2 = df.sort_values('donacion_total', ascending=False)
df2 = df2[['donacion_total', 'nombre']].set_index('nombre').head(15)
df2.plot.bar(ax=ax1, figsize=(20, 10), legend=False)
ax1.set_xlabel('Nombre de la empresa donante')
ax1.set_ylabel('Monto donado en 00.000.000 COP')
ax1.set_title("Top 15 acumulado de donación $ 2018-2020")
df2 = df.sort_values('recurrencia_prom', ascending=False)
df2 = df2[['recurrencia_prom', 'nombre']].set_index('nombre').head(15)
df2.plot.bar(ax=ax2, figsize=(20, 10), legend=False)
ax2.set_xlabel('Nombre de la empresa donante')
ax2.set_ylabel('Recurrencia promedio de su donación')
ax2.set_title("Top 15 acumulado de donantes más recurrentes en promedio")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=20)
fig.savefig('./images/empresas/empresas_descriptivo_13.png')
# plt.show()

# recurrencia promedio de donaciones y recurrencia vs donaciones totales
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional donante empresas')
bins = [1, 3, 6, 9, 12, 15, 18]
names = ['1-3', '4-6', '7-9', '10-12', '13-15', '16-18']
df['rango_n_transac'] = pd.cut(df['recurrencia_prom'], bins, labels=names)
df.groupby(['rango_n_transac']).size().plot.bar(ax=ax1, figsize=(20, 10),
                                                colors=color)
ax1.set_xlabel('Número de transacciones promedio al año')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Número promedio de transacciones al año de donantes")
df.groupby(['rango_n_transac'])['donacion_total'].sum().plot.bar(ax=ax2,
                                                                 figsize=(
                                                                     20, 10),
                                                                 colors=color)
ax2.set_ylabel('Monto donado en 00.000.000 COP')
ax2.set_xlabel('Número de transacciones promedio al año')
ax2.set_title("Monto total acumulado por transacciones")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=0)
fig.savefig('./images/empresas/empresas_descriptivo_14.png')
# plt.show()

plt.close('all')
