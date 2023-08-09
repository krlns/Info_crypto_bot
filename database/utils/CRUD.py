from typing import Dict, List, TypeVar
from peewee import ModelSelect
from database.common.models import ModelBase
from ..common.models import database, History


T = TypeVar("T")


def _store_date(db: database, model: T, *data: List[Dict]) -> None:
    with db.atomic():
        model.insert_many(*data).execute()


def _retrieve_all_data(db: database, model: T, *columns: ModelBase) -> ModelSelect:
    with db.atomic():
        response = model.select(*columns).order_by(History.numbers_of_cliks)
    return response


class CRUDInteface():
    @staticmethod
    def create():
        return _store_date

    @staticmethod
    def retrieve():
        return _retrieve_all_data


if __name__ == "__main__":
    _store_date()
    _retrieve_all_data()
    CRUDInteface()
