#!/usr/bin/env python3
import pandas as pd


##################################################################
##### Carga de Base de datos maestra y cruce caracterizacion ####
#################################################################

# cargo los archivos depurados para hacer los cruces entre ellos
# dejar las 4 grandes base de datos: cooperadoras, particulaes, empresas
d_empresas = pd.read_csv('./data/donantes_limpios/donantes_empresas.csv')
d_empresas.set_index('cod_ter', inplace=True)
d_coop = pd.read_csv('./data/donantes_limpios/donantes_cooperadoras.csv')
d_coop.set_index('cod_ter', inplace=True)
d_sup = pd.read_csv(
    './data/donantes_limpios/donantes_supernumerarias.csv')
d_sup.set_index('cod_ter', inplace=True)
d_ter_empre = pd.read_csv(
    './data/donantes_limpios/donantes_terceros_empresas.csv')
d_ter_empre.set_index('cod_ter', inplace=True)

# cargando bases de dastos transaccionales de los donantes
d_transaccional = pd.read_csv('./bd_finales/bd_transaccional_donantes.csv')
d_transaccional['cod_ter'] = d_transaccional['cod_ter'].astype('float64')
d_transaccional.set_index('cod_ter', inplace=True)

# crucando la base de datos de transacciones con la basa caracterizacion
# tipo de donante empresa
bd_empresas = d_transaccional.merge(d_empresas, on='cod_ter', how='inner')
# bd_empresas_2 = d_transaccional.merge(d_ter_empre, on='cod_ter', how='inner')
bd_empresas.to_csv('./bd_finales/empresas_transaccional_caracterizacion.csv',
                   encoding='utf-8')
print(bd_empresas)

# crucando la base de datos de transacciones con la basa caracterizacion
# tipo de donante cooperadoras
bd_coop = d_transaccional.merge(d_coop, on='cod_ter', how='inner')
print(bd_coop.columns.values)
bd_coop.to_csv('./bd_finales/cooperadoras_transaccional_caracterizacion.csv',
               encoding='utf-8')
print(bd_coop)

# crucando la base de datos de transacciones con la basa caracterizacion
# tipo de donante particulares internos
bd_part_internos = d_transaccional.merge(d_sup, on='cod_ter', how='inner')
bd_part_internos.to_csv('./bd_finales/part_int_transaccional_caracterizacion.csv',
                        encoding='utf-8')
print(bd_part_internos)

# crucando la base de datos de transacciones con la basa caracterizacion
# tipo de donante particulares externos
bd_part_externos = d_transaccional.merge(
    d_ter_empre, indicator='i', how='outer', on='cod_ter').query(
        'i == "left_only"').drop('i', 1)
bd_part_externos = bd_part_externos.merge(
    d_coop, indicator='i', how='outer', on='cod_ter').query(
        'i == "left_only"').drop('i', 1)
bd_part_externos = bd_part_externos.merge(
    d_sup, indicator='i', how='outer', on='cod_ter').query(
        'i == "left_only"').drop('i', 1)
# dejo solo las columnas que me sirven borro las demás basura
bd_part_externos = bd_part_externos[['misma_sucursal', 'misma_causa', 'donacion_total',
                                     'variacion_promedio', 'variacion_2019-2020',
                                     'variacion_promedio_%', 'variacion_%_2019-2020',
                                     'recurrencia_prom', 'reccurencia']]
bd_part_externos.to_csv('./bd_finales/part_ext_transaccional_caracterizacion.csv',
                        encoding='utf-8')
print(bd_part_externos)
print(bd_part_externos.columns.values)


##################################################################
## Carga de base de datos año a año y cruce con caracterizacion ##
##################################################################
# cargando bases de datos transaccionales de los donantes
d_transaccional = pd.read_csv(
    './bd_finales/bd_transaccional_donantes_ano_ano.csv')
d_transaccional['cod_ter'] = d_transaccional['cod_ter'].astype('float64')
d_transaccional.set_index('cod_ter', inplace=True)

# crucando la base de datos de transacciones con la basa caracterizacion
# tipo de donante empresa
bd_empresas = d_transaccional.merge(bd_empresas, on='cod_ter', how='inner')
# bd_empresas_2 = d_transaccional.merge(d_ter_empre, on='cod_ter', how='inner')
bd_empresas.to_csv('./bd_finales/empresas_transaccional_caracterizacion_ano_ano.csv',
                   encoding='utf-8')
print(bd_empresas.columns.values)

# crucando la base de datos de transacciones con la basa caracterizacion
# tipo de donante cooperadoras
bd_coop = d_transaccional.merge(bd_coop, on='cod_ter', how='inner')
bd_coop.to_csv('./bd_finales/cooperadoras_transaccional_caracterizacion_ano_ano.csv',
               encoding='utf-8')
print(bd_coop.columns.values)

# crucando la base de datos de transacciones con la basa caracterizacion
# tipo de donante particulares internos
bd_part_internos = d_transaccional.merge(bd_part_internos, on='cod_ter', how='inner')
#print(bd_coop.columns.values)
bd_part_internos.to_csv('./bd_finales/part_int_transaccional_caracterizacion_ano_ano.csv',
                        encoding='utf-8')

# crucando la base de datos de transacciones con la basa caracterizacion
# tipo de donante particulares externos
bd_part_externos = d_transaccional.merge(bd_part_externos, on='cod_ter', how='inner')
print(bd_coop.columns.values)
bd_part_externos.to_csv('./bd_finales/part_ext_transaccional_caracterizacion_ano_ano.csv',
                        encoding='utf-8')
