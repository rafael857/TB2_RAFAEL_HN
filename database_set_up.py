from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL
DATABASE_URL = "sqlite:///perpus_tb2.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session instance
session = Session()

# Create a base class for our models
Base = declarative_base()


# Define the BukuDB model
class BukuDB(Base):
    __tablename__ = 'buku'

    id = Column(Integer, primary_key=True, index=True)
    judul = Column(String, index=True)
    penulis = Column(String, index=True)
    penerbit = Column(String, index=True, nullable=True)
    tahun_terbit = Column(Integer, nullable=True)
    konten = Column(Text)
    iktisar = Column(Text, nullable=True)


# Function to create tables in the database
def create_tables():
    Base.metadata.create_all(engine)


# Function to get a book by ID
def get_buku_by_id(buku_id):
    return session.query(BukuDB).filter(BukuDB.id == buku_id).first()


# Function to post (add) a new book
def post_buku(buku):
    new_buku = BukuDB(
        judul=buku.judul,
        penulis=buku.penulis,
        penerbit=buku.penerbit,
        tahun_terbit=buku.tahun_terbit,
        konten=buku.konten,
        iktisar=buku.iktisar
    )
    session.add(new_buku)
    session.commit()
    return new_buku
