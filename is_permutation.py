def is_permutation(s1, s2):
	if len(s1) != len(s2):
		return False
	cc = {}
	for c in s1:
		if c in cc:
			cc[c] += 1
		else:
			cc[c] = 1
	for c in s2:
		if c not in cc:
			return False
		else:
			cc[c] -= 1
			if cc[c] < 0:
				return False
	i = 0
	for val in cc.values():
		i += val
	return i == 0

print is_permutation("cat", "act") # true
print is_permutation("ccc", "cca") # false
print is_permutation("", "1") # false
print is_permutation("aab", "aaa") # false