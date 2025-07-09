import psycopg2
from urllib.parse import urlparse

constr=""
p= urlparse(constr)


conn = psycopg2.connect(constr)
cur = conn.cursor()
print (conn)
print (cur)

# cur.execute("""create table if not exists pserson(
#     id int primary key,
#     name varchar(10)
# )
# """)


cur.execute("""
            insert into osia.histjobs (
jname,
jdesc,
jfilepath,
jfilesize,
jfilename,
jparams,
jcreated,
jpriority,
jstatus,
jmuploadinterval,
jmipaddress,
juser,
jinfo1,
jinfo2,
jrunplace,
jrunstart,
jrunend,
joutputfile,
joutputfilelink
)

values ('jname2','jdes2',
'jn1','jd1',
'jn1','jd1',
now(),'jn1'
'jn1','jd1',
'jn1','jd1',
'jn1','jd1',
'jn1','ddfd',now(),
now(),'jd1',
'jd1')

            """)
conn.commit()


cur.execute("""
            select * from histjobs where jname='jname2'
            """)

print(cur.fetchone())

# for row in cur.fetchall():
#     print (row)
    
    
    
sql = cur.mogrify("""
                  select * from histjobs where jname='jname2'
                  """, (1))

print(sql)

print(cur.execute(sql))



cur.close()
conn.close()

