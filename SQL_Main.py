print 'Welcome to Himanshu\'s SQL'
print '*************************'
print
print 'SQL v1.0 (default, Jan 11 2016, 13:15:18) [windows (Intel)]'
print 'Type "copyright" or "credits" for more information.'
print
print

import sqlite3 as sql

def main():
    conn = sql.connect('example.db')
    c = conn.cursor()
    cmd = raw_input('SQL> ')
    if cmd[0:7] == 'credits':
        print 
        print '''All credits go to Himanshu Sharma, the creator of this SQL software.
Also to mention python library SQLAlchemy and python itself.'''
        print 

    elif cmd[0:9] == 'copyright':
        print 
        print '''The SQL software by Himanshu Sharma is copyrighted.
Himanshu's Software Foundation;
copyright (c) 2016;
All Rights Reserved.'''
        print 
    else:
        
        try:
            print 
            CMD = cmd.rstrip(';')
            c.execute(CMD)
            print c.fetchall()
            print 

        except:
            print
            print 'Error occured! Consider if table exists.'
            print
    conn.commit()
    conn.close()
    main()
main()
