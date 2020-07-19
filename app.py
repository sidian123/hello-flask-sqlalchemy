from database import db_session, init_db
from flask import Flask

from models import User

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """当程序结束, 或一次请求结束后, 删除会话"""
    db_session.remove()


# 初始化数据库
init_db()

# 添加用户
db_session.add(User('bb','cc'))
db_session.commit()

# 查询用户
users=User.query.all()
for user in users:
    print(user)