from SQLAlchemy.engine import Base

class AstroUsers(Base):
    __tablename__ = 'astrobot_users'
    __table_args__ = {'autoload': True}


class AudioUsers(Base):
    __tablename__ = 'audiobot_users'
    __table_args__ = {'autoload': True}


class BagriyUsers(Base):
    __tablename__ = 'bagriy_bot_users'
    __table_args__ = {'autoload': True}


class MeditationUsers(Base):
    __tablename__ = 'meditation_users'
    __table_args__ = {'autoload': True}


class NewMakbotUsers(Base):
    __tablename__ = 'new_makbot_users'
    __table_args__ = {'autoload': True}


class SNebaUsers(Base):
    __tablename__ = 'users'
    __table_args__ = {'autoload': True}


class YasnaUsers(Base):
    __tablename__ = 'yasnamak_users'
    __table_args__ = {'autoload': True}