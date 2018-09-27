import datetime as d
# separator used by search.py, categories.py, ...
SEPARATOR = ";"

LANG            = "en_IN" # can be en_US, fr_FR, ...
ANDROID_ID      = "30E4B815A83CA973"  # "xxxxxxxxxxxxxxxx"
GOOGLE_LOGIN    = "digital.sec.devs@gmail.com"  # "username@gmail.com"
GOOGLE_PASSWORD = "dev@6395"
AUTH_TOKEN      = "aAX_7XGsaT4B5hIDvtdh8oM-R7B5iidTCgHxXOKQXXFDFdmdzPcXKslTr6SX0YpiDMIORA."
now = d.datetime.now()
month = now.month
year = now.year
DST_VER = "v_" + str(year) + "." + str(month)
BANNER = """
    _
   / \   _ __  _ __  ___  ___  ___ _   _ _ __ ___
  / _ \ | '_ \| '_ \/ __|/ _ |/ __| | | | '__/ _ |
 / ___ \| |_) | |_) \__ \  __/ (__| |_| | | |  __/
/_/   \_\ .__/| .__/|___/\___|\___|\__,_|_|  \___|
        |_|   |_|

"""


# force the user to edit this file
if any([each == None for each in [ANDROID_ID, GOOGLE_LOGIN, GOOGLE_PASSWORD]]):
    raise Exception("config.py not updated")

