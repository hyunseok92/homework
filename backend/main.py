from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, desc
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


app = FastAPI()

origins = [
    "http://localhost:3000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

username = 'test'
password = '1234'
host = 'database'
port = 3306
database = 'test'
DATABASE_URL = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset=utf8mb4'
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Item(BaseModel):
    testok: str
Base = declarative_base()

class Test(Base):
    __tablename__ = "testtable"
    __table_args__ = {'schema': 'test', 'mysql_collate': 'utf8mb4_general_ci'}

    testok = Column(String(100, collation='utf8mb4_general_ci'),primary_key=True)
def init_db():
    Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/add/")
async def add(item: Item, db: SessionLocal = Depends(get_db)):
    print(f"item.testok: {item.testok}")
    db_item = db.query(Test).filter(Test.testok == item.testok).first()
    print("db_item: ", db_item)
    if db_item:
        raise HTTPException(status_code=400, detail="Item already exists")
    new_item = Test(testok=item.testok)
    print("new_item: ", new_item)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.get("/get/")
async def get(db: SessionLocal = Depends(get_db)):
    return  db.query(Test).order_by(desc(Test.testok)).first()