# Predicting Airbnb First User's Destination


## Data

The following dataset is used for this project. Please save the *.csv files to the `data` directory. 

The dataset provided by Airbnb includes 5 .csv files that describe a user, their personal information, their web session records, and some summary statistics. 




1 & 2) [train_users.csv](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings/download/train_users_2.csv.zip) & [test_users.csv](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings/download/test_users.csv.zip)

    These datasets will be used to train and test our model, respectively. For each use in the dataset, we are provided the following features:
  
  * id: user id
  * date_account_created: the date of account creation
  * timestamp_first_active: timestamp of the first activity, note that it can be earlier than date_account_created or date_first_booking because a user can search before signing up
  * date_first_booking: date of first booking
  * gender
  * age
  * signup_method
  * signup_flow: the page a user came to signup up from
  * language: international language preference
  * affiliate_channel: what kind of paid marketing
  * affiliate_provider: where the marketing is e.g. google, craigslist, other
  * first_affiliate_tracked: whats the first marketing the user interacted with before the signing up
  * signup_app
  * first_device_type
  * first_browser
  * country_destination: this is the target variable you are to predict
  
  
3) [sessions.csv](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings/download/sessions.csv.zip) - This file contains information on the user's web sessions.  Features included in this file contain:
  * user_id: to be joined with the column 'id' in users table
  * action
  * action_type
  * action_detail
  * device_type
  * secs_elapsed
  
    This information can be used to provide meaningful insight on the user that may help us predict his or her first booking. For example, we could see the different types of actions a user took, if he/she began planning a trip, how long he/she spent deciding on an action (secs elapsed), etc. This information could be used to help predict where the user would want to travel first, as well as things about the trip that are important to the user, which Airbnb could leverage in their first attempt at customizing the trip for the user.
  
  
4) [countries.csv](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings/download/countries.csv.zip) - Summary statistics of destination countries in this dataset and their locations. This includes:
  * country name
  * latitude and longitutde
  * distance from U.S. (km2)
  * language and language levenshtein distance (how close words in the language are to words in english language)

    This information can be used to help determine if the country would interest the user based in its distance from the U.S. and whether or not the user would feel comfortable given the spoken language of that country. For example, the user may speak the main language spoken in that country, or the distance is not far enough from the U.S. to where the user would be discouraged from booking a trip.


5) [age_gender_bkts.csv](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings/download/age_gender_bkts.csv.zip) - Summary statistics of users' age group, gender, country of destination. This dataset includes the following columns:
 * age_bucket
 * country_destination
 * gender
 * population_in_thousands
 * year
  
    This information can be used to help understand what types of other users have chosen select countries. For example, we can see what age range of men booked trips to France in 2015 and compare this to the user's age and gender. This information would help determine whether or not the user would want to book a trip to this destination.

## Prerequisites

You will need the following libraries to run this project: 
  * numpy
  * pandas
  * matplotlib
  * seaborn
  * pickle
  * datetime  
  * sklearn
  * IPython
  * gc

