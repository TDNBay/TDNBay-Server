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
    query = "select * from mediafile order by id DESC"
    cursor.execute(query)
    filelist = []
    for file in cursor:
        obj = {'id': file[0], 'name': file[1], 'title': file[2], 'thumbnail': file[3], 'views': file[4]}
        filelist.append(obj)
    conn.disconnect()
    return filelist


def increase_video_view_count(file_id):
    conn, cursor = connect()
    query = "update mediafile set fileviews = fileviews + 1 where id = %s"
    cursor.execute(query, (file_id,))
    conn.commit()
    conn.disconnect()

def save_file(file_name, file_title):
    conn, cursor = connect()
    query = "insert mediafile (filename, filetitle, filethumb, fileviews) values (%s, %s, %s, %s)"
    cursor.execute(query, (file_name, file_title, file_name + '.png', 0,))
    conn.commit()
    conn.disconnect()