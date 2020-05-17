import os

os.system('pipenv --python 3.7') 
os.system('pipenv install scrapy')
os.system('scrapy startproject new .')
os.system('cd new/')
os.system('scrapy genspider main www.com')    
os.system('pipenv install gspread') 
os.system('pipenv shell')