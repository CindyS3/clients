import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import sys

username = input('Username: ')
#username = sys.argv[1]
print(sys.argv)

def get_token(scope, 
              username = username, 
              client_id='a33dd60d2fd74c17a1bd6dc5d461eb60',
              client_secret='10be67083f994404bdf4366055bb5248'):
    token = util.prompt_for_user_token(username, 
                            scope = scope,
                            client_id=client_id,
                            client_secret=client_secret, 
                            redirect_uri='http://localhost:8888/callback')
    return token


scope = 'user-top-read'
print(2)
token = get_token(scope)
print(3)
print(token)