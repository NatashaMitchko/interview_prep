import pytest

def urlify(s):
	"""
	>>> urlify("a  b  cd  ")
	a%20b%20cd
	"""
	contents = []
	ls = len(s)
	b = 0
	e = 0
	for i in range(ls):
		if i == 0 and s[i] != " ":
			b = 0
		if i == 0 and s[i] == " ":
			b = i + 1
		if i != 0 and s[i] == " " and s[i-1] != " ":
			e = i
			contents.append(s[b:e])
		if i != 0 and s[i] != " " and s[i-1] == " ":
			b = i
		if i == ls - 1 and s[i] != " ":
			contents.append(s[b:])
	return "%20".join(contents)

@pytest.mark.parametrize("s, expected", [("a  b  cd ", "a%20b%20cd"),
							             ("a  b  c", "a%20b%20c"),
							             (" abc", "abc"),
							             (" ab c ", "ab%20c"),
							             ("abc   d", "ab%20d")])
def test_urlify(s, expected):
	assert urlify(s) == expected