from selenium import webdriver


from selenium.webdriver.chrome.options import Options


from urllib.parse import urlsplit

import csv
from csv import writer
import time

actual_time = time.localtime()

g_url= "https://google.com/search?q="

params= "&filter=0&num=100"
#chromedriver path
executable_path=""
#change this to your keywords:
keywords = ["marketing",
"doing seo",
"seo is fun",
"learn python",
"learn seo",]

#function for writting down shit on a line
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


#setting up the webdriver
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path=executable_path, options=options)


def track_keyword(keyword):
    driver.get(g_url+keyword+ params)
    html_g_search = driver.find_elements_by_xpath('//*[@id="rso"]/div/div/div[1]/a')
    list_results=[]
    actual = str(actual_time.tm_hour)+":"+ str(actual_time.tm_min)
    year = str(actual_time.tm_year)+"/"+str(actual_time.tm_mon)+"/"+ str(actual_time.tm_mday)
    list_results.append(keyword)
    list_results.append(actual)
    list_results.append(year)
    for i in html_g_search:
              serp_url = i.get_attribute("href")
              print("url serp ", serp_url)
              list_results.append(str(serp_url))
    append_list_as_row("my_sites_tracking1.csv", list_results)
    time.sleep(10)

for keyword in keywords:
    track_keyword(keyword)
driver.close()
