from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os
import gettext
import datetime as dt
from utils.move_file_to_archive import moveFilesToArchive
from utils.getWbesMaxRev import getMaxRTMRevForDate
opts = Options()

def wbes_Rtm_iex_import():
    # set download directory path
    p = {'download.default_directory':r'C:\Users\dheer\Desktop\wrldc\RTM_BROWSER_AUTOMATION\Dumps\wbesRtmIexFile'}
    #add options to browser
    opts.add_experimental_option('prefs', p)
    # click on the datepicker select button 
    previousDate = dt.datetime.today() - dt.timedelta(days=1)
    previousDateFormatted = previousDate.strftime('%d-%m-%Y') # format the date to dd-mm-yyyy
    month = previousDate.strftime('%B')
    prevDate = previousDate.strftime('%d')
    prevDate = int(prevDate)
    prevDate = str(prevDate)
    browser = Chrome(options=opts)
    #maximize browser
    browser.maximize_window()
    wbesRtmIexUrl = 'https://wbes.wrldc.in/Report/RTMIndex#date={}|revisionno=null|type=13'.format(previousDateFormatted)
    browser.get(wbesRtmIexUrl)
    # TEST WAIT UNTIL IN SELENIUM
    delay = 60 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'newEffectiveDate')))
    except TimeoutException:
        print("Loading took too much time!")
    # open the calender menu
    browser.find_elements_by_xpath("//*[@id=\"newEffectiveDate\"]")[0].click()
    # get the month year from website
    while(True):
        t = browser.find_elements_by_xpath("//*[@id=\"ui-datepicker-div\"]/div/div/span[1]")
        monthString = t[0].text
        if month == monthString:
            break
        else:
            browser.find_elements_by_xpath("//*[@id=\"ui-datepicker-div\"]/div/a[1]")[0].click()

    dateString = browser.find_elements_by_xpath("//*[@id=\"ui-datepicker-div\"]/table/tbody/tr/td/a")
    for t in dateString:
        if prevDate == t.text:
            t.click()
            break
    delay = 60 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'dwnld')))
    except TimeoutException:
        print("Loading took too much time!")

    # click on different download option dwnld
    browser.find_elements_by_id("dwnld")[0].click()

    srcFileLocation = r'C:\Users\dheer\Desktop\wrldc\RTM_BROWSER_AUTOMATION\Dumps\wbesRtmIexFile'
    destFileLocation = r'C:\Users\dheer\Desktop\wrldc\RTM_BROWSER_AUTOMATION\Dumps\wbesRtmIexFile\Archives'
    revNum = getMaxRTMRevForDate(previousDateFormatted,13)
    destFileName = "Report-RTM_IEX-("+revNum+")-"
    moveFilesToArchive(srcFileLocation, destFileLocation, destFileName)
    delay = 60 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'CSV')))
    except TimeoutException:
        print("Loading took too much time!")
    browser.find_elements(By.LINK_TEXT,"Excel")[0].click()
    print("wbes RTM IEX fetch succesful")

    time.sleep(10)
    browser.close()
    os.chdir(srcFileLocation)
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".xlsx"):
            y=filename
            x=filename.replace('('+revNum+')','(47)')
            os.rename(os.path.join(srcFileLocation, y), os.path.join(srcFileLocation, x))
