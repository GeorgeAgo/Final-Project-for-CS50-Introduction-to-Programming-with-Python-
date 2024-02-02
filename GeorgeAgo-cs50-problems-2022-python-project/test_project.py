
from project import (
    add_note, update_note, delete_note,
    add_contact, update_contact, delete_contact
)

def test_add_note(monkeypatch):
    inputs = iter(["hello"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    notes, count = add_note([], 0)
    assert notes == [{"ID": 1, "Task": "hello"}] and count == 1


def test_update_note(monkeypatch):
    inputs = iter(["1", "update task"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    notes = update_note([{"ID": 1, "Task": "original task"}])
    assert notes == [{"ID": 1, "Task": "update task"}]


def test_delete_note(monkeypatch):
    inputs = iter(["1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    notes = delete_note([{"ID": 1, "Task": "task to be deleted"}])
    assert notes == []


def test_add_contact(monkeypatch):
    inputs = iter(["Alice", "123-456-7890"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    contacts, count = add_contact({}, 0)
    assert contacts == {"Alice": "123-456-7890"} and count == 1


def test_update_contact(monkeypatch):
    inputs = iter(["Alice", "987-654-3210"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    contacts = update_contact({"Alice": "123-456-7890"})
    assert contacts == {"Alice": "987-654-3210"}


def test_delete_contact(monkeypatch):
    inputs = iter(["Alice"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    contacts = delete_contact({"Alice": "123-456-7890", "Bob": "987-654-3210"})
    assert contacts == {"Bob": "987-654-3210"}
