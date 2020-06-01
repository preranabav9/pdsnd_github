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
    print(' Let\'s explore US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
      city = input("\nWhich city you like to see? New York City, Chicago or Washington?\n").lower()
      if city not in ('new york ', 'chicago', 'washington'):
        print("Sorry, I don't understand. Try another city.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nchoose month ? January, February, March, April, May, June or type 'all' if you do not have any preference?\n").lower()
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("Sorry, I don't understand. try again.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\n choose the  day you are looking for? enter the day : Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' when you do not have any preference.\n").lower()
      if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        print("Sorry, I don't understand. Try again.")
        continue
      else:
        break

    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])

 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # to_datetime is used to convert date into date format
    df['End Time'] = pd.to_datetime(df['End Time'])
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        #used to find index of month.
        month = months.index(month) + 1       

        df = df[df['Start Time'].dt.month == month]
        
    #filter data by day.
    if day != 'all': 
        df = df[df['Start Time'].dt.weekday_name == day.title()]
     #print 5 rows.
    print(df.head())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    #if month in('january', 'february', 'march', 'april', 'may', 'june', 'all'):
    most_common_month = df['Start Time'].dt.month.value_counts().idxmax()
    print('Most common month is ' + str(most_common_month))

    # display the most common day of week
    #if day in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
    most_common_day = df['Start Time'].dt.weekday_name.value_counts().idxmax()
    print('Most common day is ' + str(most_common_day))

    # display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('Most popular hour is ' + str(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nfind The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('\nMost commonly used start station is {}\n'.format(Start_Station))

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost commonly used end station is {}\n'.format(End_Station))

    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip is {} and {}'.format(Start_Station, End_Station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nfind duration of trip.\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    time1 = total_travel_time
    day = time1 // (24 * 3600)
    time1 = time1 % (24 * 3600)
    hour = time1 // 3600
    time1 %= 3600
    minutes = time1 // 60
    time1 %= 60
    seconds = time1
    print('\nTotal travel time is {} days {} hours {} minutes {} seconds'.format(day, hour, minutes, seconds))


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    time2 = mean_travel_time
    day2 = time2 // (24 * 3600)
    time2 = time2 % (24 * 3600)
    hour2 = time2 // 3600
    time2 %= 3600
    minutes2 = time2 // 60
    time2 %= 60
    seconds2 = time2
    print('\nMean travel time is {} hours {} minutes {} seconds'.format(hour2, minutes2, seconds2))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def disp_data(df):   #this function will display the info of 5 people and ask or next 5.
    head=0
    tail=5
    user_choise = input('\n Do you want to see the data of the trip? reply with "yes" or "no"\n')
  
    if user_choise.lower() == 'yes':
        print(df[df.columns[0:-1]].iloc[head:tail])
        want_again = ''
        while want_again.lower() != 'no':
                want_again = input('\n Do you want to see some more data of the trip? reply with "yes" or "no"\n')
                if want_again.lower() == 'yes':
                    head += 5
                    tail += 5
                    print(df[df.columns[0:-1]].iloc[head:tail])
                elif want_again.lower() == 'no':
                    break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        disp_data(df)

        restart = input('\ndo you want to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            



if __name__ == "__main__":
	main()
