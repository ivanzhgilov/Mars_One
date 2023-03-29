from data.user import User
from data.jobs import Jobs
from data.db_session import create_session, global_init

db_name = input()
global_init(db_name)
db_sess = create_session()
department = db_sess.query(Department).filter(Department.id == 1)[0]
members = [int(i) for i in department.members.split(", ")]
for index in members:
    user = db_sess.query(User).filter(User.id == index).first()
    counter = 0
    jobs = db_sess.query(Jobs).filter(Jobs.collaborators.like(f"%{index}%"))
    for job in jobs:
        counter += job.work_size
    if counter > 25:
        print(user.surname, user.name)
