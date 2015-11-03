'''
Data Analyst Nanodegree
P1-Section 1. Statistical Test
'''
import numpy as np
import scipy
import scipy.stats
import pandas

def mann_whitney_plus_means(filename):
    '''
    Mann-Whitney U-test 
    '''
    turnstile_weather = pandas.read_csv(filename)
    
    ent_r = turnstile_weather[turnstile_weather.rain == 1].ENTRIESn_hourly
    ent_nr = turnstile_weather[turnstile_weather.rain == 0].ENTRIESn_hourly
    
    with_rain_mean = np.mean(ent_r)
    without_rain_mean = np.mean(ent_nr)
   
    U, p = scipy.stats.mannwhitneyu(ent_nr, ent_r) 
    
    print with_rain_mean, without_rain_mean, U, p
    return with_rain_mean, without_rain_mean, U, p 

mann_whitney_plus_means('improved-dataset/turnstile_weather_v2.csv')
