with Model() as salmon_model:
    
    β = Normal('β', 0, sd=10, shape=3)
    
    μ = β[0] + β[1]*salmon.spawners + β[2]*salmon.spawners**2
    σ = HalfCauchy('σ', 1)
    
    recruits = Normal('recruits', μ, sd=σ, observed=salmon.recruits)
    
    salmon_sample = sample(2000)