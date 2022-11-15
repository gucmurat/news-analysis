# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 14:04:36 2022

@author: Murat
"""
# crawler
import os
os.system("pip3 install newspaper3k")
os.system("pip install Scrapy")
os.system("pip install bs4")
os.system("pip install datetime")
os.system("pip install nltk")

import nltk
nltk.download('punkt')

#sentiment-ner
os.system("pip install -U pip setuptools wheel")
os.system("pip install spacy")
os.system("pip install pandas")
os.system("pip install torch")
os.system("pip install transformers")
os.system("python -m spacy download en_core_web_sm")