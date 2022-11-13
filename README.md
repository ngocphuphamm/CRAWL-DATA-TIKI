# CRAWL-DATA-TIKI
## Introduction
Below is what you can do with this program:
- Get item product  data currently for sale on tiki .
- Get product data based on keyword.

Framework: scrapy-splash


## Install
1. Make sure you have docker installed.
2. docker pull scrapinghub/splash
3. docker run -p 8050:8050 scrapinghub/splash
4. pip install scrapy scrapy-splash
5. pip install shortuuid

## Crawler
### Usage
```
optional arguments:
  -a keyWord      : search for keywords crawl
  -a typeImage       : type images 
  -a limitProduct : number of product crawls
  -a pathName     : direct image
  -o              : output file name(json format,jcsv)
  
```
## Example
### OPTION 1: CRAWL CATEGORIES
```
scrapy crawl dataTiki  -o PATHNAME/NAME.json
```
```
scrapy crawl dataTiki  -a limitProduct=50 -a pathName=PATHNAME -a typeImage=png   -o PATHNAME/NAME.json
```
### OPTION 2: CRAWL KEYWORD
```
scrapy crawl dataTiki  -a keyWord=NAMEKEYWORD -o PATHNAME/NAME.json
```
```
scrapy crawl dataTiki -a keyWord=NAMEKEYWORD -a limitProduct=50  \
                      -a pathName=PATHNAME -a typeImage=png \
                      -o PATHNAME/NAME.json
```

### NOTE: 
You can leave out some parameters and it will be the default when crawling


