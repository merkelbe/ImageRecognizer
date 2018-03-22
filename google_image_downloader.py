import os, sys, time
import json, requests, shutil
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
from io import BytesIO
import urllib


# adding path to geckodriver to the OS environment variable
os.environ["PATH"] += os.pathsep + os.getcwd()
train_path = "images/train/"
validate_path = "images/valid/"

# downloads number of requested images of Google image search of 'searchtext' and splits them into a train / validate folder directory by search term.
def download_images(searchtext,num_requested):
	#searchtext = sys.argv[1]
	#num_requested = int(sys.argv[2])
    number_of_scrolls = num_requested / 400 + 1 
	# number_of_scrolls * 400 images will be opened in the browser
    
    # Deletes images of search path in train and validate folder if they already exist
    specific_train_path = train_path + str(searchtext)
    if os.path.exists(specific_train_path):
        shutil.rmtree(specific_train_path)
    
    specific_validate_path = validate_path + str(searchtext) 
    if os.path.exists(specific_validate_path):
        shutil.rmtree(specific_validate_path)    

    # Creates train and validate folder for search text if they don't exist
    if not os.path.exists(train_path + searchtext.replace(" ", "_")):
        os.makedirs(train_path + searchtext.replace(" ", "_"))

    if not os.path.exists(validate_path + searchtext.replace(" ", "_")):
        os.makedirs(validate_path + searchtext.replace(" ", "_"))

    url = f'https://www.google.co.in/search?q={searchtext}&source=lnms&tbm=isch'
    driver = webdriver.Firefox()
    driver.get(url)

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    extensions = { "jpg", "jpeg", "png", "gif" }
    img_count = 0
    train_img_count = 0
    validate_img_count = 0
    validate_ratio = 0.2
	
    for _ in range(int(number_of_scrolls)):
        for __ in range(10):
			# multiple scrolls needed to show all 400 images
            driver.execute_script("window.scrollBy(0, 1000000)")
            time.sleep(0.2)
		# to load next 400 images
        time.sleep(0.5)

        try:
            driver.find_element_by_xpath("//input[@value='Show more results']").click()

        except Exception as e:
            print (f'Less images found: {e}')
            break

    #imges = driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')
    #print ("Total images:", len(imges), "\n")

    imges = driver.find_elements_by_xpath("//img[@class='rg_ic rg_i']")
    
    for img in imges:
        img_count += 1
        img_url = img.get_attribute("src")
        img_type = "jpg"        

        print (f'Downloading image {img_count} : {img_url}')

        try:
            if random.uniform(0,1) > validate_ratio:
                urllib.request.urlretrieve(img_url,"./images/train/"+searchtext+"/"+searchtext+"."+str(validate_img_count+train_img_count)+"."+img_type)
                validate_img_count += 1
            else:
                urllib.request.urlretrieve(img_url,"./images/valid/"+searchtext+"/"+searchtext+"."+str(validate_img_count+train_img_count)+"."+img_type)
                train_img_count += 1 
        except Exception as e:
            print (f'Download failed: {e}')

        finally:
            print('')

        if validate_img_count + train_img_count >= num_requested:
            break

        #img_count += 1
        #img_url = json.loads(img.get_attribute('innerHTML'))["ou"]
        #img_type = json.loads(img.get_attribute('innerHTML'))["ity"]
        #print (f'Downloading image {img_count} : {img_url}')

        #try:
        #    if img_type not in extensions: 
        #        img_type = "png"

        #    r = requests.get(img_url, stream=True, headers=headers)
        #    if r.status_code == 200:
        #        if random.uniform(0,1) < validate_ratio:
        #            with open(validate_path + searchtext.replace(" ", "_") + "/" + searchtext + "." + str(validate_img_count + train_img_count) + "." + img_type, "wb") as f:
        #                r.raw.decode_content = True
        #                shutil.copyfileobj(r.raw, f)
        #                validate_img_count += 1
        #        else:
        #            with open(train_path + searchtext.replace(" ", "_") + "/" + searchtext + "." + str(validate_img_count + train_img_count) + "." + img_type, "wb") as f:
        #                r.raw.decode_content = True
        #                shutil.copyfileobj(r.raw, f)
        #                train_img_count += 1 
        #except Exception as e:
        #    print (f'Download failed: {e}')

        #finally:
        #    print('')

        #if validate_img_count + train_img_count >= num_requested:
        #    break

    print (f'Total downloaded: {validate_img_count + train_img_count}/{img_count}')
    driver.quit()