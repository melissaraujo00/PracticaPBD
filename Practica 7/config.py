import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=U20210444\\U20210444;"       # Cambia por tu servidor (ej: DESKTOP\SQLEXPRESS)
        "DATABASE=TiendaSimple;"
        "Trusted_Connection=yes;"
    )
    return conn
