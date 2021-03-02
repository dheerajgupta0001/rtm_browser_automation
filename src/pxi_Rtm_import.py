from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import datetime as dt
import time
from utils.move_file_to_archive import moveFilesToArchive
opts = Options()

def pxi_Rtm_import():
    # set download directory path
    p = {'download.default_directory':r'C:\Users\dheer\Desktop\wrldc\RTM_REPORT_AUTOMATION\Dumps\pxiRtmFile'}
    #add options to browser
    opts.add_experimental_option('prefs', p)

    browser = Chrome(options=opts)
    #maximize browser
    browser.maximize_window()
    # open the website "https://www.powerexindia.com/code/frontend/Reports/RTM/MarketVolumeProfileReport.html/"
    browser.get('https://www.powerexindia.com/code/frontend/Reports/RTM/MarketVolumeProfileReport.html/')

    # click on the datepicker select button 
    previousDate = dt.datetime.today() - dt.timedelta(days=1)
    previousDateFormatted = previousDate.strftime ('%d-%m-%Y') # format the date to ddmmyyyy
    # provide previous date
    browser.find_elements_by_name("DeliveryfromDate")[0].send_keys(previousDateFormatted)
    # provide previous date to "DeliverytoDate"
    browser.find_elements_by_name("DeliverytoDate")[0].send_keys(previousDateFormatted)
    button = browser.find_elements_by_name('submit')
    button[0].click()

    # click on different download csv option button class =  "dt-button buttons-csv buttons-html5"
    # csvDwnLd = browser.find_element_by_css_selector("dt-button buttons-csv buttons-html5")
    csvDwnLd = browser.find_elements_by_tag_name("span")

    srcFileLocation = r'C:\Users\dheer\Desktop\wrldc\RTM_REPORT_AUTOMATION\Dumps\pxiRtmFile'
    destFileLocation = r'C:\Users\dheer\Desktop\wrldc\RTM_REPORT_AUTOMATION\Dumps\pxiRtmFile\Archives'
    destFileName = "DASMVPReport_"
    moveFilesToArchive(srcFileLocation, destFileLocation, destFileName)
    csvDwnLd[11].click()
    print("pxi rtm fetch succesful")

    time.sleep(10)
    browser.close()