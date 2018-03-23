#!/usr/bin/env python

"""
Class Records object for class assignment
"""

import requests
import pandas as pd


class Records:

    """
    Class object for retreaving biodiversity data from GBIF
    """

    def __init__(self, q=None, interval=None):
        self.q = q
        self.interval = interval
        self.params = {
            "q": q, 
            "year": str(self.interval)[1:-1], 
            "basisOfRecord": "PRESERVED_SPECIMEN",
            "hasCoordinate": "true",
            "hasGeospatialIssue": "false",
            "country": "US",
            "offset": "0",
            "limit": "300"
        }   
        
        self.df = self._get_all_records()

    def _get_all_records(self):
        "iterate until end of records"
        data = []  # empty list all the results will be add.
              
        while 1:  # 1 equal true, keep running until it breaks
            # make request and store results
            res = requests.get(
                url="http://api.gbif.org/v1/occurrence/search?", 
                params=self.params
            )                                                                                               
            # increment counter
            self.params["offset"] = str(int(self.params["offset"]) + 300)  
            # offset is starting point. limit is last numebr
        
            # concatenate data 
            idata = res.json()  # format results as jSON and store in idata 
            data += idata["results"]  # pull results and add it to data
        
            # stop when end of record is reached 
            if idata["endOfRecords"]:
                break
           
        return pd.DataFrame(data)



