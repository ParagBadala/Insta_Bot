# importing ACCESS_TOKEN
from access_keys import ACCESS_TOKEN

# importing requests Package
import requests, urllib

# BASE_URL for getting self_info of instagram
BASE_URL = "https://api.instagram.com/v1/"

# importing libraries for colored output
from termcolor import colored

# Function for extracting info

def self_info():
    # getting the user info
    request_url = (BASE_URL +'users/self/?access_token=%s') % (ACCESS_TOKEN)
    print 'GET request url : %s\n' % (request_url)
    # requesting for getting user information
    user_info = requests.get(request_url).json()

#   checking if user exits or not and printing its info
    if(user_info['meta']['code']==200):
        if(len(user_info['data'])):
            print (colored('Full Name  : %s' % (user_info['data']['full_name']), 'green'))
            print (colored('Username   : %s' % (user_info['data']['username']),'green'))
            print (colored('Followers  : %s' % (user_info['data']['counts']['followed_by']),'green'))
            print (colored('Following  : %s' % (user_info['data']['counts']['follows']),'green'))
            print (colored('Posts      : %s' % (user_info['data']['counts']['media']),'green'))

            # Website of the user
            if user_info['data']['website'] != '':
                print(colored('Website    :%s' % (user_info['data']['website']), 'green'))
            # Bio of the user
            if user_info['data']['bio'] != '':
                print(colored('Bio        :%s' % (user_info["data"]["bio"]), 'green'))
        else:
            print (colored('User does not exist!','red'))
    else:
        print (colored('Status code other than 200 received!','red'))

# Function to get ID of the user by username

def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username,ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    # requesting for getting user information
    user_info = requests.get(request_url).json()

    if(user_info['meta']['code']==200):
        if(len(user_info['data'])):
            user_id = user_info['data'][0]['id']
            # returns user id
            return user_id
        else:
            return none
    else:
        print (colored('Status code other than 200 received!', 'red'))


# Function to get user info using username


def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print(colored('Full Name    : %s' % (user_info['data']['full_name']), 'red'))
            print(colored('Username     : %s' % (user_info['data']['username']),'red'))
            print(colored('UserId       : %s' % (user_id), 'red'))
            print(colored('Followed By  : %s' % (user_info['data']['counts']['followed_by']),'red'))
            print(colored('Follows      : %s' % (user_info['data']['counts']['follows']),'red'))
            print(colored('Total Posts  : %s' % (user_info['data']['counts']['media']),'red'))

            # Website of the user is given
            if user_info['data']['website'] != '':
                print(colored('Website      :%s' % (user_info['data']['website']), 'blue'))
            # Bio of the user is given
            if user_info['data']['bio'] != '':
                print(colored('Bio          :%s' % (user_info["data"]["bio"]), 'blue'))

        else:
            print 'User does not exist!'


    else:
        print 'Status code other than 200 received!'


# Function for downloading the self post

def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


# Function to get the recent post of a user by username

def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


def start_bot():
    while True:
        print (colored('*******************Here are your menu options:*****************************', 'blue'))
        print("\n")
        print ("1.Get your own details")
        print ("2.Get details of a user by username")
        print ("3.Get your own recent post")
        print ("4.Get the recent post of a user by username")

        print ("5.Exit\n")

        choice=int(raw_input("Enter you choice: "))
        if choice==1:
            print("Extracting owners instagram info")
            self_info()
        elif choice==2:
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice==3:
            get_own_post()
        elif choice==4:
            insta_username = raw_input("Enter the username of the user : ")
            get_user_post(insta_username)
        elif choice==5:
            exit()
        else:
            print (colored("Invalid choice","red"))




print colored("==================================================================",'yellow')
print colored("                                 InstaBot             ",'red')
print colored("                         Developed by PARAG BADALA  ",'red')
print colored("====================================================================",'yellow')
print ""
print (colored('*******************Hey! Welcome to InstaBot!*******************************','blue'))
print ('\n')



start_bot()

