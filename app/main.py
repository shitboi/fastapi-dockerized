from fastapi import FastAPI, Path
from pydantic import BaseModel
import pandas as pd
import itertools


app = FastAPI()


@app.get("/")
def root():
    return {'Hello World': 'Welcome to our devops learning'}


@app.get('/all_servers')
def get_servers():
    data = pd.read_excel('servers.xlsx').to_dict()
    r = [[str(s) for s in list(k.values())] for k in list(data.values())]        
    cols = ['id', 'ipAddress', 'country', 'region', 'opscodeBranch', 'description', 
            'provider', 'puppetLastRun', 'decrpyptkey', 'status']
    
    g = [(a,b,c,d,e,f,g,h,i,j) for a,b,c,d,e,f,g,h,i,j 
         in zip(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9])]
    
    records = [{cols[0]: r[0],cols[1]: r[1],cols[2]: r[2],cols[3]: r[3],cols[4]: r[4],
        cols[5]: r[5],cols[6]: r[6],cols[7]: r[7],cols[8]: r[8],cols[9]: r[9]}
         for r in g]
    return records

@app.get('/server')
def get_server(server_ip):
    x = pd.read_excel('servers.xlsx')
    x = x[x['ipAddress']==server_ip].to_dict()
    return {i: str(list(x[i].values())[0]) for i in list(x.keys())}

# get_servers()
