with Model() as medals_linear:
    
    intercept = Normal('intercept', 0, sd=100)
    slope = Normal('slope', 0, sd=100)
    σ = HalfCauchy('σ', 1)
    
    μ = intercept + slope*x
    score = Normal('score', μ, sd=σ, observed=y)
    
    samples = sample(500, random_seed=RANDOM_SEED)