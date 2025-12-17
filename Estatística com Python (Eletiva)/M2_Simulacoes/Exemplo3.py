
from scipy.stats import chi2
c1=chi2.ppf(0.05, df= 9)
c2=chi2.ppf(0.95, df= 9)

print(c1)
print(c2)