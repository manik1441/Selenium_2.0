from pages.api.Sample import Sample


def test_users():
    s = Sample()
    res = s.get_users()
    assert res[0] == 200