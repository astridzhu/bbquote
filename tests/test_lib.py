from bbquote.lib import get_quote

def test_get_quote():
    assert type(get_quote()) == str
