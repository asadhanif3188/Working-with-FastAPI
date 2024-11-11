# Working-with-FastAPI

**Note:** This repo is intended to showcase the expertise of working with Python FastAPI framework. 

## Important Aspects
- Developed API Endpoints using **FastAPI**.
- For persistance **Postgres DB** has been used.
<!-- - DB integration has been done using ORM and Alchamy  -->
- Neon (DB hosted) platform is being used.
    - It is a serverless platform designed to help build reliable and scalable applications faster.
- Pydantic-Settings module is used to manage the Env. file management.
-  

## Tools Chain
- FastAPI
- Database (Postgres)

## Description


## DB Migrations 

For DB migrations `alembic` framework has been used. 

Command to initialize alembic environment.
```
alembic init -t async migrations 
```

After doing changes in different files, run following commnad. 
```
alembic revision --autogenerate -m "init"
```


### Commands to run the code

```
fastapi dev src
```

