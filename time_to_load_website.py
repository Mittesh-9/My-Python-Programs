from urllib.request import urlopen
import time

def get_load_time(url):
    if ("https" or "http") in url: # Checking for presence of protocols
        open_this_url = urlopen(url) # Open the url as entered by the user
    else:
        open_this_url = urlopen("https://" + url) # Adding https to the url
    
    start_time = time.time() # Time stamp before the reading of url starts
    open_this_url.read() # Reading the user defined url
    end_time = time.time() # Time stamp after the reading of the url
    open_this_url.close() # Closing the instance of the urlopen object
    time_to_load = end_time - start_time
    
    return time_to_load

if __name__ == "__main__":
    url = input("Enter the url: ")
    print(f"\nThe time taken to load {url} is {get_load_time(url):.2} seconds.") # for example type input google.com