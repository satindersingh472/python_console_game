import mariadb
import dbcreds

def connect_db():
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        return cursor
    except mariadb.DatabaseError as error:
        print('DATABASE ERROR', error)
    except mariadb.Error:
        print('ERROR', error)
    except mariadb.DataError as error:
        print('DATA ERROR', error)
    except mariadb.PoolError as error:
        print('POOL ERROR', error)
    except mariadb.InternalError as error:
        print('INTERNAL ERROR', error)
    except mariadb.IntegrityError as error:
        print('INTEGRITY ERROR', error)
    except mariadb.InterfaceError as error:
        print('INTERFACE ERROR', error)
    except mariadb.OperationalError as error:
        print('OPERATIONAL ERROR', error)
    except mariadb.ProgrammingError as error:
        print('PROGRAMMING ERROR', error)
    except mariadb.NotSupportedError as error:
        print('NOT SUPPORTED ERROR', error)
    except mariadb.Warning as error:
        print('WARNING', error)
    except Exception as error:
        print('UNKNOWN ERROR', error)

def execute_statement(cursor, statement, list=[]):
    try:
        cursor.execute(statement, list)
        result = cursor.fetchall()
        return result
    except mariadb.DatabaseError as error:
        print('DATABASE ERROR', error)
    except mariadb.Error:
        print('ERROR', error)
    except mariadb.DataError as error:
        print('DATA ERROR', error)
    except mariadb.PoolError as error:
        print('POOL ERROR', error)
    except mariadb.InternalError as error:
        print('INTERNAL ERROR', error)
    except mariadb.IntegrityError as error:
        print('INTEGRITY ERROR', error)
    except mariadb.InterfaceError as error:
        print('INTERFACE ERROR', error)
    except mariadb.OperationalError as error:
        print('OPERATIONAL ERROR', error)
    except mariadb.ProgrammingError as error:
        print('PROGRAMMING ERROR', error)
    except mariadb.NotSupportedError as error:
        print('NOT SUPPORTED ERROR', error)
    except mariadb.Warning as error:
        print('WARNING', error)
    except Exception as error:
        print('UNKNOWN ERROR', error)

def close_connection(cursor):
    try:
        conn = cursor.connection()
        cursor.close()
        conn.close()
    except mariadb.DatabaseError as error:
        print('DATABASE ERROR', error)
    except mariadb.Error:
        print('ERROR', error)
    except mariadb.DataError as error:
        print('DATA ERROR', error)
    except mariadb.PoolError as error:
        print('POOL ERROR', error)
    except mariadb.InternalError as error:
        print('INTERNAL ERROR', error)
    except mariadb.IntegrityError as error:
        print('INTEGRITY ERROR', error)
    except mariadb.InterfaceError as error:
        print('INTERFACE ERROR', error)
    except mariadb.OperationalError as error:
        print('OPERATIONAL ERROR', error)
    except mariadb.ProgrammingError as error:
        print('PROGRAMMING ERROR', error)
    except mariadb.NotSupportedError as error:
        print('NOT SUPPORTED ERROR', error)
    except mariadb.Warning as error:
        print('WARNING', error)
    except Exception as error:
        print('UNKNOWN ERROR', error)