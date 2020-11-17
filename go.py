from deuces_shortdeck import Card, Evaluator, Deck

# create a card
card = Card.new('Qh')

# create a board and hole cards

# create an evaluator
evaluator = Evaluator()

board = [
    Card.new('6h'),
    Card.new('6s'),
    Card.new('Jc'),
    Card.new('Qs'),
    Card.new('Th')
]
# pretty print cards to console
Card.print_pretty_cards(board)
rank = evaluator.evaluate([],board)
print(rank)

board = [
    Card.new('Ah'),
    Card.new('Kh'),
    Card.new('Qh'),
    Card.new('Th'),
    Card.new('Jh')
]
# pretty print cards to console
Card.print_pretty_cards(board)
rank = evaluator.evaluate([],board)
print(rank)

board = [
    Card.new('6c'),
    Card.new('8h'),
    Card.new('Kd'),
    Card.new('Ts'),
    Card.new('Jd')
]
# pretty print cards to console
Card.print_pretty_cards(board)
rank = evaluator.evaluate([],board)
print(rank)
