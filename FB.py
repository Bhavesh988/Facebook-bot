from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
ctx= ssl.create_default_context()
ctx.check_hostname = False
ctx.verifymode = ssl.CERT_NONE

# #opens browser
#browser  = webdriver.Chrome(ChromeDriverManager().install())
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--disable-notifications")
browser = webdriver.Chrome(ChromeDriverManager().install(),options=option)
friends_html = 'db/index.html'
class Facebook:
    def main():
        browser.get('https://en-gb.facebook.com/login/')
    #print("FB Username - ")
    #inputs
        try:
            fb_username=input("FB Username - ")
            fb_password=input("FB password - ")
    #sends info to input boxes
            browser.find_element_by_name("email").send_keys(fb_username)
            browser.find_element_by_name("pass").send_keys(fb_password)
    #clicks login button
            browser.find_element_by_id('loginbutton').click()
            time.sleep(5)
            #browser.close()
            print("\n\n")
        except NoSuchElementException:
            print("Invalid Login")
        
        argument=1
        i=1
        while(argument>=1 and argument<=4):
            argument = int(input("1:To add a friend of same city\n2:Update account status\n3:Open timeline of a random friend and comment on the most recent post.\n4:Exit\nEnter choice  = "))
            if argument==1:
                add(i)
                i=i+1
            elif argument==2:
                update()
            elif argument==3:
                comment()
            else:
                print("\nEXIT\n")
                break
            print("\n\n")
    #presses home button
    #browser.find_element_by_class_name('_2s25').click()
    #city div id name = nc684nl6
def add(i):
    browser.get('https://www.facebook.com/me/')
    time.sleep(5)
    address=browser.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/ul/div/div[2]/div/div/span/a/div/span').text
    browser.get('https://www.facebook.com/search/people/?q='+address)
    time.sleep(5)
    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div["+str(i)+"]/div/div/div/div/div/div/div[3]/span/div").click()
    print("\nFriend Added\n")      
def update():
    browser.get('https://www.facebook.com/me/')
    time.sleep(5)
    status=input("Enter status :- ")
    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/span/span/div").click()
    time.sleep(1)
    status_area=browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/span/div/div/label/textarea")
    status_area.send_keys(Keys.CONTROL + "a")
    status_area.send_keys(Keys.DELETE)
    time.sleep(3)
    status_area.send_keys(status)
    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/span/div/div/div[2]/div[2]/div[2]/div[1]/div/span/span").click()
    time.sleep(2)
    browser.get("https://www.facebook.com")
    print("\nStatus updated")
    time.sleep(4)

def comment():
    browser.get("https://www.facebook.com/me/friends")
    time.sleep(5)
    while browser.find_elements_by_css_selector('#m_more_friends'):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    #Save friend list
    with open (friends_html, 'w') as f:
        f.write(browser.page_source)
        print('%s) Downloaded' % friends_html)


Facebook.main()