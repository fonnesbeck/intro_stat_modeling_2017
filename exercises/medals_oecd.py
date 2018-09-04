oecd = medals.oecd.values

with Model() as medals_linear:
    
    intercept = Normal('intercept', 0, sd=100)
    b = Normal('b', 0, sd=100, shape=2)
    σ = HalfCauchy('σ', 1)
    
    μ = intercept + b[0]*x + b[1]*oecd
    score = Normal('score', μ, sd=σ, observed=y)
    
    samples = sample(500, random_seed=RANDOM_SEED)