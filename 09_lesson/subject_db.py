from sqlalchemy import create_engine, text
from config import DB_URL


class SubjectDB:
    def __init__(self):
        self.engine = create_engine(DB_URL)

    def add(self, subject_id, title):
        with self.engine.connect() as conn:
            conn.execute(
                text(
                    "INSERT INTO subject(subject_id, subject_title) "
                    "VALUES (:id, :title)"
                ),
                {"id": subject_id, "title": title},
            )
            conn.commit()

    def update(self, subject_id, new_title):
        with self.engine.connect() as conn:
            conn.execute(
                text(
                    "UPDATE subject SET subject_title = :title "
                    "WHERE subject_id = :id"
                ),
                {"title": new_title, "id": subject_id},
            )
            conn.commit()

    def delete(self, subject_id):
        with self.engine.connect() as conn:
            conn.execute(
                text("DELETE FROM subject WHERE subject_id = :id"),
                {"id": subject_id},
            )
            conn.commit()

    def get_by_id(self, subject_id):
        with self.engine.connect() as conn:
            result = conn.execute(
                text("SELECT * FROM subject WHERE subject_id = :id"),
                {"id": subject_id},
            )
            return result.mappings().first()
