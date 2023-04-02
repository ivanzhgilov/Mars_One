import datetime
from data.jobs import Jobs
from data.user import User
from data import db_session

db_session.global_init('db/blogs.sqlite')
db_sess = db_session.create_session()
job = Jobs()
job.team_leader = 1
job.job = "deployment of residential modules 1 and 2"
job.work_size = 15
job.collaborators = "2, 3"
job.start_date = datetime.datetime.now()
job.is_finished = False
db_sess.add(job)
db_sess.commit()
db_session.global_init('db/blogs.sqlite')
db_sess = db_session.create_session()
user_1 = User()
user_1.email = "scott_chief@mars.org"
user_1.name = "Ridley"
user_1.surname = "Scott"
user_1.age = 21
user_1.position = "captain"
user_1.speciality = "research engineer"
user_1.address = "module_1"
db_sess.add(user_1)
user_2 = User()
user_2.email = "John_Wick@mars.org"
user_2.name = "John"
user_2.surname = "Wick"
user_2.age = 24
user_2.position = "assistant captain"
user_2.speciality = "chef"
user_2.address = "module_1"
db_sess.add(user_2)
user_3 = User()
user_3.email = "Harry_Potter@mars.org"
user_3.name = "Harry"
user_3.surname = "Potter"
user_3.age = 23
user_3.position = "pilot"
user_3.speciality = "botanist"
user_3.address = "module_1"
db_sess.add(user_3)
user_4 = User()
user_4.email = "Harry_Osborn@mars.org"
user_4.name = "Harry"
user_4.surname = "Osborn"
user_4.age = 22
user_4.position = "second pilot"
user_4.speciality = "engineer"
user_4.address = "module_1"
db_sess.add(user_4)
db_sess.commit()
