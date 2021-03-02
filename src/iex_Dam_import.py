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

def iex_Dam_import():
    # set download directory path
    p = {'download.default_directory':r'C:\Users\dheer\Desktop\wrldc\RTM_REPORT_AUTOMATION\Dumps\iexDamFile'}
    #add options to browser
    opts.add_experimental_option('prefs', p)

    browser = Chrome(options=opts)
    #maximize browser
    browser.maximize_window()
    browser.get('https://www.iexindia.com/marketdata/market_snapshot.aspx')
    # TEST WAIT UNTIL IN SELENIUM
    delay = 60 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'ctl00_InnerContent_ddlPeriod')))
    except TimeoutException:
        print("Loading took too much time!")
    # click on the dropdown button
    iexDrpdwnDam = Select(browser.find_elements_by_id("ctl00_InnerContent_ddlPeriod")[0])

    # select element of dropdown by index
    iexDrpdwnDam.select_by_index(0)

    # working with radio and checkbox buttons ctl00_InnerContent_cbViewGraph
    status = browser.find_elements_by_id("ctl00_InnerContent_cbViewGraph")[0].is_selected()
    # deselecting the graph button
    browser.find_elements_by_id("ctl00_InnerContent_cbViewGraph")[0].click()

    # click on update report ctl00_InnerContent_btnUpdateReport
    browser.find_elements_by_id("ctl00_InnerContent_btnUpdateReport")[0].click()
    # wait until dropdown is opened 
    dropdownLinks = []
    delay = 60 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'ctl00_InnerContent_reportViewer_ctl05_ctl04_ctl00_ButtonLink')))
    except TimeoutException:
        print("Loading took too much time!")
    # click on different download option ctl00_InnerContent_reportViewer_ctl05_ctl04_ctl00_ButtonLink
    browser.find_elements_by_id("ctl00_InnerContent_reportViewer_ctl05_ctl04_ctl00_ButtonLink")[0].click()

    srcFileLocation = r'C:\Users\dheer\Desktop\wrldc\RTM_REPORT_AUTOMATION\Dumps\iexDamFile'
    destFileLocation = r'C:\Users\dheer\Desktop\wrldc\RTM_REPORT_AUTOMATION\Dumps\iexDamFile\Archives'
    destFileName = "MarketMinute_"
    moveFilesToArchive(srcFileLocation, destFileLocation, destFileName)
    delay = 60 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'Excel')))
    except TimeoutException:
        print("Loading took too much time!")
    browser.find_elements(By.LINK_TEXT,"Excel")[0].click()
    print("iex dam fetch succesful")

    time.sleep(10)
    browser.close()