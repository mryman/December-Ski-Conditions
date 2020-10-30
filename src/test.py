def one_sample_one_tailed(sample_data, popmean, alpha=0.05, alternative='greater'):
    '''
    Perform a 1-sample 1-tail t-test using sample data from weather df

    ARGS: sample_data - Ratio of rain vs snow accumulations per year

    Returns: t-value: float
             p-value: float
             Statement regarding null hypothesis: String
    '''
    
    
    t, p = stats.ttest_1samp(sample_data, popmean)
    print ('t:',t)
    print ('p:',p)
    if alternative == 'greater' and (p/2 < alpha) and t > 0:
        print ('Reject Null Hypothesis for greater-than test with alpha = {}'.format(alpha))
    elif alternative == 'greater' and (p/2 >= alpha) and t > 0:
        print ('Fail to Reject Null Hypothesis for greater-than test with alpha = {}'.format(alpha))
    if alternative == 'less' and (p/2 < alpha) and t < 0:
        print ('Reject Null Hypothesis for less-thane test with alpha = {}'.format(alpha))
    elif alternative == 'less' and (p/2 >= alpha) and t > 0:
        print ('Fail to Reject Null Hypothesis for greater-than test with alpha = {}'.format(alpha))


