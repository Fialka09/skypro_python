from subject_db import SubjectDB

db = SubjectDB()
TEST_ID = 16
TEST_TITLE = "QA"


def test_insert_subject():
    db.add(TEST_ID, TEST_TITLE)
    row = db.get_by_id(TEST_ID)
    assert row is not None
    assert row["subject_title"] == TEST_TITLE
    db.delete(TEST_ID)  # удаляем за собой


def test_update_subject():
    db.add(TEST_ID, TEST_TITLE)  # создаём
    db.update(TEST_ID, "SQL")
    row = db.get_by_id(TEST_ID)
    assert row["subject_title"] == "SQL"
    db.delete(TEST_ID)  # удаляем за собой


def test_delete_subject():
    db.add(TEST_ID, TEST_TITLE)  # создаём
    db.delete(TEST_ID)
    row = db.get_by_id(TEST_ID)
    assert row is None
