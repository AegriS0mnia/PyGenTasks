text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}

for letter in text:
    result.setdefault(letter, text.count(letter))