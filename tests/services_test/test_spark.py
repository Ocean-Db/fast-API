# go three folders up
from ...app.services import spark_oceandb as sp




spark = sp.create_spark_session()
print('Session Started')
print('Code Executed Successfully')