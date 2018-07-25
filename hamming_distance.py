def hamming_distance_1(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int

    weird string manipulation method
    """
    h_distance = 0
    x = '{0:08b}'.format(x)
    y = '{0:08b}'.format(y)
    print x, y
    if len(x) != len(y):
        diff = abs(len(y) - len(x))
        if len(x) < len(y):
            x = x[::-1]
            x += ('0' * diff)
            x = x[::-1]
        else:
            y = y[::-1]
            y += ('0' * diff)
            y = y[::-1]
    for i, j in zip(x, y):
        if i != j:
            h_distance += 1
    return h_distance

def hamming_distance_2(x, y):
	"""
	bitwise or method
	"""
    diff = x ^ y
    s = "{0:08b}".format(diff)
    count = 0
    for c in s:
    	if c =='1':
    		count += 1
    return count

print hamming_distance_2(1,2)

# pytests
# @pytest.mark.parameterize('x, y', [(1,2)])
# def test_hamming_distance_1():
# 	assert hamming_distance_1() ==