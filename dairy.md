blog on browser automation - https://realpython.com/modern-web-automation-with-python-and-selenium/

webdriver download page for firefox - https://github.com/mozilla/geckodriver/releases/tag/v0.29.0

webdriver download page for chrome - https://sites.google.com/a/chromium.org/chromedriver/downloads

get rtm data for today - https://wbes.wrldc.in/Report/ExportRTMReportDownload?effectiveDate=22-01-2021&getTokenValue=1611298105978&fileType=csv&Revision=23&Type=13

button click from python using selenium- 
        python_button = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
        python_button.click()

to select a dropdown based on id of select:
        iexDrpdwnDam = Select(browser.find_elements_by_id("ctl00_InnerContent_ddlPeriod")[0])

change downloads directory in selenium - https://www.tutorialspoint.com/downloading-file-to-specified-location-with-selenium-and-python