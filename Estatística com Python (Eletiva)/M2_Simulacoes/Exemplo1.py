from scipy.stats import norm

x = norm.ppf(0.975, loc=0, scale=1)
print(x)


