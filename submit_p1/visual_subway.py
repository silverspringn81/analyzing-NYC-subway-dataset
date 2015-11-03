'''
Data Analyst Nanodegree
P1-Section 3. Visualization
'''
import numpy as np
import pandas
import matplotlib.pyplot as plt
from ggplot import *

def entries_histogram(filename):
    '''
    Histogram of ridership on rainy and non-rainy days
    '''

    turnstile_weather = pandas.read_csv(filename)

    plt.figure()
    data_r = turnstile_weather[turnstile_weather.rain == 1] 
    data_nr = turnstile_weather[turnstile_weather.rain == 0]  

    # comupute mean and median
    print np.median(data_r['ENTRIESn_hourly'])
    print np.mean(data_r['ENTRIESn_hourly'])

    print np.median(data_nr['ENTRIESn_hourly'])
    print np.mean(data_nr['ENTRIESn_hourly'])


    data_nr['ENTRIESn_hourly'].hist(bins=20, range=[0,6000], label='No Rain', alpha=0.5)
    data_r['ENTRIESn_hourly'].hist(bins=20, range=[0,6000], label='Rain', alpha=.5, color='red')
    plt.xlabel('ENTRIESn_hourly')
    plt.ylabel('Frequency')
    plt.title('Histogram of ENTRIESn_hourly')
    plt.legend()
    plt.show()
    return plt

def plot_dayofweek_data(filename):
    '''
    Scatter plot of ridership by day-of-week
    '''
    turnstile_weather = pandas.read_csv(filename)
    print ggplot(turnstile_weather, aes('day_week', 'ENTRIESn_hourly')) +\
        geom_point(size = 5.0, color = 'red') + xlab("Day of the week") +\
        ggtitle("Ridership by day of the week") +\
        scale_x_continuous(breaks=[0,1,2,3,4,5,6], labels=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]) +\
        ylim(0,)
    return 


entries_histogram('improved-dataset/turnstile_weather_v2.csv')
plot_dayofweek_data('improved-dataset/turnstile_weather_v2.csv')



