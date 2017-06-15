#importing ACCESS_TOKEN
from keys import ACCESS_TOKEN

#importing requests Package
import requests

#BASE_URL for getting self_info of instagram
BASE_URL = "https://api.instagram.com/v1/"

# Function for extracting our own info

def self_info():
    request_url = (BASE_URL +'users/self/?access_token=%s') % (ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if(user_info['meta']['code']==200):
        if(len(user_info['data'])):
            print"USERNAME"







print "================================="
print "            InstaBot             "
print "    Developed by PARAG BADALA  "
print "================================="
print ""
