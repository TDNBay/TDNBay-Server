import mysql.connector


def connect():
    conn = mysql.connector.connect(user='tdnbay', password='tdnbay', database='tdnbay')
    cursor = conn.cursor()
    return conn, cursor


def file_name_by_id(id):
    conn, cursor = connect()
    query = "select filename from mediafile where id = %s"
    cursor.execute(query, (id,))
    file_name = cursor.fetchone()
    conn.disconnect()
    return file_name[0]


def files_list():
    conn, cursor = connect()
    query = "select * from mediafile"
    cursor.execute(query)
    filelist = []
    for file in cursor:
        obj = {'id': file[0], 'name': file[1], 'title': file[2], 'views': file[3]}
        filelist.append(obj)
    conn.disconnect()
    return filelist


