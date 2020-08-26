from database import cursor, db

def add_log(text, user):
    sql = ("INSERT INTO logs(text, user) VALUES (%s, %s)")
    cursor.execute(sql, (text, user,))
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))
    
def get_logs():
    sql = ("SELECT * FROM logs ORDER BY created DESC")
    cursor.execute(sql)
    result = cursor.fetchall()
    
    for row in result:
        print(row[1])
        
def get_log(id):
    sql = ("SELECT * FROM logs WHERE id = $s")
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    
    for row in result:
        print(row)
        
def update_log(id, text):
    sql = ("UPDATE logs SET text = %s WHERE id = %s")
    cursor.execute(sql, (text, id))
    db.commit()
    print("Updated log {}".format(id))
        
def delete_log(id):
    sql = ("DELETE FROM logs WHERE id = %s")
    cursor.execute(sql, (id,))
    db.commit()
    print("Log {} deleted".format(id))
        
        
# Logs added to table        
add_log('This is log one', 'Nathan')
add_log('This is log two', 'Meagan')
add_log('This is log three', 'Jack')

# Get all current logs
get_logs()

# Get this specific log
get_log(2)

# Update this specific log
update_log(2, 'Updated log')

# Show update
get_logs()

# Delete this specific log
delete_log(2)

# Show current logs
get_logs()