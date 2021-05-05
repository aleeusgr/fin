def fetch_files(filing ='13F-HR' , CIK = "0000102909", save_path = './data'):
    '''depends on parse()'''
    import os
    from sec_edgar_downloader import Downloader
    dl = Downloader(save_path)
    dl.get(filing, CIK)
    CIK = CIK.lstrip("0")
    files = os.listdir("{}/sec-edgar-filings/".format(save_path) + CIK + "/" + filing +'/')
    data = [parse(file, CIK) for file in sorted(files)]
    try:
        return pd.concat(data)
    except ValueError:
        print("All Values are None")
        return None


def view_local_data(save_path = './data',cik = "0000102909",filing):
    ''' temporary? 
    view local dir
    '''
    location = "{}/sec-edgar-filings/{}/{}/".format(save_path, cik, filing = '13F-HR')
    return os.listdir(location)

def parse(file, CIK,filing = forms[0], save_path = './data'):

    import datetime
    import pandas as pd

    location = "{}/sec-edgar-filings/{}/{}/{}/".format(save_path, cik, filing, file)
    # implement parsing algorithm
    with open(location + 'full-submission.txt') as f:
        lines = f.readlines()
    return lines
