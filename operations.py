import requests, bs4

def data_downloader(url):
    res = requests.get(url)
    res.raise_for_status()
    res_soup = bs4.BeautifulSoup(res.text, 'lxml')
    return res_soup

def date_extractor(soup):
    month = ['janvier,', 'fevrier,', 'mars,', 'avril,', 'mai,', 'juin,',
            'juillet,', 'aout,', 'septembre,', 'octobre,', 'novembre,', 'décembre,']
    date = soup.select('#block-tools-date-maj')[0].getText().strip()
    wList = date.split(' ')
    if wList[7] in month:
        m = month.index(wList[7])+1
        date = '/'.join([wList[6], str(m), wList[8]]).replace(',', '')
    else :
        date = '-'.join([wList[6], wList[7], wList[8]]).replace(',', '')
    return date

def data_extractor(soup, date):
    data = {}
    data[date]=[]
    tr_list = soup.select('#block-system-main > div > table > tbody > tr')
    for tr in tr_list :
        stk = tr.select('td')
        code = stk[0].getText()
        label = stk[1].getText()
        volume = stk[2].getText().strip(' ').replace(' ', '')
        cours = stk[4].getText().replace(' ', '')
        data[date].append({'code': code, 'label': label, 'volume':volume, 'cours':cours})
    return data

