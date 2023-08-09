from database.utils.CRUD import CRUDInteface
from database.common.models import database, History

database.connect()
database.create_tables([History])

crud = CRUDInteface()


if __name__ == "main":
    crud()
