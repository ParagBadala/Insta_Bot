# importing ACCESS_TOKEN
from access_keys import ACCESS_TOKEN

# importing requests Package
import requests, urllib

# importing textblob package for analyzing the sentence
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

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


# Function to get post with maximum likes

def max_like(user_media):
    like=0
    for x in range(0,len(user_media['data'])):
        if(like<user_media['data'][x]['likes']['count']):
            like=user_media['data'][x]['likes']['count']
            z=x
    if(like==0):
        print(colored("All post of user have ZERO likes, So getting the most recent post",'red'))
        recent_post(user_media)
    else:
        image_name = user_media['data'][z]['id'] + '.jpeg'
        image_url = user_media['data'][z]['images']['standard_resolution']['url']
        urllib.urlretrieve(image_url, image_name)
        print (colored('Your image with most number of likes has been downloaded!','red'))


# Function to get post with minimum likes

def min_like(user_media):
    like = 999999
    for x in range(0, len(user_media['data'])):
        if (like > user_media['data'][x]['likes']['count']):
            like = user_media['data'][x]['likes']['count']
            z = x
    if (like == 0):
        print(colored("All post of user have ZERO likes, So getting the most recent post", 'red'))
        recent_post(user_media)
    else:
        image_name = user_media['data'][z]['id'] + '.jpeg'
        image_url = user_media['data'][z]['images']['standard_resolution']['url']
        urllib.urlretrieve(image_url, image_name)
        print (colored('Your image with minimum number of likes has been downloaded!', 'red'))


# Function for getting most recent post

def recent_post(user_media):
    image_name = user_media['data'][0]['id'] + '.jpeg'
    image_url = user_media['data'][0]['images']['standard_resolution']['url']
    urllib.urlretrieve(image_url, image_name)
    print (colored('Your image has been downloaded!','red'))

# Function to get the post of a user by username

def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print("User does not exist!")
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):

            while True:
                print"\n"
                print(colored("---------------SELECT THE OPTION--------------------\n",'green'))
                print("1.Get the post with maximum likes")
                print("2.Get the post with minimum likes")
                #print("3.Get the most recent post liked by the user")
                print("4.Get the most recent post")
                print("5.Return to main menu")
                select=int(raw_input("Enter the choice"))
                if select==1:
                    max_like(user_media)
                elif select==2:
                    min_like(user_media)
                elif select==4:
                    recent_post(user_media)
                elif select==5:
                    break;
                else:
                    print("Invalid choice")
        else:
            print("Post does not exist!")
    else:
        print("Status code other than 200 received!")


# Function declaration to get the ID of the recent post of a user by username

def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print("User does not exist!")
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print("There is no recent post of the user!")
            exit()
    else:
        print("Status code other than 200 received!")
        exit()

# Function to get recent media liked by the user

def recent_post_like():
    request_url = (BASE_URL + 'users/self/media/liked?access_token=%s') % (ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()
    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print(colored("Your image has been downloaded!","red"))
        else:
            print(colored("Post does not exist!","red"))
    else:
        print(colored("Status code other than 200 received!","red"))


# Function to fetch the user who have liked the recent post

def get_like_list(insta_username):
    post_id = get_post_id(insta_username)
    request_url = (BASE_URL+ 'media/%s/likes?access_token=%s') % (post_id,ACCESS_TOKEN)
    likes_info = requests.get(request_url).json()

    if likes_info['meta']['code'] == 200:
        if len(likes_info['data']):
            print(colored("People likes the post are :","red"))
            for x in range(0,len(likes_info['data'])):
                print(likes_info['data'][x]['username'])
        else:
            print("No user have liked the post ")
    else:
        print("Status code other than 200 received!")






# Function to like the recent post of a user

def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()

    if post_a_like['meta']['code'] == 200:
        print(colored("Like was successful!","red"))
    else:
        print(colored("Your like was unsuccessful. Try again!","red"))

#Function to get list of comments

def get_comment_list(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL+ 'media/%s/comments?access_token=%s') % (media_id, ACCESS_TOKEN)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200 :
        if len(comment_info['data']):
            print(colored("COMMENTS ON THE POST ARE :","red"))
            for x in range(0,len(comment_info['data'])):
                print("Comments : %s  || User : %s") % (comment_info['data'][x]['text'],comment_info['data'][x]['from']['username'])
        else:
            print(colored("No comments on this post","red"))
    else:
        print(colored("Status code other than 200 received","red"))


# Function to make a comment on recent post

def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("Give comment: ")
    payload = {"access_token": ACCESS_TOKEN, "text" : comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print (colored("Successfully added a new comment!","red"))
    else:
        print (colored("Unable to add comment. Try again!","red"))


#Function to delete negative comment

def delete_negative_comment(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            # NaiveBayesAnalyzer to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print(colored("Comment successfully deleted!\n","red"))
                    else:
                        print(colored("Unable to delete comment!","red"))
                else:
                    print(colored("Positive comment : %s\n' % (comment_text)","red"))
        else:
            print(colored("There are no existing comments on the post!","red"))
    else:
        print(colored("Status code other than 200 received!","red"))

def start_bot():
    while True:
        print (colored('*******************Here are your menu options:*****************************', 'blue'))
        print("\n")
        print ("1.Get your own details")
        print ("2.Get details of a user by username")
        print ("3.Get your own recent post")
        print ("4.Get the recent post of a user by username")
        print ("5.Get the recent post liked by the user ")
        print ("6.Get a list of people who have liked the recent post of a user")
        print ("7.Like the post")
        print ("8.List the comments on the post")
        print ("9.Post the comment")
        print ("10.Delete the negative comment")
        print ("11.Exit\n")

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
            recent_post_like()
        elif choice==6:
            insta_username = raw_input("Enter the username of the user: ")
            get_like_list(insta_username)
        elif choice == 7:
            insta_username = raw_input("Enter the username of the user: ")
            like_a_post(insta_username)
        elif choice==8:
            insta_username = raw_input("Enter the username of the user : ")
            get_comment_list(insta_username)
        elif choice==9:
            insta_username = raw_input("Enter the username of the user : ")
            post_a_comment(insta_username)
        elif choice==10:
            insta_username = raw_input("Enter the username of the user : ")
            delete_negative_comment(insta_username)
        elif choice==11:
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

#asking username for which bot will perform action
#insta_username = raw_input("Enter the username of the user : ")
start_bot()

