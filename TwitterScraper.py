import os
import re
import tweepy
from textblob import TextBlob
import tweepy as tw
import awswrangler.secretsmanager as sm
import time


class Menu:
    # default constructor

    def __init__(self):  # this defines and sets up menu
        self.__title = '----------------------   Main Menu   ----------------------'
        self.__description1 = 'This App will enable a search for recent Tweets on a default or user generated subject.'
        self.__description2 = 'These Tweets can then be analyzed for positive, negative or neutral polarity.'
        self.__option_one = '          Run analysis on default (#JoeRogan) subject.'
        self.__option_two = '          Choose your own subject to analyze.'
        self.__option_three = '          Print only positive Tweets.'
        self.__option_four = '          Print only negative Tweets.'
        self.__option_five = '          Print only neutral Tweets.'
        self.__option_six = '          Print positive, neutral, and negative Tweets and add them to Readme.txt.'
        self.__option_seven = '          Exit this awesome Application.'
        self.__exit_input = 7

    # get / set functions
    def get_title(self):  # defines title
        return self.__title

    def set_title(self, title):  # sets title
        self.__title = title

    def get_description1(self):  # defines first line of the description
        return self.__description1

    def set_description1(self, description1):  # sets the first line of description
        self.__description1 = description1

    def get_description2(self):  # defines second line of description
        return self.__description2

    def set_description2(self, description2):  # sets second line of description
        self.__description2 = description2

    def get_option_one(self):  # defines option 1
        return self.__option_one

    def set_option_one(self, option):  # sets option 1
        self.__option_one = option

    def get_option_two(self):  # defines option 2
        return self.__option_two

    def set_option_two(self, option):  # sets option 2
        self.__option_two = option

    def get_option_three(self):  # defines option 3
        return self.__option_three

    def set_option_three(self, option):  # sets option 3
        self.__option_three = option

    def get_option_four(self):  # defines option 4
        return self.__option_four

    def set_option_four(self, option):  # sets option 4
        self.__option_four = option

    def get_option_five(self):  # defines option 5
        return self.__option_five

    def set_option_five(self, option):  # sets option 5
        self.__option_five = option

    def get_option_six(self):  # defines option 6
        return self.__option_six

    def set_option_six(self, option):  # sets option 6
        self.__option_six = option

    def get_option_seven(self):  # defines option 7
        return self.__option_seven

    def set_option_seven(self, option):  # sets option 7
        self.__option_six = option

    def get_exit_input(self):  # defines exit input
        return self.__exit_input

    def set_exit_input(self, input):  # sets exit input
        self.__exit_input = input

    # object display function that shows the menu options
    def __str__(self):
        # display the menu with a formatted string when calling the object
        menu_string = '{}\n {}\n {}\n1. {}\n2. {}\n3. {}\n4. {}\n5. {}\n6. {}\n7. {}\n'.format(self.__title,
                                                                                               self.__description1,
                                                                                               self.__description2,
                                                                                               self.__option_one,
                                                                                               self.__option_two,
                                                                                               self.__option_three,
                                                                                               self.__option_four,
                                                                                               self.__option_five,
                                                                                               self.__option_six,
                                                                                               self.__option_seven,
                                                                                               self.__exit_input)
        return menu_string


# class for validating input
class Validator:
    # default constructor
    def __init__(self):
        self.__valid = False  # this block of code sets the start and finish of the validator
        self.__start = 1
        self.__end = 7

    #  the following code pieces are the get / set functions for the validator
    def get_valid(self):
        return self.__valid

    def set_valid(self, is_valid):
        self.__valid = is_valid

    def get_start(self):
        return self.__start

    def set_start(self, first):
        self.__start = first

    def get_end(self):
        return self.__end

    def set_end(self, last):
        self.__end = last

    # validation function
    def validate(self, integer):
        self.set_valid(False)
        # make sure the user has entered an integer.
        try:  # this block of code verifies that the data input is within the menu range
            option = int(integer)
            # make sure it's inside the range of options.
            if option < self.get_start() or option > self.get_end():
                print('')
                print('That number is not one of your choices.')
            else:
                self.set_valid(True)  # if a valid choice is made this allows the user to move forward
        # This is exception handling if the user puts something other than an integer
        except ValueError:
            print('')
            print('That is not even an integer. Try again please.')
            print('')
            main()
        return self.get_valid()  # returns the user back to menu choices to input a valid number

    def __str__(self):
        validator_string = 'Valid: {}\nStart: {}\nEnd: {}'.format(self.__valid, self.__start, self.__end)
        return validator_string


def main():
    # set up main menu
    main_menu = Menu()
    main_validator = Validator()
    keep_going = True
    main_validator.set_valid(False)
    # stop if user enters the exit choice.
    while keep_going:
        # validate the input.
        if main_validator.get_valid() == False:
            # display the main menu and prompt for choice.
            print(main_menu)
            print('')
            validate_option: str = input('Enter number (1-7) for choice: ')
            main_validator.validate(validate_option)
        menu_option = int(validate_option)
        # determine which function to run based on user input. if they enter 5, application will quit.
        if menu_option == 1:
            menu_option = 1
            DefaultClient(menu_option)
            main_validator.set_valid(False)
        elif menu_option == 2:
            menu_option = 2
            DefaultClient(menu_option)
            main_validator.set_valid(False)
        elif menu_option == 3:
            menu_option = 3
            DefaultClient(menu_option)
            main_validator.set_valid(False)
        elif menu_option == 4:
            menu_option = 4
            DefaultClient(menu_option)
        elif menu_option == 5:
            menu_option = 5
            DefaultClient(menu_option)
            main_validator.set_valid(False)
        elif menu_option == 6:
            menu_option = 6
            DefaultClient(menu_option)
            main_validator.set_valid(False)
        elif menu_option == 7:
            time.sleep(2)
            quit_answer = input("This has been very informative. Would you like to keep analyzing (Y or N)? ")
            if quit_answer.upper() == "N":  # turns user input to upper and checks for N to quit
                keep_going = False
                try:
                    os.remove('readme.txt')
                except Exception as err:
                    print(err)
                exit()
            elif quit_answer.upper() == "Y":
                print("Awesome, let's do this!")  # this block converts user input to upper and checks for Y
                keep_going = True  # if Y is entered, user is taken back to main menu
                main()

            else:
                print('That is not a valid option. Please choose Y or N.')


class TwitterClient(object):

    def __init__(self):
        # keys and tokens from the Twitter Dev Console
        API_Key = sm.get_secret_json("TwitterAPI").get('API_Key')
        API_Secret_Key = sm.get_secret_json("TwitterAPI").get('API_Secret_Key')
        Access_Token = sm.get_secret_json("TwitterAPI").get('Access_Token')
        Access_Token_Secret = sm.get_secret_json("TwitterAPI").get('Access_Token_Secret')

        self.auth = tw.OAuthHandler(API_Key, API_Secret_Key)
        self.auth.set_access_token(Access_Token, Access_Token_Secret)
        self.api = tw.API(self.auth, wait_on_rate_limit=True)

    def clean_tweet(self, tweet):
        # return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])
        # (\w+:\/\/\S+)", " ", tweet).split())
        clean_tweet = re.sub('@[A-Za-z0-9_]+', "", tweet)
        clean_tweet = re.sub('#[A-Za-z0-9_]+', "", clean_tweet)
        tweet = clean_tweet
        return tweet

    def get_tweet_sentiment(self, tweet):
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count=200):
        # empty list to store parsed tweets
        tweets = []

        try:
            # call Twitter api to fetch tweets
            fetched_tweets = self.api.search_tweets(q=query, count=count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {'text': tweet.text, 'sentiment': self.get_tweet_sentiment(tweet.text)}

                # saving text of tweet
                # saving sentiment of tweet

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepyException as e:
            # print error (if any)
            print("Error : " + str(e))


def DefaultClient(menu_option):
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    if menu_option == 1:
        query = "#JoeRogan"
        try:
            new_file = open('query.txt', 'w')
            new_file.write(str(query) + '\n')
            new_file.close()
            print('')
        except Exception as err:
            print(err)
        tweets = api.get_tweets(query='#JoeRogan', count=200)
        GetTweets(tweets, query, menu_option)
    elif menu_option == 2:
        query = input("Input your subject of choice preceded by the # sign: ")
        try:
            new_file = open('query.txt', 'w')
            new_file.write(str(query) + '\n')
            new_file.close()
            print('')
        except Exception as err:
            print(err)
        tweets = api.get_tweets(query=query, count=200)
        GetTweets(tweets, query, menu_option)
    elif menu_option == 3:
        try:
            with open('query.txt') as f:
                query = f.readlines()
                f.close()
        except Exception as err:
            print(err)
        tweets = api.get_tweets(query=query, count=200)
        GetTweets(tweets, query, menu_option)
    elif menu_option == 4:
        try:
            with open('query.txt') as f:
                query = f.readlines()
                f.close()
        except Exception as err:
            print(err)
        tweets = api.get_tweets(query=query, count=200)
        GetTweets(tweets, query, menu_option)
    elif menu_option == 5:
        try:
            with open('query.txt') as f:
                query = f.readlines()
                f.close()
        except Exception as err:
            print(err)
        tweets = api.get_tweets(query=query, count=200)
        GetTweets(tweets, query, menu_option)
    elif menu_option == 6:
        try:
            with open('query.txt') as f:
                query = f.readlines()
                f.close()
        except Exception as err:
            print(err)
        tweets = api.get_tweets(query=query, count=200)
        GetTweets(tweets, query, menu_option)


def GetTweets(tweets, query, menu_option):
    if menu_option <= 2:
        try:
            ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
            ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
            neutweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
            # picking positive tweets from tweets
            print('Here is the polarity breakdown of ' + query + ':')
            DefinePtweets(tweets, ptweets)
            DefineNtweets(tweets, ntweets)
            DefineNeutweets(tweets, ptweets, ntweets)
        except Exception as err:
            print(err)
    elif menu_option == 3:
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        DefinePtweets(tweets, ptweets)
        print("\n\nPositive Tweets:")
        for tweet in ptweets[:200]:
            print(tweet['text'])
    elif menu_option == 4:
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        print("\n\nNegative Tweets:")
        for tweet in ntweets[:200]:
            print(tweet['text'])
    elif menu_option == 5:
        neutweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
        print("\n\nNeutral Tweets:")
        for tweet in neutweets[:200]:
            print(tweet['text'])
    elif menu_option == 6:
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        neutweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
        print("\n\nPositive Tweets:")
        for tweet in ptweets[:200]:
            print(tweet['text'])
            try:
                new_file = open('readme.txt', 'a')
                new_file.write("\n\nPositive Tweet:")
                new_file.write(tweet['text'])
                new_file.close()
                print('')
            except Exception as err:
                print(err)
        print("\n\nNeutral Tweets:")
        for tweet in neutweets[:200]:
            print(tweet['text'])
            try:
                new_file = open('readme.txt', 'a')
                new_file.write("\n\nNeutral Tweet:")
                new_file.write(tweet['text'])
                new_file.close()
                print('')
            except Exception as err:
                print(err)
        print("\n\nNegative Tweets:")
        for tweet in ntweets[:200]:
            print(tweet['text'])
            try:
                new_file = open('readme.txt', 'a')
                new_file.write("\n\nNegative Tweet:")
                new_file.write(tweet['text'])
                new_file.close()
                print('')
            except Exception as err:
                print(err)


def DefinePtweets(tweets, ptweets):
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))


def DefineNtweets(tweets, ntweets):
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))


def DefineNeutweets(tweets, ntweets, ptweets):
    # percentage of neutral tweets
    print(
        "Neutral tweets percentage: {} %".format(100 * (len(tweets) - (len(ntweets) + len(ptweets))) / len(tweets)))


main()
