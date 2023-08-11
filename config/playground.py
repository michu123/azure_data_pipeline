from config.db.sql_funcs import connect_db
from config.db.sql_creds import server_name, database, login, password

cnxn = connect_db(server_name, database, login, password)
crsr = cnxn.execute(
    'SELECT res_streamline_id from edw_in."t$raw$res_streamline" limit 1')
row = crsr.fetchone()
print(row)
crsr.close()
cnxn.close()
