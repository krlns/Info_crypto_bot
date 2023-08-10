from database.utils.CRUD import CRUDInteface
import os
from site_API.core import headers, querystring_tickers, site_api, url
from database.common.models import database, History
import json

crud = CRUDInteface()


async def fill_db() -> None:
    if not os.path.isfile(os.path.abspath("rating_coins.db")):
        database.connect()
        database.create_tables([History])
        querystring_tickers['limit'] = "100"
        response = site_api.get_data_tickers()
        response = response(url, headers, querystring_tickers, "tickers").text
        data = json.loads(response)

        write = crud.create()
        data_source = [{"name_coin": data['data'][el]['symbol'], "numbers_of_cliks": 0} for el in range(len(data['data']))]
        write(database, History, data_source)

        querystring_tickers['limit'] = "15"


if __name__ == "main":
    crud()
