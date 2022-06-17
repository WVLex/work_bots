import datetime

from SQLAlchemy.engine import session_scope
from sqlalchemy import select, func
from statisctic_bot.db.models import AstroUsers, YasnaUsers, AudioUsers, \
    BagriyUsers, SNebaUsers, NewMakbotUsers, MeditationUsers


class Users:

    def __init__(self):
        with session_scope() as s:
            self.sneba_users = s.query(func.count(SNebaUsers.tg_id)).scalar()
            self.astro_users = s.query(func.count(AstroUsers.tg_id)).scalar()
            self.yasna_users = s.query(func.count(YasnaUsers.tg_id)).scalar()
            self.audio_users = s.query(func.count(AudioUsers.tg_id)).scalar()
            self.bagriy_users = s.query(func.count(BagriyUsers.tg_id)).scalar()
            self.new_makbot_users = s.query(func.count(NewMakbotUsers.tg_id)).scalar()
            self.meditation_users = s.query(func.count(MeditationUsers.tg_id)).scalar()
