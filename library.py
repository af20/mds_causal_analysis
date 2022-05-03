import pandas as pd
import numpy as np
from scipy import stats

v_columns_df = ['hhid', 'areaid', 'treatment', 'w', 'w1', 'w2', 'sample1', 'sample2', 'old_biz', 'any_old_biz', 'area_pop_base', 'area_debt_total_base', 'area_business_total_base', 'area_exp_pc_mean_base', 
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

def lib_get_combp_columns():
  v_combo = []
  v_cols_1 = [x for x in v_columns_df if x[-2:] == '_1']
  for x in v_cols_1:
    s = x.replace('_1', '_2')
    if s in v_columns_df:
      v_combo.append(x.replace('_1', ''))
  return v_combo


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
#print(df_endlines1and2[['treatment', 'consumption_index_1', 'consumption_index_2']])
'''

''' The impact of the program is simply computed as the
    diﬀerence between two diﬀerences:
    DDimpact = (B-A)-(D-C) = (0.74-0.60)-(0.81-0.78) = 0.11
        A, B: Treatment Group (A: before, B: after)
        C, D: Comparison Group (C: before, D: after)

    df_T = df_endlines1and2[df_endlines1and2['treatment'] == 'Treatment']
    ds_T_v1 = df_T['consumption_index_1'].dropna(how='all')
    ds_T_v2 = df_T['consumption_index_2'].dropna(how='all')
    mean_T_v1 = A = np.mean(ds_T_v1)
    mean_T_v2 = B = np.mean(ds_T_v2)

    df_C = df_endlines1and2[df_endlines1and2['treatment'] == 'Control']
    ds_C_v1 = df_C['consumption_index_1'].dropna(how='all')
    ds_C_v2 = df_C['consumption_index_2'].dropna(how='all')
    mean_C_v1 = C = np.mean(ds_C_v1)
    mean_C_v2 = D = np.mean(ds_C_v2)
    DDimpact = (B-A) - (D-C)
    #print('DDimpact', DDimpact)
'''





def convert_data_to_csv():
  v_file_names = ['2013-0533_data_baseline', '2013-0533_data_census', '2013-0533_data_endline1businesstype', '2013-0533_data_endlines1and2']
  for file_name in v_file_names:
    data = pd.io.stata.read_stata('data/dta/' + file_name + '.dta')
    file_name = file_name.replace('2013-0533_','')
    data.to_csv('data/' + file_name+ '.csv')









# .... STAT TEST - P VALUE - SCORES ....#
def libg_get_if_distibution_is_normal(sample1):
  '''
    Test whether a sample differs from a normal distribution.
      This function tests the null hypothesis that a sample comes from a normal distribution.
      It is based on D’Agostino and Pearson’s [1], [2] test that combines skew and kurtosis to produce an omnibus test of normality.

      alpha = 1e-3 # = 1 / 1000
      print("         pvalue = {:g}".format(pvalue), '         stat', stat)
      if pvalue < alpha:  # null hypothesis: x comes from a normal distribution
          print("The null hypothesis can be rejected,the distribution is normal ---- pvalue:", pvalue)
      else:
          print("The null hypothesis cannot be rejected,the distribution is NOT normal ---- pvalue", pvalue)
      #arr = [1,2,4,-1,4,2,0,2,4,4,6,-2,-3,4,5,2,5,4,-2,-1,3,2,1]
      #x = libg_get_if_distibution_is_normal(arr)

  '''
  min_score_for_normality_of_distribution = 100
  stat,pvalue = stats.normaltest(sample1)
  pvalue_adj = max(0.000000001, pvalue) # 1 miliardo
  score = int(1/pvalue_adj)
  int(score)

  if score >= min_score_for_normality_of_distribution:
    return False
  else:
    return True

  




def libg_get_2_samples__have_different_Mean(sample1, sample2):
  # 2 SAMPLES	t-test con equal_var = False (ma minimo 20 n, altrimenti i 2 samples dovrebbero essere normali)
  ''' 
      IF ARE BOTH NORMAL ==> stats.ttest_ind (PARAMETRIC)
          Calculate the T-test for the means of two independent samples of scores.
          This is a two-sided test for the null hypothesis that 2 independent samples have identical average (expected) values. 
          This test assumes that the populations have identical variances by default.
              equal_varbool, optional
                  If True (default), perform a standard independent 2 sample test that assumes equal population variances [1]. 
                  If False, perform Welch’s t-test, which does not assume equal population variance [2].
                      Welch’s t-test: is a two-sample location test which is used to test the hypothesis that two populations have equal means. 
                                      It is named for its creator, Bernard Lewis Welch, and is an adaptation of Student's t-test,
                                      it is more reliable when the two samples have unequal variances and/or unequal sample sizes.
                                  Student's t-test assumes that the sample means (test statistics) of two population distributions being compared are normally distributed with equal variance. 
                                  Welch's t-test is designed for unequal sample distribution variance, but the assumption of normally distributed sample is maintained
      IF ONE IS NOT NORMAL ==> Mann-Whitney's test (NON-PARAMETRIC)
          In statistics, the Mann–Whitney U test (also called the Mann–Whitney–Wilcoxon (MWW), Wilcoxon rank-sum test, or Wilcoxon–Mann–Whitney test) 
              is a nonparametric test of the null hypothesis that, for randomly selected values X and Y from two populations, 
              the probability of X being greater than Y is equal to the probability of Y being greater than X.
          A similar nonparametric test used on dependent samples is the Wilcoxon signed-rank test.
  '''

  '''
    H0: media identica
        p-value piccolo ===> reject H0
  '''


  is_normal_1 = libg_get_if_distibution_is_normal(sample1)
  is_normal_2 = libg_get_if_distibution_is_normal(sample2)

  if is_normal_1 and is_normal_2:
    tstat,pvalue = stats.ttest_ind(sample1, sample2, equal_var = False, nan_policy='omit')
  else:
    tstat,pvalue = stats.mannwhitneyu(sample1, sample2, alternative='greater') # ERROR IF All numbers are identical in mannwhitneyu
  
  tstat, pvalue = round(tstat,2), round(pvalue,4)

  if pvalue > 0.05: # ttest piccolo, pvalue grande  ACCEPT H0 (media identica)
    return tstat, pvalue, False
  else: # REJECT H0 (media diversa)
    return tstat, pvalue, True # media significativamente diversa,  ttest grande (molto piccolo o molto grande)




def lib_check_causal_analysis(field, df, field_t0, field_t1):
  from classes import c_Boh

  df = df[['treatment', field_t0, field_t1]]
  df_0 = df[['treatment', field_t0]]
  df_0['t'] = 0
  df_0 = df_0.dropna()
  df_0.dropna(subset=[field_t0], inplace=True)


  df_1 = df[['treatment', field_t1]]
  df_1['t']=1
  df_1 = df_1.dropna()

  v_T0 = df_0[df_0['treatment'] == 'Treatment'][field_t0].tolist()
  v_nT0 = df_0[df_0['treatment'] == 'Control'][field_t0].tolist()
  tstat_0, pvalue_0, different_mean_0 = libg_get_2_samples__have_different_Mean(v_T0, v_nT0)

  v_T1 = df_1[df_1['treatment'] == 'Treatment'][field_t1].tolist()
  v_nT1 = df_1[df_1['treatment'] == 'Control'][field_t1].tolist()
  tstat_1, pvalue_1, different_mean_1 = libg_get_2_samples__have_different_Mean(v_T1, v_nT1)


  print(field)
  print('T0 ==> len:', len(v_T0), '   tstat:', tstat_0, '     pvalue:', pvalue_0,  '     different_mean:', different_mean_0)
  print('T1 ==> len:', len(v_T1), '   tstat:', tstat_1, '     pvalue:', pvalue_1,  '     different_mean:', different_mean_1)
  print()
  return c_Boh(field, len(v_T0), tstat_0, pvalue_0, different_mean_0, len(v_T1), tstat_1, pvalue_1, different_mean_1)
