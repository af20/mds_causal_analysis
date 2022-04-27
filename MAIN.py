import pandas as pd
from library import *
convert_data_to_csv()
df_data_baseline = pd.read_csv('data/data_baseline.csv', header=0)
df_data_census = pd.read_csv('data/data_census.csv', header=0)
df_endline1businesstype = pd.read_csv('data/data_endline1businesstype.csv', header=0)
df_endlines1and2 = pd.read_csv('data/data_endlines1and2.csv', header=0)

'''
COLUMNS                     print(df_data_baseline.columns.tolist())

df_data_baseline            ['hhid_baseline', 'areaid', 'area_dropped', 'treatment', 'hh_size', 'adults', 'children', 'male_head', 'head_age', 'head_noeduc', 'spandana', 'othermfi', 'bank', 'informal', 'anyloan', 'spandana_amt', 'othermfi_amt', 
                            'bank_amt', 'informal_amt', 'anyloan_amt', 'total_biz', 'female_biz', 'female_biz_pct', 'bizrev', 'bizexpense', 'bizinvestment', 'bizemployees', 'hours_weekbiz', 'total_exp_mo', 'nondurable_exp_mo', 
                            'durables_exp_mo', 'home_durable_index']

df_data_census              ['hhid_census', 'hhid', 'areaid', 'treatment', 'attrit', 'spandana_borrower', 'mfi_borrower', 'hhinslum_months', 'pucca', 'ownhouse', 'woman_biz', 'husb_biz', 'woman_salary', 'husb_salary', 'firstloandate', 'p10loandate']

df_endlines1and2            ['hhid', 'areaid', 'treatment', 'w', 'w1', 'w2', 'sample1', 'sample2', 'old_biz', 'any_old_biz', 'area_pop_base', 'area_debt_total_base', 'area_business_total_base', 'area_exp_pc_mean_base', 
                            'area_literate_head_base', 'area_literate_base', 'visitday_1', 'visitmonth_1', 'visityear_1', 'visitday_2', 'visitmonth_2', 'visityear_2', 'hhsize_1', 'hhsize_adj_1', 'adults_1', 'children_1', 'male_head_1', 
                            'head_age_1', 'head_noeduc_1', 'women1845_1', 'anychild1318_1', 'hhsize_2', 'hhsize_adj_2', 'adults_2', 'children_2', 'male_head_2', 'head_age_2', 'head_noeduc_2', 'women1845_2', 'anychild1318_2', 'spouse_literate_1', 
                            'spouse_works_wage_1', 'ownland_hyderabad_1', 'ownland_village_1', 'spouse_literate_2', 'spouse_works_wage_2', 'ownland_hyderabad_2', 'ownland_village_2', 'spandana_1', 'othermfi_1', 'anymfi_1', 'anybank_1', 'anyinformal_1', 
                            'anyloan_1', 'everlate_1', 'mfi_loan_cycles_1', 'spandana_amt_1', 'othermfi_amt_1', 'anymfi_amt_1', 'bank_amt_1', 'informal_amt_1', 'anyloan_amt_1', 'spandana_2', 'othermfi_2', 'anymfi_2', 'anybank_2', 'anyinformal_2', 
                            'anyloan_2', 'everlate_2', 'mfi_loan_cycles_2', 'spandana_amt_2', 'othermfi_amt_2', 'anymfi_amt_2', 'bank_amt_2', 'informal_amt_2', 'anyloan_amt_2', 'bizassets_1', 'bizinvestment_1', 'bizrev_1', 'bizexpense_1', 'bizprofit_1', 
                            'bizemployees_1', 'any_biz_1', 'total_biz_1', 'any_new_biz_1', 'biz_stop_1', 'newbiz_1', 'female_biz_1', 'female_biz_new_1', 'bizassets_2', 'bizinvestment_2', 'bizrev_2', 'bizexpense_2', 'bizprofit_2', 'bizemployees_2', 
                            'any_biz_2', 'total_biz_2', 'any_new_biz_2', 'biz_stop_2', 'newbiz_2', 'female_biz_2', 'female_biz_new_2', 'wages_nonbiz_1', 'wages_nonbiz_2', 'hours_week_1', 'hours_week_biz_1', 'hours_week_outside_1', 'hours_headspouse_week_1', 
                            'hours_headspouse_outside_1', 'hours_headspouse_biz_1', 'hours_child1620_week_1', 'hours_girl1620_week_1', 'hours_boy1620_week_1', 'hours_week_2', 'hours_week_biz_2', 'hours_week_outside_2', 'hours_headspouse_week_2', 
                            'hours_headspouse_outside_2', 'hours_headspouse_biz_2', 'hours_child1620_week_2', 'hours_girl1620_week_2', 'hours_boy1620_week_2', 'total_exp_mo_1', 'durables_exp_mo_1', 'nondurable_exp_mo_1', 'health_exp_mo_1', 'educ_exp_mo_1', 
                            'festival_exp_annual_1', 'temptation_exp_mo_1', 'food_exp_mo_1', 'total_exp_mo_pc_1', 'durables_exp_mo_pc_1', 'nondurable_exp_mo_pc_1', 'food_exp_mo_pc_1', 'health_exp_mo_pc_1', 'educ_exp_mo_pc_1', 'temptation_exp_mo_pc_1', 
                            'festival_exp_mo_pc_1', 'home_durable_index_1', 'total_exp_mo_2', 'durables_exp_mo_2', 'nondurable_exp_mo_2', 'health_exp_mo_2', 'educ_exp_mo_2', 'festival_exp_annual_2', 'temptation_exp_mo_2', 'food_exp_mo_2', 'total_exp_mo_pc_2', 
                            'durables_exp_mo_pc_2', 'nondurable_exp_mo_pc_2', 'food_exp_mo_pc_2', 'health_exp_mo_pc_2', 'educ_exp_mo_pc_2', 'temptation_exp_mo_pc_2', 'festival_exp_mo_pc_2', 'home_durable_index_2', 'girl515_school_1', 'boy515_school_1', 
                            'girl515_workhrs_pc_1', 'boy515_workhrs_pc_1', 'girl1620_school_1', 'boy1620_school_1', 'women_emp_index_1', 'female_biz_pct_1', 'girl515_school_2', 'boy515_school_2', 'girl515_workhrs_pc_2', 'boy515_workhrs_pc_2', 
                            'girl1620_school_2', 'boy1620_school_2', 'women_emp_index_2', 'female_biz_pct_2', 'credit_index_1', 'biz_index_all_1', 'biz_index_old_1', 'biz_index_new_1', 'income_index_1', 'labor_index_1', 'consumption_index_1', 
                            'social_index_1', 'credit_index_2', 'biz_index_all_2', 'biz_index_old_2', 'income_index_2', 'labor_index_2', 'consumption_index_2', 'social_index_2']
                    INTERESSANTI ==> consumption_index_1, consumption_index_2

df_endline1businesstype:    ['hhid', 'areaid', 'treatment', 'businessid', 'new_business_1', 'business_type_1', 'business_type_aggregate_1']
'''
print(df_endlines1and2[['treatment', 'consumption_index_1', 'consumption_index_2']])
