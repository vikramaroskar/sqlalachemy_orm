import sqlalchemy as sa
from sqlalchemy import Table, inspect, Column, Integer, String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, sessionmaker

constr=""


engine = sa.create_engine(
    constr, connect_args={"options": "-csearch_path={}".format("osia")}
)
connection = engine.connect()

metadata = sa.MetaData()
metadata.bind = engine


Session = sessionmaker(bind=engine)
Base = declarative_base()
Base.metadata.reflect(bind=engine)


# inspector = inspect(engine)

# for table_name in inspector.get_table_names():
#    for column in inspector.get_columns(table_name):
#        print("Column: %s" % column['name'])

# table = Table(
#     'histjobs',
#     metadata,
#     autoload_with=engine
# )

# def select_job(jobname:str)  -> sa.engine.Result:
#     query = table.select().where(table.columns.jname == jobname)
#     result = connection.execute(query)
#     return result.fetchone()
#
# print(select_job("jname2"))

# print(Base.metadata.tables)


# Example: Define a reflected model for a 'users' table
# class Newjobs(Base):
#     __tablename__ = "newjobs"  # Optional, if your table name differs

#     id = Column(Integer, primary_key=True)
#     jname = Column(String)
#     jdesc, Column(String)
#     jfilepath, Column(String)
#     jfilesize, Column(String)
#     jfilename, Column(String)
#     jparams, Column(String)
#     jcreated, Column(String)
#     jpriority, Column(String)
#     jstatus, Column(String)
#     jmuploadinterval, Column(String)
#     jmipaddress, Column(String)
#     juser, Column(String)


class Newjobs(Base):
    __table__ = Table("newjobs", Base.metadata, autoload_with=engine)
    
    def __repr__(self) -> str:
        return f"Newjob is {self.jname}"
    
    def __getitem__(self, field):
        return self.__dict__[field]


# class Histjobs(Base):
#     __tablename__ = "histjobs"
#     id = Column(Integer, primary_key=True)
#     jname = Column(String)
#     jdesc= Column(String)
#     jfilepath= Column(String)
#     jfilesize= Column(String)
#     jfilename= Column(String)
#     jparams= Column(String)
#     jcreated= Column(String)
#     jpriority= Column(String)
#     jstatus= Column(String)
#     jmuploadinterval= Column(String)
#     jmipaddress= Column(String)
#     juser= Column(String)
#     jinfo1= Column(String)
#     jinfo2= Column(String)
#     jrunplace= Column(String)
#     jrunstart= Column(String)
#     jrunend= Column(String)
#     joutputfile= Column(String)
#     joutputfilelink= Column(String)


class Histjobs(Base):
    __table__ = Table("histjobs", Base.metadata, autoload_with=engine)
    
    def __getitem__(self, field):
        return self.__dict__[field]

    # def __repr__(self) -> str:
    #     return f"Histjob is {self.jname}"


sess = Session()
# print("------------------------------------------")
# print(sess.query(Newjobs).all())
# print("------------------------------------------")
# print(sess.query(Histjobs).all())
print("------------------------------------------")
result = sess.query(Newjobs).all()
for row in result:
    print ("Row type is ")
    print(type(row.__dict__))
    print(vars(row))
    print(row.jdesc)
    print(row['jdesc'])
    #print(row["jdesc"])