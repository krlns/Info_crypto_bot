from typing import Dict

import requests


def _make_response(url: str, headers: Dict, params: Dict, success=200):
    response = requests.get(
        url,
        headers=headers,
        params=params,
    )

    status_code = response.status_code

    if status_code == success:
        return response
    return status_code


def _get_data_tickers(url: str, headers: Dict, params: Dict, name_: str, func=_make_response):
    url = "{}/{}/".format(url, name_)
    response = func(url, headers=headers, params=params)
    return response


def _get_data_markets(url: str, headers: Dict, params: Dict,
                      coin: str, markets: str, func=_make_response):
    url = "{}/{}/{}/".format(url, coin, markets)

    response = func(url, headers=headers, params=params)
    return response


def _get_global_data(url: str, headers: Dict, params: Dict, global_: str, func=_make_response):
    url = "{}/{}/".format(url, global_)

    response = func(url, headers=headers, params=params)
    return response


class SiteApiInterface:
    @staticmethod
    def get_data_tickers():
        return _get_data_tickers

    @staticmethod
    def get_data_markets():
        return _get_data_markets

    @staticmethod
    def get_global_data():
        return _get_global_data


if __name__ == "__main__":
    _make_response()
    _get_data_tickers()
    _get_data_markets()

    SiteApiInterface()
