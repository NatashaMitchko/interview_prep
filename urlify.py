def urlify(s):
	"""
	>>> urlify("a  b  cd  ")
	a%20b%20cd
	"""
	contents = []
	b = 0
	e = 0
	for i in range(len(s)):
		if s[i] == " " and i != 0 and s[i-1] != " ":
			e = i
			contents.append(s[b:e])
		elif i != 0 and i != len(s) - 1 and s[i+1] != " " and s[i-1] == " ":
			b = i + 1
		elif i == len(s) - 1 and s[i] != " ":
			contents.append(s[b:])
	return "%20".join(contents)


print urlify("a  b  c")
print urlify("   b   ")
print urlify(" abc")
print urlify(" ab c ")
print urlify("abc    d")