#! python3

import os, json, time
from operations import data_downloader, date_extractor, data_extractor

def main ():
    url = 'https://www.brvm.org/fr/cours-actions/0'
    dt_scraped = []
    while True:
        #Download webpage
        file = data_downloader(url)

        #Extract the date of data
        date = date_extractor(file)

        #Check if not old data and then extract it
        if not date in dt_scraped:
            print(f'We are scraping data for {date}...')
            dt_scraped.append(date)
            stock_tb = data_extractor(file, date)

            #Store data in json
            file_path = os.getcwd()+'/data.txt'
            with open(file_path, 'a') as outfile:
                json.dump(stock_tb, outfile)
            print(f"Well done!")
        else :
            print('Current data has already been crawled')
        print(f"{len(dt_scraped)} data downloaded from brvm so far!")
        #Delay the proces for 24 hours before started again
        time.sleep(24*24*60)

if __name__ == "__main__":
    main()