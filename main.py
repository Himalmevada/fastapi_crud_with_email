from fastapi import FastAPI
from config.db import Base, engine
from routes import project_1, project_2, project_3, email_invite
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(project_1.router, prefix="/project1")
app.include_router(project_2.router, prefix="/project2")
app.include_router(project_3.router, prefix="/project3")
app.include_router(email_invite.router, prefix="/invite")