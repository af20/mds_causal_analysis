class c_Boh:
  def __init__(self, field, obs_0, ttest_0, pvalue_0, is_mean_different_0, obs_1, ttest_1, pvalue_1, is_mean_different_1):
    self.field = field

    self.obs_0 = obs_0
    self.ttest_0 = ttest_0
    self.pvalue_0 = pvalue_0
    self.is_mean_different_0 = is_mean_different_0

    self.obs_1 = obs_1
    self.ttest_1 = ttest_1
    self.pvalue_1 = pvalue_1
    self.is_mean_different_1 = is_mean_different_1

  '''
                        T0                              T1                        RESULTS (se le medie tra Control e Treatm. sono significativ. diverse)
  field,          obs_0, ttest_0, pval_0,    obs_1, ttest_1, pval_1,         diff_mean_0, diff_mean_1
  Consumption     1000, 202, 0.1              992,  9100, 0.01                  False   ,   True(ed è aumentato xk ttest grande)
  '''