import json
import pandas as pd
import requests
from io import StringIO

async def query(query_string, store="L", set_na=False):
    # Define endpoints
    endpoints = {"F": 'https://fedlex.data.admin.ch/sparqlendpoint',
                 "G": 'https://geo.ld.admin.ch/query',
                 "L": 'https://ld.admin.ch/query'}
    
    address = endpoints.get(store, store)

    # Try the POST request
    try:
        resp = requests.post(address,
                             data={"query": query_string},
                             headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                      "Accept": "text/csv"})
        resp.raise_for_status()  # Raise exception for non-200 status codes
    except Exception as e:
        raise RuntimeError(f"Fetch failed: {str(e)}")

    if resp.ok:
        res = resp.text
        if '{"message":' in res:
            error = json.loads(res)
            raise RuntimeError("SPARQL query malformed: " + error["message"])
        elif 'Parse error:' in res:
            raise RuntimeError("SPARQL query malformed: " + res)
        else:
            df = pd.read_csv(StringIO(res), na_filter=set_na)
            return df
    else:
        if resp.status_code == 400:
            raise RuntimeError("Response status 400: Possible malformed SPARQL query. No syntactic advice available.")
        else:
            raise RuntimeError(f"Response status {resp.status_code}")


def display_result(df):
    html_content = df.to_html(render_links=True, escape=False)
    print(html_content)
