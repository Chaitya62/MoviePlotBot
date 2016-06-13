import json
from urllib.parse import urlencode
import urllib.request

main_url = "http://www.omdbapi.com/?"

parameter = {}

def json_decoder(response):
    decoder = json.JSONDecoder()
    return decoder.decode(response)

def make_query(t,plot='short'):
    parameter["t"] = t
    parameter["plot"] = plot
    query = urlencode(parameter)
    request_url = main_url + query
    return request_url
    
def request(request_url):
    with urllib.request.urlopen(request_url) as response:
        resp = response.read()
        resp = resp.decode('utf-8')
        result =  json_decoder(resp)
        try:
            return result['Plot']
        except:
            return ("The Movie doesn't exist or you haven't entered the correct name")

    
if __name__ == "__main__":
    print("Enter the Movie")
    print("Enter 'Q' or 'q' to quit")
    while True:
        q = input()
        if q == 'Q' or q == 'q':
            break
        url = make_query(q)
        plot = request(url)
        print(plot)
    
    

        
