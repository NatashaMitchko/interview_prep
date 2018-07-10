deck = [(None, 'a'), ('a', 'b'), ('b', 'c'), ('d', None)]

def order_cards(deck):
	if len(deck) == 0:
		return
	for i, card in enumerate(deck):
		if card[0] == None:
			deck.pop(i)
			print [card[1]].append(order_cards(deck))

			return [card[1]].append(order_cards(deck))
		else:
			

print order_cards(deck)