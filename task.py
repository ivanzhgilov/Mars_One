from data.user import User
from data.jobs import Jobs
from data.db_session import create_session, global_init

db_name = input()
global_init(db_name)
db_sess = create_session()
result = db_sess.query(User).filter(User.age < 21, User.address == "module_1")
for el in result:
    el.address = "module_3"
db_sess.commit()
