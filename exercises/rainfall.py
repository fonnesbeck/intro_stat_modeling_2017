from pymc3 import Gamma

jul_rain = nash_precip.Jul
jan_rain = nash_precip.Jan

with Model() as rainfall_model:
    
    σ_jan = Uniform('σ_jan', 0, 1000)
    σ_jul = Uniform('σ_jul', 0, 1000)
    
    mu_jan = Uniform('mu_jan', 0, 25)
    mu_jul = Uniform('mu_jul', 0, 25)
    
    jan = Gamma('jan', mu=mu_jan, sd=σ_jan, observed=jan_rain)
    jul = Gamma('jul', mu=mu_jul, sd=σ_jul, observed=jul_rain)
    
    d = Deterministic('d', mu_jan - mu_jul)
    
    samples = fit(20000).sample(1000)
    