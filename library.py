import pandas as pd

def convert_data_to_csv():
  v_file_names = ['2013-0533_data_baseline', '2013-0533_data_census', '2013-0533_data_endline1businesstype', '2013-0533_data_endlines1and2']
  for file_name in v_file_names:
    data = pd.io.stata.read_stata('data/dta/' + file_name + '.dta')
    file_name = file_name.replace('2013-0533_','')
    data.to_csv('data/' + file_name+ '.csv')
