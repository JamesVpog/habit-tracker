# James Vongphasouk
import requests as re
import logging
import http.client as http_client


http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

## user functions
def makeUser(user:str, token:str):    
    #user will not need to know token so generate a random string of random chars up to 9
    data = { "token":token, "username":user, "agreeTermsOfService":"yes", "notMinor":"yes"}

    r = re.post('https://pixe.la/v1/users', json=data)
    if r.status_code == 200:
        print("SUCCESSFULLY CREATED USER")
        # TODO: stores user and token in text file for retrieval, ask friends on how to store sensitive tokens on github
    else:
        print("FAILED TO CREATE USER")
        #if failed, then see why it failed based on message contents
        # TODO: prompt user to retry
    return r.text

def deleteUser(user:str, token:str):
    headers = {'X-USER-TOKEN': token}

    r = re.delete('https://pixe.la/v1/users/' + user, headers=headers)
    if r.status_code == 200:
        print("SUCCESSFULLY DELETED USER")
    else:
        print("FAILED TO DELETE USER")
    return r.text

def updateUserToken(user:str, token:str, newtoken:str):
    return 0

## graph functions on the user and its graph
def createGraph(user:str, token:str, graphid:str, graphname:str, unit:str):
    # ask user to specify type of quantity recorded (int or float)

    # ask user to specify color options (shibafu, momiji, sora, ichou, ajisai, kuro)
    return 0

def deleteGraph(user:str, token:str, graphid:str):
    return 0

def updateGraph(user:str, token:str, graphid:str):
    return 0

def viewGraph(user:str, graphid:str):
    return 0

## pixel functions on a graph
def updatePixel(user:str, graphid:str, date:str, quantity:str):
    #specify if want optional data
    return 0

def deletePixel(user:str, token:str, graphid:str, date:str):
    return 0


#testing print statements