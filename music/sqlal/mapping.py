
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Album(Base):

    __tablename__ = 'albums'
    id = Column(Integer, primary_key=True, autoincrement=True)
    artist = Column(String)
    album_title = Column(String)
    genre = Column(String)
    album_logo = Column(String)


class Song(Base):

    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    album = Column(Integer, ForeignKey(Album.id), primary_key=True)
    file_type = Column(String)
    song_title = Column(String)
    is_favorite = Column(Boolean, default=False)

