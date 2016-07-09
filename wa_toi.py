from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
final_news = []
browser = webdriver.Chrome()
browser.get('http://web.whatsapp.com')
input()
while (1):
    code_box = urlopen('http://timesofindia.indiatimes.com/home/headlines').read()
    soup = BeautifulSoup(code_box, 'html.parser')
    top_headlines = soup.find_all("ul", { "class" : "content" }, limit=2)
    for lines in top_headlines:
	    ww  = lines.find_all("li")
	    for lines in ww:
		    final_news.append(lines.get_text())
    reciever = browser.find_element_by_xpath('//span[contains(text(),"15000 !")]')
    reciever.click()
    reciever_input = browser.find_elements_by_class_name('input')
    reciever_input[1].send_keys("so this is an automated message which shows you latest headlines from TOI  every 10 min")
    reciever_input[1].send_keys(Keys.SHIFT, Keys.RETURN)
    reciever_input[1].send_keys(Keys.SHIFT, Keys.RETURN)
    for report in final_news:
        reciever_input[1].send_keys(report)
        reciever_input[1].send_keys(Keys.SHIFT, Keys.RETURN)
    reciever_input[1].send_keys("© Sachin :D ")    
    browser.find_element_by_class_name('send-container').click()
    final_news[:] = []
    time.sleep(600)