#!/usr/bin/python3
#######################################################################################
# @author: Guille Rodriguez https://github.com/guillerg86
# @version: 2025-05-03 20:55 (YYYY-MM-DD)
# @python-version: 3.x
#
# This script allows for controlled retrieval of Netskope Publishers information, 
# helping to avoid HTTP 429 (Too Many Requests) errors that can occur when monitoring
# a large number of publishers via the API. It provides two main actions:
#
# - get-publishers: Retrieves the full list of publishers from the Netskope API and
#                   either saves it to a JSON file or prints it to the console (testing).
#
# - get-publisher: Extracts information for a specific publisher (by ID) from the 
#                  previously saved file, avoiding repeated API calls.
#
# The main goal of the script is to facilitate local monitoring of Netskope Publishers
# through centralized and efficient queries, making it ideal for environments with high
# volumes where reducing API load is critical.
#
#######################################################################################

import requests
import argparse
import json
from urllib.parse import urlparse

def fetch_publishers(base_url,api_key):
    api_endpoint = f"{configure_tenant_url(base_url)}/infrastructure/publishers"
    headers = {"Netskope-Api-Token": api_key}
    response = requests.get(api_endpoint,headers=headers)
    response.raise_for_status()
    respdata = json.loads(response.text)
    publishers_list = respdata.get('data',{}).get('publishers',{})
    return publishers_list

def configure_tenant_url(base_url,version="v2"):
    return f"{base_url}/api/{version.lower()}"

def configure_parser():
    parser = argparse.ArgumentParser(
        prog="Netskope Publisher", 
    )
    parser.add_argument("-a","--action",choices=['get-publishers','get-publisher'],required=True)
    parser.add_argument("-c","--console",action="store_true")
    parser.add_argument("-au","--api-url",required=True)
    parser.add_argument("-ak","--api-key",required=True)
    parser.add_argument("-f","--folder",required=False,default="/tmp")
    parser.add_argument("-pid","--publisher-id",required=False,type=int)
    args = parser.parse_args()
    return args

if __name__ == "__main__":    
    args = configure_parser()
    filename = (urlparse(args.api_url).netloc).replace(".","_")
    
    if args.action == "get-publishers":
        publishers_list = fetch_publishers(args.api_url,args.api_key)
        if args.console:
            print(json.dumps(publishers_list,indent=2))
        else:
            with open(f"{args.folder}/publishers-{filename}.json", 'w') as fp:
                json.dump(publishers_list, fp, indent=2)
            print(1)
    if args.action == "get-publisher":
        if args.publisher_id is None:
            print("Parameter --publisher-id missing or not integer")
            exit(1)
        with open(f"{args.folder}/publishers-{filename}.json", 'r') as fp:
            publishers_list = json.load(fp)
        for publisher in publishers_list:
            if publisher.get('publisher_id') == args.publisher_id:
                print(json.dumps(publisher,indent=2))
                exit(0)
        print(f"Publisher not found in file publishers-{filename}.json")

            
        
        


