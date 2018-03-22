import os
import subprocess
#import get_google_images
#import google_images_download
import google_image_downloader

#Method 1 using get_google_images library
#get_google_images.search_images(["parrot"],[""],1000)

#Method 2 using googleimagesdownload exe and calling through subprocess

## Things you would like to differentiate with a neural net
#firstThing = 'parrot'
#secondThing = 'tiger'

#numberOfTrainPicturesToDownload = 5
#numberOfValidationPicturesToDownload = 400

#cwd = os.getcwd()

#picturesDirectory = cwd+"/pictures"
#trainDirectory = picturesDirectory+"/train"
#validationDirectory = picturesDirectory+"/valid"

#if not os.path.exists(picturesDirectory):
#    os.makedirs(picturesDirectory, exist_ok = True)

## Download images from google search of the things specified above
#firstImageBatchTrainDownloadCommand = 'googleimagesdownload --format jpg --keywords \"' + firstThing + '\" --limit \"'+str(numberOfTrainPicturesToDownload)+'\" --output_directory \"'+trainDirectory+'\"'
#secondImageBatchTrainDownloadCommand = 'googleimagesdownload --format jpg --keywords \"' + secondThing + '\" --limit \"'+str(numberOfTrainPicturesToDownload)+'\" --output_directory \"'+trainDirectory+'\"'
#firstImageBatchValidateDownloadCommand = 'googleimagesdownload --format jpg --keywords \"' + firstThing + '\" --limit \"'+str(numberOfValidationPicturesToDownload)+'\" --output_directory \"'+validationDirectory+'\"'
#secondImageBatchValidateDownloadCommand = 'googleimagesdownload --format jpg --keywords \"' + secondThing + '\" --limit \"'+str(numberOfValidationPicturesToDownload)+'\" --output_directory \"'+validationDirectory+'\"'

#subprocess.call(firstImageBatchTrainDownloadCommand)
#subprocess.call(secondImageBatchTrainDownloadCommand)
#subprocess.call(firstImageBatchValidateDownloadCommand)
#subprocess.call(secondImageBatchValidateDownloadCommand)

#Method 3 using google_image_downloader library
firstThing = 'cat'
secondThing = 'dog'

numberOfImagesToDownload = 10000

## downloads images found on Google image search and splits them into train / validate folders
#google_image_downloader.download_images(firstThing,numberOfImagesToDownload)
#google_image_downloader.download_images(secondThing,numberOfImagesToDownload)

## import fastai stuff
#from fastai.imports import *

#from fastai.transforms import *
#from fastai.conv_learner import *
#from fastai.model import *
#from fastai.dataset import *
#from fastai.sgdr import *
#from fastai.plots import *

#PATH = "images/"
#sz = 224

#arch = resnext50
#data = ImageClassifierData.from_paths(PATH, tfms = tfms_from_model(arch,sz))
#learn = ConvLearner.pretrained(arch,data,precompute=True)
#learn.fit(0.01,2)
#learn.save(str(firstThing)+"_"+str(secondThing)+"_"+str(sz))
