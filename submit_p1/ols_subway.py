'''
Data Analyst Nanodegree
P1-Section 2. Linear Regression
'''
import numpy as np
import pandas
import scipy
import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import random
import math
from ggplot import *

def predictions(filename):
    '''
    OLS using Statsmodels
    '''

    weather_turnstile = pandas.read_csv(filename)
    y = weather_turnstile['ENTRIESn_hourly']
   
    # input variables
    x_t = weather_turnstile['meantempi']
    x_p = weather_turnstile['precipi']
    x_h = weather_turnstile['hour']
    x_r = weather_turnstile['rain']
    
#    x = pandas.DataFrame({ 'meantempi': x_t, 'mt2': x_t**2, 'hour2': x_h**2})
#    x = pandas.DataFrame({ 'meantempi': x_t, 'hour': x_h, 'precipi': x_p})
    x = pandas.DataFrame({ 'hour': x_h, 'meantempi': x_t})

    # dummy variables
    dummy_units = pandas.get_dummies(weather_turnstile['UNIT'], prefix='unit')
    dummy_units2 = pandas.get_dummies(weather_turnstile['day_week'], prefix='wd')
    dummy_units3 = pandas.get_dummies(weather_turnstile['rain'], prefix='rain')

    x = x.join(dummy_units)
    x = x.join(dummy_units2)
    x = x.join(dummy_units3)
    x = sm.add_constant(x)

    # OLS
    model = sm.OLS(y, x)
    results = model.fit()
    print results.summary()
    
    prediction = np.dot(x, results.params)

    # residuals
    res = y - prediction
    
    # histogram
    plt.figure()
    res.hist(range=(-7500, 7500), bins=30)
    plt.title('Residual Frequency')
    plt.xlabel('Residuals')
    plt.ylabel('Frequency')
    plt.show()


    # residual plots
    res_vs_t = pandas.DataFrame({'meantempi':x_t, 'res':res})
    print ggplot(res_vs_t, aes('meantempi', 'res')) +\
        geom_point(size = 5.0, color = 'red') + xlab("meantempi") +\
        ylab("Residuals") + ggtitle("Residual Plot")

    res_vs_p = pandas.DataFrame({'precipi':x_p, 'res':res})
    print ggplot(res_vs_p,  aes('precipi', 'res')) +\
        geom_point(size = 5.0, color = 'red') + xlab("precipi") +\
        ggtitle("Residuals")

    res_vs_h = pandas.DataFrame({'hour':x_h, 'res':res})
    print ggplot(res_vs_h, aes('hour', 'res')) +\
        geom_point(size = 5.0, color = 'red') + xlab("hour") +\
        ylab("Residuals") + ggtitle("Residual Plot")

    res_vs_p = pandas.DataFrame({'prediction':prediction, 'res':res})
    print ggplot(res_vs_p, aes('prediction', 'res')) +\
        geom_point(size = 5.0, color = 'red') + xlab("Predicted value") +\
        ylab("Residuals") + ggtitle("Residual Plot")

    return prediction

predictions('improved-dataset/turnstile_weather_v2.csv')
