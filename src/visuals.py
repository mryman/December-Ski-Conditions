import matplotlib.pyplot as plt  
import pandas as pd  
import datetime as dt
import scipy.stats as stats


def plt_precip_totals(df):
    '''
    Create visualization illustrating quantity of month total rain vs. snow, grouped by Year

    ARG: df pertaining to specific month
    OUTPUT: jpg file
    '''
    rain = df.groupby(df['dt_time_pst'].dt.year)['hrly_rain'].sum()
    snow = df.groupby(df['dt_time_pst'].dt.year)['hrly_snow'].sum()

    fig, ax = plt.subplots(figsize=(10,4))
    ax.bar(rain.index, rain, width=0.25, label='Rain')
    ax.bar(snow.index + 0.25, snow, width=0.25, label='Snow')
    ax.set_ylabel('Precip in In. Water Equivalent')
    ax.legend()
    plt.suptitle('December Cumulative Precipitation by Type',y=0.97,fontsize=18, fontweight='bold')

    return plt.savefig('img/precip_totals.jpg')


def plt_precip_means(df):
    
    '''
    Plot normal distribution graphs of precipitation types and show mean for each

    ARG: df - month df with columns added for snow and rain
    OUTPUT: jpg file
    '''
    
    full_rain_mean = df['hrly_rain'].mean()
    full_rain_sd = df['hrly_rain'].std()

    full_snow_mean = df['hrly_snow'].mean()
    full_snow_sd = df['hrly_snow'].std()


    x_min = -0.2
    x_max = 0.2
    x = np.linspace(x_min, x_max, 100)

    yrain = stats.norm.pdf(x,full_rain_mean,full_rain_sd)
    ysnow = stats.norm.pdf(x,full_snow_mean, full_snow_sd)

    fig, ax = plt.subplots(figsize=(10,4))

    ax.plot(x,yrain, color='blue',label='Rain')
    ax.plot(x,ysnow, color='coral', label='Snow')
    plt.axvline(full_rain_mean, ls='--', lw=1, color='blue')
    plt.axvline(full_snow_mean, ls='--', lw=1, color='coral')
    ax.set_xlabel('Precip in In. Water Equivalent')
    ax.legend()
    return plt.savefig('img/daily_precip_means.jpg')

def plt_future_prob(data):
    '''
    Plot normal distribution using sample mean and stdev from data
    and shade area to right of 1 - cdf of x=1

    OUTPUT: jpg file
    '''

    fig, ax = plt.subplots(figsize=(10,4))
    data = sorted(ratio.ratio.values)
    x = np.linspace(mu-4*std, mu+4*std, 100)
    pdf = stats.norm.pdf(x, mu, std)
    plt.axvline(mu, ls='--', lw=1.5, color='green')
    plt.axvline(1, lw=1.5, color='red')
    plt.plot(x, pdf)

    #coloring area
    iq = stats.norm(mu, std)
    px = np.arange(1,mu+4*std,0.01)
    plt.fill_between(px,iq.pdf(px),color='blue',alpha=0.25)
    plt.text(1.5, 0.15, '54.9%', style='italic', fontsize=14)
    ax.set_xlabel('Ratio of Rain/Snow')

    plt.suptitle('Probabilty of Future Rain Equal to Snow', fontsize=16)

    return plt.savefig('img/future_rain_prob.jpg')

def plt_temp_daily_means(df, month_name):
     '''
    Plot daily mean temps for each year in separate ax

    ARG: df - month df 
         month_name - string
    OUTPUT: jpg file
    '''
    
    
    fig, axs = plt.subplots(5,1, figsize = (15, 10), sharex = True, sharey=True)
    for i, year in enumerate([2015, 2016, 2017, 2018, 2019]):
        #print(year)
        x = df['dt_time_pst'].dt.day.unique()
        yrmask = df['dt_time_pst'].dt.year == year
        ymean = df[yrmask]['temperature_deg_f'].groupby(df['dt_time_pst'].dt.day).mean()
        ymax = df[yrmask]['temperature_deg_f'].groupby(df['dt_time_pst'].dt.day).max()
        ymin = df[yrmask]['temperature_deg_f'].groupby(df['dt_time_pst'].dt.day).min()
    
    
        axs[i].set_ylabel('Temp Deg F')
    
        axs[i].plot(x, ymean, color='navy', lw=2, label=year)
        axs[i].axis([1,32, 0, 45])
        axs[i].text(6, 6, year, style='italic', fontsize=16)
   
        axs[i].grid()
        axs[i].axhline(32, 0,31, ls='--', lw=1, color='red')
    
    axs[4].set_xlabel(month_name + 'Dates', fontsize=12)    
    plt.suptitle('Mean Daily Temps for ' + month_name + ' Dates',y=0.97,fontsize=18, fontweight='bold')
    plt.text(0.14, 0.9, '----- Rain/Snow Transition Temp', fontsize=12, color='red',transform=plt.gcf().transFigure)
    plt.text(0.68, 0.9, 'Data from instruments at 3100ft elev', fontsize=12, transform=plt.gcf().transFigure)

    return plt.savefig('img/meantemps.jpg')


def plt_snowdepth(fulldec_df):
    '''
    Plot representation of snow max depth per day with separate plot for each year.
    
    Represent all opening dates with day as integer plus 0.5 offset so they present between 
    bars for clarity
    '''

    #Actual opening date for each year at Alpental ski area
    Season2015 = 18.5 #'2015-12-18'
    Season2016 = 12.5 #'2016-12-12'
    Season2017 = 9.5  #'2017-12-09'
    Season2018 = 22.5 #'2018-12-22'
    Season2019 = 36.5 #'2020-01-05'
    seasons = [Season2015, Season2016, Season2017, Season2018, Season2019]

    #Critical target date to open for Holiday season(school break begins):
    xmas2015 = 19.5 #'2015-12-19'
    xmas2016 = 17.5 #'2016-12-17'
    xmas2017 = 16.5 #'2017-12-16'
    xmas2018 = 22.5 #'2018-12-22'
    xmas2019 = 21.5 #'2019-12-21'

    crit_dates = [xmas2015, xmas2016, xmas2017, xmas2018, xmas2019]

    fig, axs = plt.subplots(5, figsize = (12, 13), sharex=True, sharey=True )

    for i, year in enumerate([2015, 2016, 2017, 2018, 2019]):
        #print(year)
        x = fulldec_df['dt_time_pst'].dt.day.unique()
        yrmask = fulldec_df['dt_time_pst'].dt.year == year
        ydepth_max = fulldec_df[yrmask]['total_snow_depth'].groupby(fulldec_df['dt_time_pst'].dt.day).max()
    
        axs[i].bar(x, ydepth_max)
        axs[i].set_ylabel('Snow Depth')
        axs[i].set_xlabel('December Dates')
        axs[i].axhline(36, 0,31, ls='--', lw=1, color='red')
        axs[i].axvline(seasons[i], color='green')
        axs[i].axvline(crit_dates[i], color='red')
        axs[i].text(2, 75, year, style='italic', fontsize=16)
        axs[i].axis([1,37, 0, 120])

    axs[4].text(31, 75, 'Jan 5-2020!--->', style='italic', fontsize=12)
    plt.suptitle('Depth of Snow by Date in inches',y=0.95,fontsize=18, fontweight='bold')
    plt.text(0.14, 0.9, '----- 36in Min Depth Target', fontsize=10, color='red',transform=plt.gcf().transFigure)
    plt.text(0.74, 0.92, '| Critical Date Target', fontsize=10, color='red',transform=plt.gcf().transFigure)
    plt.text(0.74, 0.9, '| Actual Opening Date', fontsize=10, color='green',transform=plt.gcf().transFigure)

    return plt.savefig('img/snowdepths.jpg')