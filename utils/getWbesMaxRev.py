import datetime as dt
import requests
import re

# get default headers for requests
def getDefaultReqHeaders():
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3887.7 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    }

def getMaxRTMRevForDate(revDt,iex_pxi):
    headers = getDefaultReqHeaders()
    # https://wbes.wrldc.in/Report/GetRTMRevisionNoByDate?date=22-01-2021&typeId=13
    revUrl = "https://wbes.wrldc.in/Report/GetRTMRevisionNoByDate?date={0}&typeId={1}".format(revDt,iex_pxi)
    r = requests.get(revUrl, headers=headers)
    revsObjs = r.json()
    return revsObjs[0]['revisionNo']
# previousDate = dt.datetime.today() - dt.timedelta(days=1)
# print(getMaxRTMRevForDate(previousDate))


# token value =  int(dt.datetime.timestamp(dt.datetime.now())*1000)