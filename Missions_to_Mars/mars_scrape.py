#import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time
from selenium import webdriver
from urllib.parse import urlsplit

def init_browser():
    execute_path = {"executable_path":"C:\chromedriver_win32\chromedriver"}

    return Browser("chrome", **execute_path, headless = False)

def scrape():
    browser = init_browser()
    facts = {}

    nasa = "https://mars.nasa.gov/news/"
    browser.visit(nasa)
    time.sleep(2)

    html = browser.html
    soup = bs(html,"html.parser")

    #scrapping latest news about mars from nasa
    nasa_paragraph = soup.find("div", class_ = "article_teaser_body").text
    nasa_title = soup.find("div", class_ = "content_title").text
    facts['news_title'] = news_title
    facts['news_paragraph'] = news_paragraph 
    
    
    img = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars#submit"
    browser.visit(img)
    time.sleep(3)

    b_url = "{0.scheme}://{0.netloc}/".format(urlsplit(nasa_image))
    
    path = "//*[@id=\"page\"]/section[3]/div/ul/li[1]/a/div/div[2]/img"

    results = browser.find_by_xpath(path)
    img_x = results[0]
    img_x.click()
    time.sleep(3)
    
    img_html = browser.html
    soup = bs(img_html, "html.parser")
    image_url = soup.find("img", class_ = "fancybox-image")["src"]
    true_img_url = b_url + image_url
    facts["Main Image"] = true_img_url
    
   

    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)
    weather_html = browser.html
    soup = bs(weather_html, "html.parser")
    weather_on_mars = soup.find("p", class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    facts["Weather on Mars"] = weather_on_mars

   


    facts_url = "https://space-facts.com/mars/"    
    time.sleep(3)
    db = pd.read_html(facts_url)
    db[0]

    db_facts = db[0]
    db_facts.columns = ["Measurements", "Mars-Values","Earth-Values"]
    db_facts.set_index(["Measurements"])
    db_html = db_facts.to_html()
    db_html.replace("\n", "")
    facts["mars_facts_table"] = html_table

    

    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemi_url)

  

    hemi_url_base = "{0.scheme}://{0.netloc}/".format(urlsplit(hemi_url))
    hemi_images = []
    hemi_images


    returns1 = browser.find_by_xpath("//*[@id='product-section']/div[2]/div[1]/a/img")[0].click()
    time.sleep(2)
    click_cerb = browser.find_by_xpath("//*[@id='wide-image-toggle']")[0].click()
    time.sleep(1)
    img_cerb = browser.html
    soup = bs(img_cerb, "html.parser")
    url_cerb = soup.find("img", class_="wide-image")["src"]
    img_url_cerb = hemi_url_base + url_cerb
    title_cerb = soup.find("h2", class_ = "title").text
    go_back = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a")[0].click()
    cerb = {"Image":title_cerb, "Url": img_url_cerb}
    hemi_images.append(cerb)



    returns2 = browser.find_by_xpath("//*[@id='product-section']/div[2]/div[2]/a/img").first.click()
    time.sleep(3)
    click_schi = browser.find_by_xpath("//*[@id='wide-image-toggle']").first.click()
    time.sleep(3)
    img_schi = browser.html
    soup = bs(img_schi, "html.parser")
    url_schi = soup.find("img", class_="wide-image")["src"]
    img_url_schi = hemi_url_base + url_schi
    title_schi = soup.find("h2", class_ = "title").text
    go_back = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").first.click()
    schi = {"Image":title_schi, "Url": img_url_schi}
    hemi_images.append(schi)



    returns3 = browser.find_by_xpath("//*[@id='product-section']/div[2]/div[3]/a/img").first.click()
    time.sleep(3)
    click_syr_major = browser.find_by_xpath("//*[@id='wide-image-toggle']").first.click()
    time.sleep(3)
    img_syr_major = browser.html
    soup = bs(img_syr_major, "html.parser")
    url_syr_major = soup.find("img", class_="wide-image")["src"]
    img_url_syr_major = hemi_url + url_syr_major
    title_syr_major = soup.find("h2", class_ = "title").text
    go_back = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").first.click()
    syr_major = {"Image":title_syr_major, "Url": img_url_syr_major}
    hemi_images.append(syr_major)   


    returns4 = browser.find_by_xpath("//*[@id='product-section']/div[2]/div[4]/a/img").first.click()
    time.sleep(3)
    click_val_mari = browser.find_by_xpath("//*[@id='wide-image-toggle']").first.click()
    time.sleep(3)
    img_val_mari = browser.html
    soup = bs(img_val_mari, "html.parser")
    url_val_mari = soup.find("img", class_="wide-image")["src"]
    img_url_val_mari = hemi_url + url_val_mari
    title_val_mari = soup.find("h2", class_ = "title").text
    go_back = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").first.click()
    val_mari = {"Image":title_val_mari, "Url": img_url_val_mari}
    hemi_images.append(val_mari)


    facts["hemi_images"] = hemi_images

    

    return facts