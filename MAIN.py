import pandas as pd
import numpy as np
from library import *

convert_data_to_csv()
df_data_baseline = pd.read_csv('data/data_baseline.csv', header=0)
df_data_census = pd.read_csv('data/data_census.csv', header=0)
df_endline1businesstype = pd.read_csv('data/data_endline1businesstype.csv', header=0)
df_endlines1and2 = pd.read_csv('data/data_endlines1and2.csv', header=0)

v_combo_columns= lib_get_combp_columns()
v_obj = []
for x in v_combo_columns:
  col_1, col_2 = x+'_1', x+'_2'
  try:
    obj = lib_check_causal_analysis(x, df_endlines1and2, col_1, col_2)
    v_obj.append(obj)
  except:
    pass # su 14 su 85 stianta, abbiamo 71 colonne

df = pd.DataFrame({
    'Field': [x.field for x in v_obj],

    'Obs_0': [x.obs_0 for x in v_obj],
    'Ttest_0': [x.ttest_0 for x in v_obj],
    'p-value_0': [x.pvalue_0 for x in v_obj],

    'Obs_1': [x.obs_1 for x in v_obj],
    'Ttest_1': [x.ttest_1 for x in v_obj],
    'p-value_1': [x.pvalue_1 for x in v_obj],

    'Diff.Mean_0': [x.is_mean_different_0 for x in v_obj],
    'Diff.Mean_1': [x.is_mean_different_1 for x in v_obj]
  })
print(df)
df.to_excel("RESULTS.xlsx")

# lib_check_causal_analysis('Consumo Totale', df_endlines1and2, 'consumption_index_1', 'consumption_index_2')
# lib_check_causal_analysis('Consumo Beni Durevoli', df_endlines1and2, 'durables_exp_mo_1', 'durables_exp_mo_2')
# lib_check_causal_analysis('Consumo Beni Durevoli (PC)', df_endlines1and2, 'durables_exp_mo_pc_1', 'durables_exp_mo_pc_2')
# lib_check_causal_analysis('Spesa Beni Durevoli Casa', df_endlines1and2, 'home_durable_index_1', 'home_durable_index_2')
# lib_check_causal_analysis('Spesa Beni Durevoli Casa (PC)', df_endlines1and2, 'nondurable_exp_mo_pc_1', 'nondurable_exp_mo_pc_2')
