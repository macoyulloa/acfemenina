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
    '../bd_finales/cooperadoras_transaccional_caracterizacion_ano_ano.csv')
# coop.set_index('cod_ter', inplace=True)
d_2018 = pd.read_csv(
    '../data/contabilidad_limpios/Auxiliar_Donantes_2018.csv')
d_2019 = pd.read_csv(
    '../data/contabilidad_limpios/Auxiliar_Donantes_2019.csv')
d_2020 = pd.read_csv(
    '../data/contabilidad_limpios/Auxiliar_Donantes_2020.csv')
# coop.set_index('cod_ter', inplace=True)
print(df.columns.values)
# print(coop)

# tendencia de donación año a año en monto de donación
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante cooperadoras')
df[['total_2018', 'total_2019', 'total_2020']].sum().plot(ax=ax1, figsize=(20, 10),
                                                          colors=color)
ax1.set_xlabel('Año')
ax1.set_ylabel('Monto donado en miles de millones de pesos')
ax1.set_title("Tendencia del monto de donación acumulado año a año")
df.groupby(['centro'])[['total_2018', 'total_2019',
                        'total_2020']].sum().plot(ax=ax2, colors=color)
ax2.set_xlabel('Centro cultural')
ax2.set_ylabel('Monto donado en miles de millones de pesos')
ax2.set_title('Tendencia año a año del monto donado por centro')
plt.xticks(rotation=30)
fig.savefig('./images/cooperadoras/cooperadoras_descriptivo_1.png')
# plt.show()

# sucrsal fuente de cada donacion año a año
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante cooperadoras')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df.groupby(['categ_suc_2018'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).plot.bar(ax=ax1, figsize=(20, 10),
                                                              colors=color)
ax1.set_xlabel('Sucursal')
ax1.set_ylabel('Número de Donaciones')
ax1.set_title("Sucursal de cada Donación 2018")
colors = ['blue', 'blue', 'blue', 'blue']
lines = [Line2D([0], [0], color=c, linewidth=2)
         for c in colors]
labels = ['0. No aplica', '1. Centros',
          '2. ACF',
          '3. Labores sociales']
ax1.legend(lines, labels, title="Categoría de Sucursales",
           ncol=1, loc='upper right', prop={'size': 8})
ax2 = fig.add_subplot(gs[0, 1])
df.groupby(['categ_suc_2019'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).plot.bar(ax=ax2, figsize=(20, 10),
                                                              colors=color)
ax2.set_xlabel('Sucursal')
ax2.set_ylabel('Número de Donaciones')
ax2.set_title("Sucursal de cada Donación 2019")
colors = ['blue', 'blue', 'blue', 'blue']
lines = [Line2D([0], [0], color=c, linewidth=2)
         for c in colors]
labels = ['0. No aplica', '1. Centros',
          '2. ACF',
          '3. Labores sociales']
ax2.legend(lines, labels, title="Categoría de Sucursales",
           ncol=1, loc='upper right', prop={'size': 8})
ax3 = fig.add_subplot(gs[1, :])
df.groupby(['categ_suc_2020'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).plot.bar(ax=ax3, figsize=(20, 10),
                                                              colors=color)
ax3.set_xlabel('Sucursal')
ax3.set_ylabel('Número de Donaciones')
ax3.set_title("Sucursal de cada Donación 2020")
colors = ['blue', 'blue', 'blue', 'blue']
lines = [Line2D([0], [0], color=c, linewidth=2)
         for c in colors]
labels = ['0. No aplica', '1. Centros',
          '2. ACF',
          '3. Labores sociales']
ax3.legend(lines, labels, title="Categoría de Sucursales",
           ncol=1, loc='upper right', prop={'size': 8})
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=0)
fig.savefig('./images/cooperadoras/cooperadoras_descriptivo_3.png')
# plt.show()

# centro de costos destino de cada donacion
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante cooperadoras')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df.groupby(['categ_cco_2018'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).plot.bar(ax=ax1, figsize=(20, 10),
                                                              colors=color)
ax1.set_xlabel('Centro de Costo')
ax1.set_ylabel('Número de Donaciones')
ax1.set_title("Centros de Costos de cada Donación 2018")
colors = ['blue', 'blue', 'blue', 'blue', 'blue']
lines = [Line2D([0], [0], color=c, linewidth=2)
         for c in colors]
labels = ['0. No aplica', '21. Donante Cooperadoras',
          '22. Donante Particulares',
          '4. Mantenimiento de centros',
          '6. Eventos, Actividades y Productos']
ax1.legend(lines, labels, title="Categoría de Centro de Costos",
           ncol=1, loc='upper right', prop={'size': 8})
ax2 = fig.add_subplot(gs[0, 1])  # row 0, col 1
df.groupby(['categ_cco_2019'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).plot.bar(ax=ax2, figsize=(20, 10),
                                                              colors=color)
ax2.set_xlabel('Centro de Costo')
ax2.set_ylabel('Número de Donaciones')
ax2.set_title("Centros de Costos de cada Donación 2019")
colors = ['blue', 'blue', 'blue', 'blue', 'blue']
lines = [Line2D([0], [0], color=c, linewidth=2)
         for c in colors]
labels = ['0. No aplica', '21. Donante Cooperadoras',
          '22. Donante Particulares',
          '4. Mantenimiento de centros',
          '6. Eventos, Actividades y Productos']
ax2.legend(lines, labels, title="Categoría de Centro de Costos",
           ncol=1, loc='upper right', prop={'size': 8})
ax3 = fig.add_subplot(gs[1, :])  # row 1, span all columns
df.groupby(['categ_cco_2020'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).plot.bar(ax=ax3, figsize=(20, 10),
                                                              colors=color)
ax3.set_xlabel('Centro de Costo')
ax3.set_ylabel('Número de Donaciones')
ax3.set_title("Centros de Costos de cada Donación 2020")
colors = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue']
lines = [Line2D([0], [0], color=c, linewidth=2)
         for c in colors]
labels = ['0. No aplica', '21. Donante Cooperadoras',
          '22. Donante Particulares', '33. Donante Empresas',
          '4. Mantenimiento de centros', '6. Eventos, Actividades y Productos']
ax3.legend(lines, labels, title="Categoría de Centro de Costos",
           ncol=1, loc='upper right', prop={'size': 8})
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=0)
fig.savefig('./images/cooperadoras/cooperadoras_descriptivo_4.png')
# plt.show()

# cuantos donaron mas de 1 vez
# cuantas cooperadoras donaron más de a una causa
d_2018 = d_2018.merge(df, on='cod_ter', how='inner')
d_2018 = d_2018.groupby(['cod_ter', 'categoria_cco'])['categoria_cco'].count(
).sort_values(ascending=False).to_frame()
n_donantes_2018 = len(d_2018)
d_2018.rename(columns={'categoria_cco': 'n_donacion'}, inplace=True)
d_2018.reset_index(inplace=True)
d_2018 = d_2018.groupby(['cod_ter'])['cod_ter'].count(
).sort_values(ascending=False).to_frame()
d_2018.rename(columns={'cod_ter': 'n_donacion'}, inplace=True)
index_names = d_2018[d_2018['n_donacion'] == 1].index
d_2018.drop(index_names, inplace=True)
n_donantes_causas_2018 = len(d_2018)
# cuantas cooperadoras donaron más de a una causa
d_2019 = d_2019.merge(df, on='cod_ter', how='inner')
d_2019 = d_2019.groupby(['cod_ter', 'categoria_cco'])['categoria_cco'].count(
).sort_values(ascending=False).to_frame()
n_donantes_2019 = len(d_2019)
d_2019.rename(columns={'categoria_cco': 'n_donacion'}, inplace=True)
d_2019.reset_index(inplace=True)
d_2019 = d_2019.groupby(['cod_ter'])['cod_ter'].count(
).sort_values(ascending=False).to_frame()
d_2019.rename(columns={'cod_ter': 'n_donacion'}, inplace=True)
index_names = d_2019[d_2019['n_donacion'] == 1].index
d_2019.drop(index_names, inplace=True)
n_donantes_causas_2019 = len(d_2019)
# cuantas cooperadoras donaron más de a una causa
d_2020 = d_2020.merge(df, on='cod_ter', how='inner')
d_2020 = d_2020.groupby(['cod_ter', 'categoria_cco'])['categoria_cco'].count(
).sort_values(ascending=False).to_frame()
n_donantes_2020 = len(d_2020)
d_2020.rename(columns={'categoria_cco': 'n_donacion'}, inplace=True)
d_2020.reset_index(inplace=True)
d_2020 = d_2020.groupby(['cod_ter'])['cod_ter'].count(
).sort_values(ascending=False).to_frame()
d_2020.rename(columns={'cod_ter': 'n_donacion'}, inplace=True)
index_names = d_2020[d_2020['n_donacion'] == 1].index
d_2020.drop(index_names, inplace=True)
n_donantes_causas_2020 = len(d_2020)
# dataframe y descripivo
data = {'total_donantes':  [n_donantes_2018, n_donantes_2019, n_donantes_2020],
        'donantes_a_muchos_centros_costo': [n_donantes_causas_2018, n_donantes_causas_2019,
                                            n_donantes_causas_2020]
        }
df_1 = pd.DataFrame(data, index=['2018', '2019', '2020'],
                    columns=['total_donantes', 'donantes_a_muchos_centros_costo'])
# descriptivo, cuantos donaron a muchas causas año a año
fig, ax = plt.subplots(figsize=(20, 10))
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante cooperadoras')
df_1.plot.bar(ax=ax, colors=color)
ax.set_xlabel('Año')
ax.set_ylabel('Cantidad de donantes')
ax.set_title("Donantes cooperadoras que donaron a más de una causa")
ax.legend(title="Donantes",
          ncol=1, loc='upper left', prop={'size': 10})
plt.xticks(rotation=0)
fig.savefig('./images/cooperadoras/cooperadoras_descriptivo_5.png')
# plt.show()

# centro de costos destino de cada donacion por profesion
gs = gridspec.GridSpec(2, 2)
fig = plt.figure()
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante cooperadoras')
ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
df.groupby(['profesion', 'categ_cco_2018'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).head(10).plot.bar(ax=ax1, figsize=(20, 10),
                                                                       colors=color)
ax1.set_xlabel('Profesion / Centro de Costo')
ax1.set_ylabel('Número de Donaciones')
ax1.set_title("Profesion VS Centro de costos 2018")
ax2 = fig.add_subplot(gs[0, 1])  # row 0, col 1
df.groupby(['profesion', 'categ_cco_2019'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).head(10).plot.bar(ax=ax2, figsize=(20, 10),
                                                                       colors=color)
ax2.set_xlabel('Profesion / Centro de Costo')
ax2.set_ylabel('Número de Donaciones')
ax2.set_title("Profesion VS Centro de costos 2019")
ax3 = fig.add_subplot(gs[1, :])  # row 1, span all columns
df.groupby(['profesion', 'categ_cco_2020'])['cod_ter'].count(
).to_frame().sort_values('cod_ter', ascending=False).head(10).plot.bar(ax=ax3, figsize=(20, 10),
                                                                       colors=color)
ax3.set_xlabel('Profesion / Centro de Costo')
ax3.set_ylabel('Número de Donaciones')
ax3.set_title("Profesion VS Centro de costos 2020")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=210)
fig.savefig('./images/cooperadoras/cooperadoras_descriptivo_6.png')
# plt.show()



##########################################################
##### gráficas usando la base de datos master ############
##########################################################

# cargo los archivos de bases de datos de cooperadoras
df = pd.read_csv(
    '../bd_finales/cooperadoras_transaccional_caracterizacion.csv')
# coop.set_index('cod_ter', inplace=True)
print(df.columns.values)
# print(coop)
df['cod_ter'] = df['cod_ter'].astype('int32', copy=False)
df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'],
                                        infer_datetime_format=True)
now = pd.Timestamp('now')
df['edad'] = (now - df['fecha_nacimiento']).astype('<m8[Y]')
# print(coop['edad'].max())
# print(coop['edad'].min())
df['prom_donacion_mes'] = df['donacion_total'] / 32

# gráficos sobre información caracteristica vs transaccional

# graficos de edad y relación con monto donado
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante cooperadoras')
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
ax2.set_ylabel('Monto acum (miles de millones $)')
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
fig.savefig('./images/cooperadoras/cooperadoras_descriptivo_2.png')
# plt.show()

# aderencia con la causa y los montos donados
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante cooperadoras')
df.groupby(['misma_sucursal']).size().plot.pie(ax=ax1, colors=color,
                                               autopct='%1.1f%%',
                                               counterclock=False)
ax1.set_title("Misma sucrusal durante los tres años?")
df.groupby(['misma_sucursal'])[
    'donacion_total'].sum().plot.bar(ax=ax2, colors=color)
ax2.set_xlabel('')
ax2.set_ylabel('Monto acum (miles millones de cop)')
ax2.set_title("Sucursal vs monto total donado")
df.groupby(['misma_causa']).size().plot.pie(ax=ax3, figsize=(20, 10),
                                            colors=color,
                                            autopct='%1.1f%%',
                                            counterclock=False)
ax3.set_title("Donó a un mismo centro de costos durante los 3 años")
df.groupby(['misma_causa'])[
    'donacion_total'].sum().plot.bar(ax=ax4, colors=color)
ax4.set_xlabel('Si donaron o no al mismo centro de costos')
ax4.set_ylabel('Monto acum (miles millones de cop)')
ax4.set_title("Aderencia con el centro de costos vs monto total donado")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=0)
fig.savefig('./images/cooperadoras/cooperadoras_descriptivo_7.png')
# plt.show()

# estado civil del donante
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante cooperadoras')
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
fig.savefig('./images/cooperadoras/cooperadoras_descriptivo_8.png')
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
fig.savefig('./images/cooperadoras/cooperadoras_descriptivo_9.png')
# plt.show()

# informacion del centro
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante cooperadoras')
df.groupby(['centro'])['donacion_total'].sum().plot.bar(ax=ax1, figsize=(20, 10),
                                                        colors=color)
ax1.set_xlabel('Centro Cultural')
ax1.set_ylabel('Monto acum (miles de millones $)')
ax1.set_title("Monto en pesos acumulado por centro 2018-2020")
df.groupby(['centro']).size().plot.bar(ax=ax2, figsize=(20, 10),
                                       colors=color)
ax2.set_xlabel('Centro Cultural')
ax2.set_ylabel('Número de donantes (personas)')
ax2.set_title("Número de donantes por centro")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=30)
fig.savefig('./images/cooperadoras/cooperadoras_descriptivo_10.png')

fig, (ax3, ax4) = plt.subplots(1, 2)
fig.suptitle(
    'Información característica vs transaccional del donante cooperadoras')
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
fig.savefig('./images/cooperadoras/cooperadoras_descriptivo_11.png')
# plt.show()


# informacion de la profesion e insights
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante cooperadoras')
df2 = df.groupby(['profesion']).size(
).to_frame().sort_values(0, ascending=False)
df2 = df2.head(15)
df2.plot.bar(ax=ax1, figsize=(20, 10),
             colors=color)
ax1.set_xlabel('Profesion')
ax1.set_ylabel('Número de donantes cooperadoras (personas)')
colors = ['purple', 'purple', 'purple', 'purple', 'purple',
          'purple', 'purple', 'purple', 'purple', 'purple',
          'purple', 'purple', 'purple', 'purple', 'purple']
lines = [Line2D([0], [0], color=c, linewidth=2)
         for c in colors]
labels = [
    'Abogada', 'Ama de casa', 'Administradora de empresas',
    'Ingeniera Industrial', 'Administradora de Empresas',
    'Docente', 'Bacteriologa', 'Contadora Publica',
    'Psicologa', 'Arquitecta', 'Comunicadora Social',
    'Odontologa', 'Comunicadora social', 'Psicóloga',
    'Fisioterapeuta']
ax1.legend(lines, labels, loc='upper right', prop={'size': 7})
ax1.set_title("Top 15 de profesiones más frecuentes (de 115 en total)")
df2 = df.groupby(['profesion'])[
    'prom_donacion_mes'].sum().sort_values(0, ascending=False)
df2 = df2.head(15)
df2.plot.bar(ax=ax2, figsize=(20, 10),
             colors=color)
ax2.set_xlabel('Profesion')
ax2.set_ylabel('Promedio de donación mensual')
colors = ['purple', 'purple', 'purple', 'purple', 'purple',
          'purple', 'purple', 'purple', 'purple', 'purple',
          'purple', 'purple', 'purple', 'purple', 'purple']
lines = [Line2D([0], [0], color=c, linewidth=2)
         for c in colors]
labels = [
    'Abogada', 'Ingeniera Industrial', 'Administradora de Empresas',
    'Arquitecta', 'Ama de casa', 'Administradora de empresas',
    'Enfermera Jefe', 'Psicóloga', 'Contadora Publica',
    'Contadora',  'Comunicadora social', 'Ingeniera de sistemas',
    'Odontologa', 'Fisioterapeuta', 'Comunicadora Social']
ax2.legend(lines, labels, loc='upper right', prop={'size': 7})
ax2.set_title("Top 15 de profesiones que más donan (de 115 en total)")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=85)
fig.savefig('./images/cooperadoras/cooperadoras_descriptivo_12.png')
# plt.show()

# top 15 de donantes más recurrentes y que más donan $
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Top 15 de donantes cooperadoras que más...')
df2 = df.sort_values('donacion_total', ascending=False)
df2 = df2[['donacion_total', 'cod_ter']].set_index('cod_ter').head(15)
df2.plot.bar(ax=ax1, figsize=(20, 10),
             colors=color)
ax1.set_xlabel('Número de documento del donante')
ax1.set_ylabel('Monto de donación en miles de millones de pesos')
colors = ['purple', 'purple', 'purple', 'purple', 'purple',
          'purple', 'purple', 'purple', 'purple', 'purple',
          'purple', 'purple', 'purple', 'purple', 'purple']
lines = [Line2D([0], [0], color=c, linewidth=2)
         for c in colors]
labels = ['Olga Orjuela', 'Claudia Prieto',
          'Maria Margarita Escobar', 'Juliana Restrepo',
          'Claudia Marcela Moreno', 'Handrix Garcia',
          'Maria Jose Izquierdo', 'Laura Cristina Parra',
          'Carolina Certuche', 'Angela Claudia Burbano',
          'Amalia Riveros', 'Teresita Cardona',
          'Gloria Helena Carbonell', 'Luisa Yaneth Pallares',
          'Natalia Silva']
ax1.legend(lines, labels, ncol=1, loc='upper right', prop={'size': 7})
ax1.set_title("Top 15 acumulado de donación $ 2018-2020")
df3 = df.sort_values('recurrencia_prom', ascending=False)
df3 = df3[['recurrencia_prom', 'cod_ter']].set_index('cod_ter').head(15)
df3.plot.bar(ax=ax2, figsize=(20, 10),
             colors=color)
ax2.set_xlabel('Número de documento del donante')
ax2.set_ylabel('Recurrencia de su donación promedio')
colors = ['purple', 'purple', 'purple', 'purple', 'purple',
          'purple', 'purple', 'purple', 'purple', 'purple',
          'purple', 'purple', 'purple', 'purple', 'purple']
lines = [Line2D([0], [0], color=c, linewidth=2)
         for c in colors]
labels = [
    'Claudia Prieto', 'Maria Luisa Sanchez',
    'Amalia Riveros', 'Cristina Restrepo',
    'Viviana Ramirez', 'Claudia Milena Amado',
    'Liliana Castellanos', 'Olga Villalba',
    'Maria del Mar Perez', 'Clara Eugenia Romero',
    'Angela Claudia Burbano', 'Olga Cecilia García',
    'Zoraida Herrera', 'Gloria Carbonell',
    'Maria Teresa Gonzalez']
ax2.legend(lines, labels, ncol=1, loc='upper right', prop={'size': 7})
ax2.set_title("Top 15 acumulado de donantes más recurrentes en promedio")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=60)
fig.savefig('./images/cooperadoras/cooperadoras_descriptivo_13.png')
# plt.show()

# recurrencia promedio de donaciones y recurrencia vs donaciones totales
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle(
    'Insights: información caracteristica vs transaccional de donante cooperadoras')
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
ax2.set_ylabel('Monto acumulado (en miles de millones)')
ax2.set_xlabel('Número de transacciones promedio al año')
ax2.set_title("Monto total acumulado por transacciones")
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=0)
fig.savefig('./images/cooperadoras/cooperadoras_descriptivo_14.png')
# plt.show()
