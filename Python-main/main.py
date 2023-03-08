from typing import Union 
from fastapi import FastAPI 
from orcl import RDB_client

app = FastAPI()
db = RDB_client('test', 'test', '127.0.0.1', 1521, 'ORCL')

@app.get("/{table}")
def read_orcl(table: str): 
    sql = f'SELECT * FROM {table}'

    db.execute_sql(sql)
    fields = db.get_field_names()
    datas = db.get_datas()

    if not datas:
        return 'no data'
    items = [{field:value for field, value in zip(fields, data)} for data in datas]
    return items