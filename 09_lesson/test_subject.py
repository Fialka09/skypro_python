from subject_db import SubjectDB

db = SubjectDB()


def test_insert_subject():
    db.add(16, "QA")
    row = db.get_by_id(16)
    assert row is not None
    assert row["subject_title"] == "QA"


def test_update_subject():
    db.update(16, "SQL")
    row = db.get_by_id(16)
    assert row["subject_title"] == "SQL"


def test_delete_subject():
    db.delete(16)
    row = db.get_by_id(16)
    assert row is None
