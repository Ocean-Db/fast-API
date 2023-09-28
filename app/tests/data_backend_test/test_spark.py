# go three folders up
from ...data_backend import spark_oceandb as sp




spark = sp.create_spark_session()
print('Session Started')
print('Code Executed Successfully')