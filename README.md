<h1>Fastapi</h1>

requirements - Have psql in local machine

### Create database
1) $ psql postgres
2) $ create database fast;
3) $ create user fast_user with password "admin";
4) $ grant all privileges on database fast to fast_user;

### Start
1) $ git clone https://github.com/Kanatik6/fastapi.git
2) $ pip3 install -r requirements
3) $ cd psql_app
4) $ uvicorn main:app --reload
