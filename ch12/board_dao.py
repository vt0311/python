'''
Created on 2017. 10. 25.

@author: hsw
'''

import cx_Oracle

#class BoardListDAO:
        
def  boardListSelect():
            
        boardVO = []
             
        conn = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/xe')
    
        cursor = conn.cursor()
        
        cursor.execute('select b_no,b_title,b_writer,b_contents,reg_date from board')
        #cursor.execute('select * from board')
        
        for row in cursor:
            boardVO.append(row)
            #print(row)
        
        cursor.close()
        
        conn.close()
    
        return boardVO
   
def  boardListInsert(title, writer, contents ):
            
        #boardVO = []
             
        conn = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/xe')
    
        cursor = conn.cursor()
        
        sql = "insert into board values('{}','{}','{}', sysdate)".format(title, writer, contents)
        #cursor.execute(sql, (title, writer, contents))
        cursor.execute(sql)
        #cursor.execute('select * from board')
        
        conn.commit()
        
        cursor.close()
        
        conn.close()
    
        