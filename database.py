from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 连接数据库, 获取session
engine = create_engine('mysql+mysqldb://root:123456@localhost/test',echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
# 获取定义实体所需的Base基类
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # 引入定义了实体的模块, 引入的同时该模块将被执行一次, sqlalchemy将获取到元数据
    import models
    # 根据获取到的元数据, 创建表. 注意, 表已存在时, 不会重复创建
    Base.metadata.create_all(bind=engine)
