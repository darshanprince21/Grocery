__cnx= None
def get_sql_connection():
    import mysql.connector
    global __cnx
    if __cnx is None:
        
        __cnx = mysql.connector.connect(user='root', password='Darshan@sql21',
                                     host='127.0.0.1',
                                    database='g_store')
        
    return __cnx

