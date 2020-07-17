# def sayHello(name='Sam'):
#     print(f'Hello {name}')
# sayHello('John Doe')
# def getSum(num1, num2):
#     total = num1 + num2
#     return total
# num = getSum(2, 4)
# print(num)
# getSum = lambda num1, num2 : num1 + num2
# print(getSum(10,3))


def multi_word_search(document, keywords):
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(document, keyword)
    return keyword_to_indices
