from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from utils.move_file_to_archive import moveFilesToArchive
opts = Options()

def iex_Rtm_import():
    # set download directory path
    p = {'download.default_directory':r'C:\Users\dheer\Desktop\wrldc\RTM_BROWSER_AUTOMATION\Dumps\iexRtmFile'}
    #add options to browser
    opts.add_experimental_option('prefs', p)

    browser = Chrome(options=opts)
    #maximize browser
    browser.maximize_window()
    # open the website "https://www.iexindia.com/marketdata/rtm_market_snapshot.aspx"
    browser.get('https://www.iexindia.com/marketdata/rtm_market_snapshot.aspx')
    # TEST WAIT UNTIL IN SELENIUM
    delay = 120 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'ctl00_InnerContent_ddlPeriod')))
    except TimeoutException:
        print("Loading took too much time!")
    # open the dropdown select button "ctl00_InnerContent_ddlPeriod" to select day
    iexDrpdwnDam = Select(browser.find_elements_by_id("ctl00_InnerContent_ddlPeriod")[0])

    # select day element of dropdown by index # "yesterday"
    iexDrpdwnDam.select_by_index(0)

    # click on update report buttton "ctl00_InnerContent_btnUpdateReport"
    browser.find_elements_by_id("ctl00_InnerContent_btnUpdateReport")[0].click()
    # updateReport.click()
    # wait until dropdown is opened 
    dropdownLinks = []
    delay = 60 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'ctl00_InnerContent_reportViewer_ctl05_ctl04_ctl00_ButtonImg')))
    except TimeoutException:
        print("Loading took too much time!")
    dropdownLinks = browser.find_elements_by_id("ctl00_InnerContent_reportViewer_ctl05_ctl04_ctl00_ButtonImg")

    # click on different download option button "ctl00_InnerContent_reportViewer_ctl05_ctl04_ctl00_ButtonLink"
    dropdownLinks[0].click()

    # move all iex files from "C:\Users\dheer\Desktop\wrldc\RTM_BROWSER_AUTOMATION\iexDamFile" to
    #                           "C:\Users\dheer\Desktop\wrldc\RTM_BROWSER_AUTOMATION\iexDamFile\Archives"
    srcFileLocation = r'C:\Users\dheer\Desktop\wrldc\RTM_BROWSER_AUTOMATION\Dumps\iexRtmFile'
    destFileLocation = r'C:\Users\dheer\Desktop\wrldc\RTM_BROWSER_AUTOMATION\Dumps\iexRtmFile\Archives'
    destFileName = "MarketMinute_"
    moveFilesToArchive(srcFileLocation, destFileLocation, destFileName)

    excelLinks = []
    delay = 60 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'Excel')))
    except TimeoutException:
        print("Loading took too much time!")
    excelLinks = browser.find_elements(By.LINK_TEXT,"Excel")

    excelLinks[0].click()

    print("iex rtm fetch succesful")

    time.sleep(15)
    browser.close()