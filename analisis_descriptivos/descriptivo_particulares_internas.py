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
    '../bd_finales/part_int_transaccional_caracterizacion_ano_ano.csv')
# coop.set_index('cod_ter', inplace=True)
d_2018 = pd.read_csv(
    '../data/contabilidad_limpios/Auxiliar_Donantes_2018.csv')
d_2019 = pd.read_csv(
    '../data/contabilidad_limpios/Auxiliar_Donantes_2019.csv')
d_2020 = pd.read_csv(
    '../data/contabilidad_limpios/Auxiliar_Donantes_2020.csv')
# print(df.columns.values)

df['profesion'] = df['profesion'].replace('Hogar', 'Ama de casa')
df['profesion'] = df['profesion'].replace(
    'Administradora de empresas', 'Administradora')
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

# tendencia de donación año a año en monto de donación
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional del donante particulares internas')
df[['total_2018', 'total_2019', 'total_2020']
   ].sum().plot(ax=ax1, figsize=(20, 10))
ax1.set_xlabel('Año')
ax1.set_ylabel('Monto donado en 00.000.000 COP')
ax1.set_title("Tendencia del monto de donación acumulado año a año")
df.groupby(['centro'])[['total_2018', 'total_2019',
                        'total_2020']].sum().plot(ax=ax2)
ax2.set_xlabel('Centro cultural')
ax2.set_ylabel('Monto donado en 0.000.000 COP')
ax2.set_title('Tendencia año a año del monto donado por centro')
plt.xticks(rotation=30)
fig.savefig('./images/particulares_internas/part_int_descriptivo_1.png')
# plt.show()

# sucrsal fuente de cada donacion año a año
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional del donante particulares internas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_suc_2018'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False)
df1['sucursal'] = ['no aplica', 'centros', 'ACF', 'labores sociales']
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
df1['sucursal'] = ['no aplica', 'centros', 'ACF', 'labores sociales']
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
df1['sucursal'] = ['labores sociales', 'no aplica', 'ACF', 'centros']
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
fig.savefig('./images/particulares_internas/part_int_descriptivo_3.png')
# plt.show()

# Top sucursal: centor cultural fuente de cada donacion año a año
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante particulares internas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_suc_2018', 'cod_suc_2018'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_suc_2018'] == 1.0]
# print(df1)
df1['nom_suc'] = ['Cedro', 'Inaya', 'Nogal', 'Portones', 'Torreon', 'Arboleda',
                  'Naval', 'Torr-C.E.']
df1.drop(columns=['categ_suc_2018', 'cod_suc_2018'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax1, legend=False)
ax1.set_xlabel('Destino Donación:')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Destino Donación: Centro Cultural 2018")
ax2 = fig.add_subplot(gs[0, 1])
df1 = df.groupby(['categ_suc_2019', 'cod_suc_2019'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_suc_2019'] == 1.0]
# print(df1)
df1['nom_suc'] = ['Cedro', 'Nogal', 'Portones', 'Torreon', 'Arboleda',
                  'Naval', 'Torr-C.E.']
df1.drop(columns=['categ_suc_2019', 'cod_suc_2019'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax2, figsize=(20, 10), legend=False)
ax2.set_xlabel('Destino Donación:')
ax2.set_ylabel('Cantidad de donantes')
ax2.set_title("Destino Donación: Centro Cultural 2019")
ax3 = fig.add_subplot(gs[1, :])
df1 = df.groupby(['categ_suc_2020', 'cod_suc_2020'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_suc_2020'] == 1.0]
# print(df1)
df1['nom_suc'] = ['Cedro', 'Nogal', 'Portones', 'Arboleda',
                  'Naval']
df1.drop(columns=['categ_suc_2020', 'cod_suc_2020'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10), legend=False)
ax3.set_xlabel('Labor Social')
ax3.set_ylabel('Cantidad de donantes')
ax3.set_title("Destino Donación: Labor Social 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=15)
fig.savefig('./images/particulares_internas/part_int_descriptivo_3_1.png')
# plt.show()

gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante particulares internas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_suc_2018', 'cod_suc_2018'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_suc_2018'] == 3.0]
# print(df1)
df1['nom_suc'] = ['ICSEF', 'Casanueva (JUV)', 'Fondo Sacerdotes']
df1.drop(columns=['categ_suc_2018', 'cod_suc_2018'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax1, legend=False)
ax1.set_xlabel('Destino Donación:')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Destino Donación: Centro Cultural 2018")
ax2 = fig.add_subplot(gs[0, 1])
df1 = df.groupby(['categ_suc_2019', 'cod_suc_2019'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_suc_2019'] == 3.0]
# print(df1)
df1['nom_suc'] = ['ICSEF', 'Casanueva (JUV)', 'Fondo Sacerdotes']
df1.drop(columns=['categ_suc_2019', 'cod_suc_2019'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax2, figsize=(20, 10), legend=False)
ax2.set_xlabel('Destino Donación:')
ax2.set_ylabel('Cantidad de donantes')
ax2.set_title("Destino Donación: Centro Cultural 2019")
ax3 = fig.add_subplot(gs[1, :])
df1 = df.groupby(['categ_suc_2020', 'cod_suc_2020'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_suc_2020'] == 3.0]
# print(df1)
df1['nom_suc'] = ['ICSEF', 'Casanueva (JUV)', 'Fondo Sacerdotes', 'APoyo Venezuela',
                  'Mujeres Escasos Rec.']
df1.drop(columns=['categ_suc_2020', 'cod_suc_2020'], inplace=True)
df1.set_index('nom_suc', inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10), legend=False)
ax3.set_xlabel('Labor Social')
ax3.set_ylabel('Cantidad de donantes')
ax3.set_title("Destino Donación: Labor Social 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=15)
fig.savefig('./images/particulares_internas/part_int_descriptivo_3_2.png')
# plt.show()

# centro de costos destino de cada donacion
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional del donante particulares internas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_cco_2018'])['cod_ter'].count().to_frame(
).sort_values('cod_ter', ascending=False).reset_index()
df1['cco'] = ['No Aplica', 'Eventos/Act/Prod', 'D Cooperadoras',
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
df1['cco'] = ['No Aplica', 'D Cooperadoras', 'Eventos/Act/Prod',
              'Manten centros', 'D Particulares']
df1.drop(columns=['categ_cco_2019'], inplace=True)
df1.set_index('cco', inplace=True)
df1.plot.bar(ax=ax2, figsize=(20, 10), legend=False)
ax2.set_xlabel('Origen de la Donación')
ax2.set_ylabel('Cantidad de donantes')
ax2.set_title("Origen de cada Donación 2019")
ax3 = fig.add_subplot(gs[1, :])  # row 1, span all columns
df1 = df.groupby(['categ_cco_2020'])['cod_ter'].count().to_frame(
).sort_values('cod_ter', ascending=False).reset_index()
df1['cco'] = ['No Aplica', 'D Particulares', 'D Cooperadoras',
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
fig.savefig('./images/particulares_internas/part_int_descriptivo_4.png')
# plt.show()

# destino de cada donacion año a año
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante particulares internas')
ax1 = fig.add_subplot(gs[0, 0])
df1 = df.groupby(['categ_cco_2019', 'cod_cco_2019'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2019'] == 4.0]
# print(df1)
df1['nom_cco'] = ['C Mantenimiento GP', 'C Mantenimiento GP']
df1.drop(columns=['categ_cco_2019', 'cod_cco_2019'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax2, legend=False)
ax1.set_xlabel('')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Origen donación: Mantenimiento de Centros 2019")
ax2 = fig.add_subplot(gs[0, 1])
df1 = df.groupby(['categ_cco_2019', 'cod_cco_2019'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2019'] == 4.0]
# print(df1)
df1['nom_cco'] = ['C Mantenimiento GP', 'C Mantenimiento GP']
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
df1['nom_cco'] = ['C Mantenimiento GP']
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
fig.savefig('./images/particulares_internas/part_int_descriptivo_4_1.png')
# plt.show()

# destino de cada donacion año a año
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante particulares internas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_cco_2018', 'cod_cco_2018'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2018'] == 6.0]
# print(df1)
df1['nom_cco'] = ['Pashminarte', 'Clasicos Amor',
                  'Bonos Donacion', 'Evento Solidario',
                  'Cantarte', 'Libros-Navidad']
df1.drop(columns=['categ_cco_2018', 'cod_cco_2018'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax1, legend=False)
ax1.set_xlabel('')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Origen donación: Eventos, Actividades y Productos 2018")
ax2 = fig.add_subplot(gs[0, 1])
df1 = df.groupby(['categ_cco_2019', 'cod_cco_2019'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2019'] == 6.0]
# print(df1)
df1['nom_cco'] = ['Pashmi', 'Clasco Amor', 'Bono Donacion',
                  'F libros-nav.', 'F CD-Nav', 'F taller emprendimiento',
                  'F sem imagen', 'F ciclopaseo', 'F acción gracias']
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
df1['nom_cco'] = ['Bono Donacion', 'Curso Historia Arte',
                  'F libros-nav.']
df1.drop(columns=['categ_cco_2020', 'cod_cco_2020'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10), legend=False)
ax3.set_xlabel('Tipo de Donante Particulares')
ax3.set_ylabel('Cantidad de donantes')
ax3.set_title("Origen donación: Particular 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=15)
plt.xticks(rotation=0)
fig.savefig('./images/particulares_internas/part_int_descriptivo_4_2.png')
# plt.show()

# destino de cada donacion año a año
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante particulares internas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_cco_2018', 'cod_cco_2018'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2018'] == 21.0]
# print(df1)
df1['nom_cco'] = ['Cooperadora', 'Donación cooperadoras casanueva']
df1.drop(columns=['categ_cco_2018', 'cod_cco_2018'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax1, legend=False)
ax1.set_xlabel('')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Origen donación: Cooperadora 2018")
ax2 = fig.add_subplot(gs[0, 1])
df1 = df.groupby(['categ_cco_2019', 'cod_cco_2019'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2019'] == 21.0]
# print(df1)
df1['nom_cco'] = ['F. Cooperadoras', 'P. Cooperadoras']
df1.drop(columns=['categ_cco_2019', 'cod_cco_2019'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax2, legend=False)
ax2.set_xlabel('')
ax2.set_ylabel('Cantidad de donantes')
ax2.set_title("Origen donación: Cooperadora 2019")
ax3 = fig.add_subplot(gs[1, :])
df1 = df.groupby(['categ_cco_2020', 'cod_cco_2020'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2020'] == 21.0]
# print(df1)
df1['nom_cco'] = ['F. Cooperadoras', 'P. Cooperadoras']
df1.drop(columns=['categ_cco_2020', 'cod_cco_2020'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10), legend=False)
ax3.set_xlabel('Tipo de Donante Cooperadora')
ax3.set_ylabel('Cantidad de donantes')
ax3.set_title("Origen donación: Cooperadora 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=15)
plt.xticks(rotation=0)
fig.savefig('./images/particulares_internas/part_int_descriptivo_4_3.png')
# plt.show()

# destino de cada donacion año a año
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante particulares internas')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['categ_cco_2018', 'cod_cco_2018'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2018'] == 22.0]
# print(df1)
df1['nom_cco'] = ['particulares', 'Donaciones Juventus']
df1.drop(columns=['categ_cco_2018', 'cod_cco_2018'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax1, legend=False)
ax1.set_xlabel('')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Origen donación: Eventos, Actividades y Productos 2018")
ax2 = fig.add_subplot(gs[0, 1])
df1 = df.groupby(['categ_cco_2019', 'cod_cco_2019'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2019'] == 22.0]
# print(df1)
df1['nom_cco'] = ['Donaciones Juventus', 'F Particulares', 'P Particulares']
df1.drop(columns=['categ_cco_2019', 'cod_cco_2019'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax2, legend=False)
ax2.set_xlabel('')
ax2.set_ylabel('Cantidad de donantes')
ax2.set_title("Origen donación: Eventos, Actividades y Productos 2019")
ax3 = fig.add_subplot(gs[1, :])
df1 = df.groupby(['categ_cco_2020', 'cod_cco_2020'])[
    'cod_ter'].count().reset_index()
df1 = df1.loc[df1['categ_cco_2020'] == 22.0]
# print(df1)
df1['nom_cco'] = ['Limmat Donaciones', 'Crowfunding Juventus', 'P. Particulares']
df1.drop(columns=['categ_cco_2020', 'cod_cco_2020'], inplace=True)
df1.set_index('nom_cco', inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10), legend=False)
ax3.set_xlabel('Tipo de Donante Particulares')
ax3.set_ylabel('Cantidad de donantes')
ax3.set_title("Origen donación: Particular 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=15)
plt.xticks(rotation=0)
fig.savefig('./images/particulares_internas/part_int_descriptivo_4_4.png')
# plt.show()

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
fig.savefig('./images/particulares_internas/part_int_descriptivo_5.png')
# plt.show()

# centro de costos destino de cada donacion por profesion
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional donante particulares internos')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['profesion', 'cod_suc_2018'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).reset_index()
df1 = df1.loc[df1['profesion'] == 'Abogada']
# print(df1)
df1['nom_suc'] = ['NA', 'Torreon', 'Nogal', 'Cedro', 'Portones', 'ACF',
                  'Narval', 'Mirabal']
df1.drop(columns=['profesion', 'cod_suc_2018'], inplace=True)
df1.set_index(['nom_suc'], inplace=True)
df1.plot.bar(ax=ax1, figsize=(20, 10),
             legend=False)
ax1.set_xlabel('Destino donación')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Abogadas y su destino de donación 2018")
ax2 = fig.add_subplot(gs[0, 1])  # row 0, col
df1 = df.groupby(['profesion', 'cod_suc_2019'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).reset_index()
df1 = df1.loc[df1['profesion'] == 'Abogada']
# print(df1)
df1['nom_suc'] = ['Torreon', 'NA', 'Nogal', 'Arboleda',
                  'Cedro', 'Portones', 'ACF', 'Serrania',
                  'Casanueva']
df1.drop(columns=['profesion', 'cod_suc_2019'], inplace=True)
df1.set_index(['nom_suc'], inplace=True)
df1.plot.bar(ax=ax2, figsize=(20, 10),
             legend=False)
ax2.set_xlabel('Destino donación')
ax2.set_ylabel('Cantidad de donantes')
ax2.set_title("Abogadas y su destino de donación 2019")
ax3 = fig.add_subplot(gs[1, :])  # row 1, span all columns
df1 = df.groupby(['profesion', 'cod_suc_2020'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).reset_index()
df1 = df1.loc[df1['profesion'] == 'Abogada']
# print(df1)
df1['nom_suc'] = ['Portones', 'NA', 'Nogal', 'Cedro', 'Arboleda', 'Torreon CE',
                  'Protones', 'Mujeres Escasos Rec.']
df1.drop(columns=['profesion', 'cod_suc_2020'], inplace=True)
df1.set_index(['nom_suc'], inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10),
             legend=False)
ax3.set_xlabel('Destino donación')
ax3.set_ylabel('Cantidad de donantes')
ax3.set_title("Abogadas y su destino de donación 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=20)
fig.savefig('./images/particulares_internas/part_int_descriptivo_12_1.png')
# plt.show()

# centro de costos destino de cada donacion por profesion
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional donante particulares internos')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['profesion', 'cod_suc_2018'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).reset_index()
df1 = df1.loc[df1['profesion'] == 'Administradora']
# print(df1)
df1['nom_suc'] = ['NA', 'Torreon', 'Cedro', 'Torreon C.E.', 'Arboleda']
df1.drop(columns=['profesion', 'cod_suc_2018'], inplace=True)
df1.set_index(['nom_suc'], inplace=True)
df1.plot.bar(ax=ax1, figsize=(20, 10),
             legend=False)
ax1.set_xlabel('Destino donación')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Administradoras y su destino de donación 2018")
ax2 = fig.add_subplot(gs[0, 1])  # row 0, col
df1 = df.groupby(['profesion', 'cod_suc_2019'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).reset_index()
df1 = df1.loc[df1['profesion'] == 'Administradora']
# print(df1)
df1['nom_suc'] = ['NA', 'Cedro', 'Torreon', 'Arboleda',
                  'Mujeres Esc. Recur.', 'Casanueva',
                  'Torreon C.E.']
df1.drop(columns=['profesion', 'cod_suc_2019'], inplace=True)
df1.set_index(['nom_suc'], inplace=True)
df1.plot.bar(ax=ax2, figsize=(20, 10),
             legend=False)
ax2.set_xlabel('Destino donación')
ax2.set_ylabel('Cantidad de donantes')
ax2.set_title("Administradoras y su destino de donación 2019")
ax3 = fig.add_subplot(gs[1, :])  # row 1, span all columns
df1 = df.groupby(['profesion', 'cod_suc_2020'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).reset_index()
df1 = df1.loc[df1['profesion'] == 'Administradora']
# print(df1)
df1['nom_suc'] = ['NA', 'Cedro', 'Arboleda', 'Torreon',
                  'Mujeres Escasos Rec.', 'Fondo Sacerdotes',
                  'Casanueva', 'Nogal']
df1.drop(columns=['profesion', 'cod_suc_2020'], inplace=True)
df1.set_index(['nom_suc'], inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10),
             legend=False)
ax3.set_xlabel('Destino donación')
ax3.set_ylabel('Cantidad de donantes')
ax3.set_title("Administradoras y su destino de donación 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=20)
fig.savefig('./images/particulares_internas/part_int_descriptivo_12_2.png')
# plt.show()

# centro de costos destino de cada donacion por profesion
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional donante particulares internos')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df1 = df.groupby(['profesion', 'cod_suc_2018'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).reset_index()
df1 = df1.loc[df1['profesion'] == 'Ama de casa']
# print(df1)
df1['nom_suc'] = ['Torreon', 'Cedro', 'Serrania', 'NA',
                  'Nogal']
df1.drop(columns=['profesion', 'cod_suc_2018'], inplace=True)
df1.set_index(['nom_suc'], inplace=True)
df1.plot.bar(ax=ax1, figsize=(20, 10),
             legend=False)
ax1.set_xlabel('Destino donación')
ax1.set_ylabel('Cantidad de donantes')
ax1.set_title("Amas de casa y su destino de donación 2018")
ax2 = fig.add_subplot(gs[0, 1])  # row 0, col
df1 = df.groupby(['profesion', 'cod_suc_2019'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).reset_index()
df1 = df1.loc[df1['profesion'] == 'Ama de casa']
# print(df1)
df1['nom_suc'] = ['Torreon', 'NA', 'Serrania',
                  'Nogal', 'Cedro']
df1.drop(columns=['profesion', 'cod_suc_2019'], inplace=True)
df1.set_index(['nom_suc'], inplace=True)
df1.plot.bar(ax=ax2, figsize=(20, 10),
             legend=False)
ax2.set_xlabel('Destino donación')
ax2.set_ylabel('Cantidad de donantes')
ax2.set_title("Amas de casa y su destino de donación 2019")
ax3 = fig.add_subplot(gs[1, :])  # row 1, span all columns
df1 = df.groupby(['profesion', 'cod_suc_2020'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).reset_index()
df1 = df1.loc[df1['profesion'] == 'Ama de casa']
# print(df1)
df1['nom_suc'] = ['NA', 'Torreon', 'Serrania',
                  'Nogal', 'Cedro']
df1.drop(columns=['profesion', 'cod_suc_2020'], inplace=True)
df1.set_index(['nom_suc'], inplace=True)
df1.plot.bar(ax=ax3, figsize=(20, 10),
             legend=False)
ax3.set_xlabel('Destino donación')
ax3.set_ylabel('Cantidad de donantes')
ax3.set_title("Amas de casa y su destino de donación 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=20)
fig.savefig('./images/particulares_internas/part_int_descriptivo_12_3.png')
# plt.show()


##########################################################
##### gráficas usando la base de datos master ############
##########################################################

# cargo los archivos de bases de datos de cooperadoras
df = pd.read_csv(
    '../bd_finales/part_int_transaccional_caracterizacion.csv')
# coop.set_index('cod_ter', inplace=True)
print(df.columns.values)
# print(coop)
df['cod_ter'] = df['cod_ter'].astype('int32', copy=False)
df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'],
                                        infer_datetime_format=True)
now = pd.Timestamp('now')
df['edad'] = (now - df['fecha_nacimiento']).astype('<m8[Y]')
df['prom_donacion_mes'] = df['donacion_total'] / 32
# colores de las gráficas
cmap = plt.cm.rainbow
color = cmap(np.linspace(0., 1., 12))

# gráficos sobre información caracteristica vs transaccional

# graficos de edad y relación con monto donado
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional donante particulares internos')
bins = [0, 18, 30, 40, 50, 60, 70, np.inf]
names = ['<18', '19-30', '31-40', '41-50', '51-60', '61-70', '+71']
df['rango_edades'] = pd.cut(df['edad'], bins, labels=names)
df.groupby(['rango_edades']).size().plot.bar(ax=ax1, figsize=(20, 10),
                                             colors=color)
ax1.set_xlabel('')
ax1.set_ylabel('Número de donantes')
ax1.set_title("Rango de edad del donante cooperadoras")
df.groupby(['rango_edades'])['donacion_total'].sum().plot.bar(ax=ax2, figsize=(20, 10),
                                                              colors=color)
ax2.set_xlabel('')
ax2.set_ylabel('Monto donado en 0.000.000 COP')
ax2.set_title("Rango de edad VS total de donación acumulada")
df.groupby(['rango_edades'])['prom_donacion_mes'].sum().plot.bar(ax=ax3, figsize=(20, 10),
                                                                 colors=color)
ax3.set_xlabel('Rango de edades (años)')
ax3.set_ylabel('Donación promedio mensual')
ax3.set_title("Rango de edad VS promedio donación mensual")
df.groupby(['ciudad']).size().plot.bar(ax=ax4, colors=color,
                                       figsize=(20, 10))
ax4.set_xlabel('Ciudad')
ax4.set_ylabel('Número de donantes (personas)')
ax4.set_title("¿De qué ciudad son?")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=0)
plt.xticks(rotation=30)
fig.savefig('./images/particulares_internas/part_int_descriptivo_2.png')
# plt.show()

# aderencia con la causa y los montos donados
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional donante particulares internos')
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
fig.savefig('./images/particulares_internas/part_int_descriptivo_7.png')
# plt.show()

# estado civil del donante
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional donante particulares internos')
df.groupby(['estado_civil']).size().plot.bar(ax=ax1, colors=color,
                                             figsize=(20, 10))
ax1.set_xlabel('Estado Civil')
ax1.set_ylabel('Número de donantes (personas)')
ax1.set_title("Estado civil")
df.groupby(['estado_civil'])[
    'prom_donacion_mes'].sum().plot.bar(ax=ax2, colors=color)
ax2.set_xlabel('Estado Civil')
ax2.set_ylabel('Monto mensual promedio COP')
ax2.set_title("Estado civil vs promedio mensual donado")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=30)
fig.savefig('./images/particulares_internas/part_int_descriptivo_8.png')
# plt.show()

# informacion del centro
fig, ax = plt.subplots(figsize=(20, 10))
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante cooperadoras')
df.groupby(['centro', 'rango_edades'])[
    'rango_edades'].size().plot.bar(ax=ax, colors=color)
ax.set_xlabel('Centro Cultural y Rango de Edad')
ax.set_ylabel('Cantidad de donantes (personas)')
ax.set_title("Rango de edad del donante por centro")
plt.xticks(rotation=75)
fig.savefig('./images/particulares_internas/part_int_descriptivo_9.png')
# plt.show()

# informacion del centro cultural
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional donante particulares internos')
df.groupby(['centro'])['donacion_total'].sum().plot.bar(ax=ax1, figsize=(20, 10),
                                                        colors=color)
ax1.set_xlabel('Centro Cultural')
ax1.set_ylabel('Monto donado en 00.000.000 COP')
ax1.set_title("Monto en pesos acumulado por centro 2018-2020")
df.groupby(['centro']).size().plot.bar(ax=ax2, figsize=(20, 10),
                                       colors=color)
ax2.set_xlabel('Centro Cultural')
ax2.set_ylabel('Número de donantes (personas)')
ax2.set_title("Número de donantes por centro")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=30)
fig.savefig('./images/particulares_internas/part_int_descriptivo_10.png')

# informacion del centro cultural
fig, (ax3, ax4) = plt.subplots(1, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional donante particulares internos')
df.groupby(['centro'])['recurrencia_prom'].sum().plot.bar(ax=ax3, figsize=(20, 10),
                                                          colors=color)
fig.suptitle('Insights usando variables transaccionales y profesion')
ax3.set_xlabel('Centro Cultural')
ax3.set_ylabel('N. Transacciones mensuales promedio')
ax3.set_title("Número de transacciones promedio mensual por centro")
df.groupby(['tipo_doc'])['prom_donacion_mes'].sum().plot.bar(ax=ax4, figsize=(20, 10),
                                                             colors=color)
ax4.set_xlabel('Tipo documento')
ax4.set_ylabel('Promedio de donaciones mensuales')
ax4.set_title("Promedio donación mensual vs Tipo documento")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=30)
# plt.xticks(rotation=30)
fig.savefig('./images/particulares_internas/part_int_descriptivo_11.png')
# plt.show()


# informacion de la profesion e insights
fig, (ax1, ax2) = plt.subplots(1, 2)
df['profesion'] = df['profesion'].replace('Hogar', 'Ama de casa')
df['profesion'] = df['profesion'].replace(
    'Administradora de empresas', 'Administradora')
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
fig.suptitle(
    'Insights: información caracteristica vs transaccional donante particulares internos')
df2 = df.groupby(['profesion']).size(
).to_frame().sort_values(0, ascending=False)
df2 = df2.head(15)
print(df2)
df2.plot.bar(ax=ax1, figsize=(20, 10))
ax1.set_xlabel('Profesion')
ax1.set_ylabel('Número de donantes cooperadoras (personas)')
colors = ['blue', 'blue', 'blue', 'blue', 'blue',
          'blue', 'blue', 'blue', 'blue', 'blue',
          'blue', 'blue', 'blue', 'blue', 'blue']
lines = [Line2D([0], [0], color=c, linewidth=2)
         for c in colors]
labels = [
    'Ama de casa', 'Administradora', 'Abogada', 'Médico', 'Psicologa',
    'Economista', 'Profesora', 'Contadora', 'Pensionada',
    'Fisioterapeuta', 'Enfermera', 'Arquitecta', 'Bacteriologa',
    'Odontóloga', 'Comunicadora social'
]
ax1.legend(lines, labels, loc='upper right', prop={'size': 9})
ax1.set_title("Top 15 de profesiones más frecuentes")
df2 = df.groupby(['profesion'])[
    'prom_donacion_mes'].sum().sort_values(0, ascending=False)
df2 = df2.head(15)
print(df2)
df2.plot.bar(ax=ax2, figsize=(20, 10))
ax2.set_xlabel('Profesion')
ax2.set_ylabel('Promedio de donación mensual')
colors = ['blue', 'blue', 'blue', 'blue', 'blue',
          'blue', 'blue', 'blue', 'blue', 'blue',
          'blue', 'blue', 'blue', 'blue', 'blue']
lines = [Line2D([0], [0], color=c, linewidth=2)
         for c in colors]
labels = [
    'Ama de casa', 'Administradora', 'Abogada',
    'Profesora', 'Periodista - exdecana',
    'Terapista de lenguaje', 'Fisioterapeuta',
    'Nutricionista', 'Economista', 'Arquitecta',
    'Ingeniera Quimica', 'Psicologa', 'Ingeniera Civil',
    'Diseñador industrial', 'Médico']
ax2.legend(lines, labels, loc='upper right', prop={'size': 9})
ax2.set_title("Top 15 de profesiones que más donan")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=85)
fig.savefig('./images/particulares_internas/part_int_descriptivo_12.png')
# plt.show()

# top 15 de donantes más recurrentes y que más donan $
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Top 15 de donantes particulares internas que más...')
df2 = df.sort_values('donacion_total', ascending=False)
df2 = df2[['donacion_total', 'cod_ter']].set_index('cod_ter').head(15)
df2.plot.bar(ax=ax1, figsize=(20, 10))
ax1.set_xlabel('Número de documento del donante')
ax1.set_ylabel('Monto donado en 0.000.000 COP')
colors = ['blue', 'blue', 'blue', 'blue', 'blue',
          'blue', 'blue', 'blue', 'blue', 'blue',
          'blue', 'blue', 'blue', 'blue', 'blue']
lines = [Line2D([0], [0], color=c, linewidth=2)
         for c in colors]
labels = [
    'Laila Faour', 'Ruth Marina Naranjo', 'Maria Graciela Plazas',
    'Ana Lucia Medina', 'Alicia Elena Amezquita',
    'Maria Tadea Morales', 'Maria Helena Rodrigues',
    'Maria Gladys Buitrago', 'Maria Nohora Manrique',
    'Gloria Maria Malagon', 'Dolly Velez', 'Fanny Hernández',
    'Sandra Patricia Ortiz', 'Lesly Patricia Linares',
    'Sylvia Cardemil']
ax1.legend(lines, labels, ncol=1, loc='upper right', prop={'size': 9})
ax1.set_title("Top 15 acumulado de donación $ 2018-2020")
df3 = df.sort_values('recurrencia_prom', ascending=False)
df3 = df3[['recurrencia_prom', 'cod_ter']].set_index('cod_ter').head(15)
df3.plot.bar(ax=ax2, figsize=(20, 10))
ax2.set_xlabel('Número de documento del donante')
ax2.set_ylabel('Recurrencia de su donación promedio')
colors = ['blue', 'blue', 'blue', 'blue', 'blue',
          'blue', 'blue', 'blue', 'blue', 'blue',
          'blue', 'blue', 'blue', 'blue', 'blue']
lines = [Line2D([0], [0], color=c, linewidth=2)
         for c in colors]
labels = [
    'Laila Faour', 'Dolly Velez',
    'Maria Nohora Manrique',
    'Gloria Maria Malagon',
    'Ilva Gema Alfonso', 'Maria Graciela Plazas',
    'Zulay Chon Lu', 'Ana Lucia Medina',
    'Sandra Patricia Jarro', 'Patricia Amelia Rojas',
    'Maria Teresa Moreno', 'Maria Enriqueta Moreno',
    'Susana Machado', 'Sonia Cristina Vera',
    'Sandra Patricia Ortiz']
ax2.legend(lines, labels, ncol=1, loc='upper right', prop={'size': 9})
ax2.set_title("Top 15 acumulado de donantes más recurrentes en promedio")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=60)
fig.savefig('./images/particulares_internas/part_int_descriptivo_13.png')
# plt.show()

# recurrencia promedio de donaciones y recurrencia vs donaciones totales
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional donante particulares internos')
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
ax2.set_ylabel('Monto donado en 0.000.000 COP')
ax2.set_xlabel('Número de transacciones promedio al año')
ax2.set_title("Monto total acumulado por transacciones")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=0)
fig.savefig('./images/particulares_internas/part_int_descriptivo_14.png')
# plt.show()
