import requests
import xml.etree.ElementTree as etree
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def parse_public_services(response):
    '''
    Parse xml data of public services in oulu region
    Arguments: Requests response object
    Returns: Pandas DataFrame
    '''
    root = etree.fromstring(response.text)
    # searchObjects element contains the entries
    objects = root.find('searchObjects')
    data = []
    for obj in objects:
        # get all attributes via dict comprehension
        values = {o.tag:o.text for o in obj.findall('*')}
        # geometry is defined by subelements X and Y or a Boundary with list of Xs and Ys
        geoms = obj.find('Geometry').findall('*')
        for val in geoms:
            values[val.tag] = val.text
        data.append(values)
    data = pd.DataFrame(data)
    # replace missing locations with first elements of Boundary data
    data['X'] = data['X'].fillna(data.Boundary.fillna('a a').str.split().str[0]).astype(np.float32)
    data['Y'] = data['Y'].fillna(data.Boundary.fillna('a a').str.split().str[1]).astype(np.float32)
    # drop unnecessary columns
    data = data[['Category', 'Name', 'Explanation', 'Url', 
           'Image', 'NameEntry', 'UrlEntry', 'X', 'Y']]
    return data

if __name__ == '__main__':
    # establish engine connection
    engine = create_engine('sqlite:///./data/oukadata.db', echo=False)

    # get xml file of public services from ouka open data
    response = requests.get('https://kartta.ouka.fi/web/siirto/kohteet.xml')

    if response.status_code == 200:
        data = parse_public_services(response)
        #save to sqlite
        data.to_sql('oukaJulkiset', con=engine, index=True, if_exists='replace')
    print(engine.table_names())