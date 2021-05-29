import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    """-------------------------------------------------------------------------"""
    city_selection = input('To view the available bikeshare data, kindly type:\n The letter (c) for Chicago\n The letter (n) for New York City\n The letter (w) for Washington:\n').lower()
    while city_selection not in {'c','n','w'}:
        print('That\'s invalid input.')
        city_selection = input('To view the available bikeshare data, kindly type:\n The letter (c) for Chicago\n The letter (n) for New York City\n The letter (w) for Washington:\n').lower()
    if city_selection == 'c':
        city = 'chicago'
    elif city_selection == 'n':
        city = 'new york city'
    elif city_selection == 'w':
        city = 'washington'
    """-------------------------------------------------------------------------"""
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    time_frame = input("Would you like to filter by month, day, both or all?\n").lower()
    while time_frame not in {'month','day','both','all'}:
        print('That\'s invalid input.')
        time_frame = input("Would you like to filter by month, day, both or all?\n").lower()
    #if user choose to filter by all:
    if time_frame == 'all':
        print('\nFiltering for {} for the 6 months period\n\n'.format(city.title()))
        month = 'all'
        day = 'all'
    #if user choose to filter by month and day:
    elif time_frame =='both':
        while True:
            month_selection = input("Choose a month from january to june\n").lower()
            if month_selection in months:
                month = month_selection
                break
            else:
                print('Invalid month choice!!')
        while True:
            day_selection = input("Choose a day from saturday to friday\n").lower()
            if day_selection in days:
                day = day_selection
                break
            else:
                print('Invalid day choice!!')
    #if user choose to filter by month:
    elif time_frame == 'month':
        while True:
            month_selection = input("Choose a month from january to june\n").lower()
            if month_selection in months:
                month = month_selection
                break
            else:
                print('Invalid month choice!!')
        day = 'all'
    #if user choose to filter by day:
    elif time_frame == 'day':
        while True:
            day_selection = input("Choose a day from saturday to friday\n").lower()
            if day_selection in days:
                day = day_selection
                break
            else:
                print('Invalid day choice!!')
        month = 'all'
    print('_'*40)
    return city, month, day
filters = get_filters()
city, month, day = filters
"""-------------------------------------------------------------------------"""
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
# extract month , day and hour of week from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    #df['day'] = df['Start Time'].dt.day
    df['day_of_week'] = df['Start Time'].dt.day_name()
# filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
         # filter by month to create the new dataframe
        df = df[df['month'] == month]
# filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df
city, month, day = filters
df = load_data(city, month, day)
"""-------------------------------------------------------------------------"""

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    #print codes
    print('The most popular month :', popular_month)
    print('The most popular day :', popular_day)
    print('The most popular start hour: ', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
time_stats(df)
"""-------------------------------------------------------------------------"""
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    df["rout"] = df["Start Station"] + " & " + df["End Station"]
    combination = df['rout'].mode()[0]
    #print codes:
    print('The commonly used start station: ', start_station)
    print('The most commonly used end station: ', end_station)
    print('The most frequent combination of start station and end station trip:', combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
station_stats(df)
"""-------------------------------------------------------------------------"""
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()/86400

    # display mean travel time
    mean_travel_time =df['Trip Duration'].mean()
    #print codes:
    print('The total travel time: ',int(total_travel_time),'days')
    print('The mean travel tim: ',int(mean_travel_time),'seconds')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
trip_duration_stats(df)
"""-------------------------------------------------------------------------"""
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    subscriber_user = df['User Type'].value_counts()[0]
    customer_user = df['User Type'].value_counts()[1]
    print('There are {} subscriber users and {} customer users.'.format(subscriber_user, customer_user))
    # Display counts of gender
    # Display earliest, most recent, and most common year of birth
    try:
        male_gender = df['Gender'].value_counts()[0]
        female_gender = df['Gender'].value_counts()[1]
        birth_year = df['Birth Year']
        print('There are {} males users and {} females users.'.format(male_gender, female_gender))
        print("The most recent year of birth for a user is: {}.".format(birth_year.max()))
        print("The earliest year of birth for a user is: {}".format(birth_year.min()))
        print("The most common year of birth for a user is: {}.".format(birth_year.mode()[0]))
    except KeyError:
        print('\n\nSorry, there\'s no gender or birth year data for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
user_stats(df)
"""-------------------------------------------------------------------------"""
def display_raw_data(city):
    display_raw = input('\nWould you like to see another 5 rows of the raw data? Enter yes or no.\n').lower()
    #if display_raw == 'no':
        #print('Thank You')
    while display_raw == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city],chunksize=5):
                print(chunk)
                display_raw = input('\nWould you like to see another 5 rows of the raw data? Enter yes or no.\n').lower()
                if display_raw !='yes':
                    print('Thank You')
                    break #breaking out of the for loop
            break
        except KeyboardInterrupt:
            print('Thank you')
display_raw_data(city)
"""-------------------------------------------------------------------------"""
def main():
    while True:
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thank You')
            break
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)


if __name__ == "__main__":
	main()

