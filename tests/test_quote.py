from bbquote.lib import get_quote

def test_get_quote_is_list():
    quote = get_quote()
    assert isinstance(quote, dict)
