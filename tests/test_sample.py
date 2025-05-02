def test_add():
    from main import add
    assert add(2, 3)["result"] == 5
