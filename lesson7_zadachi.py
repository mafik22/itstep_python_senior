# class FilterIterator:
#     def __init__(self, data, condition_func):
#         self.data = data
#         self.condition_func = condition_func
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.index < len(self.data):
#             item = self.data[self.index]
#             self.index += 1
#             if self.condition_func(item):
#                 return item
#         raise StopIteration
#
# def starts_with_letter(letter):
#     return lambda x: x.startswith(letter)
#
#
# words_list = ['apple', 'banana', 'avocado', 'orange', 'grape']
#
# starts_with_a_filter = FilterIterator(words_list, starts_with_letter('a'))
# for item in starts_with_a_filter:
#     print(item)
#
# import random
#
# def generate_sentence(subjects, verbs, objects, adjectives, adverbs,  sentence_count=5):
#     for _ in range(sentence_count):
#         subject = random.choice(subjects)
#         verb = random.choice(verbs)
#         obj = random.choice(objects)
#         adjective = random.choice(adjectives)
#         adverb = random.choice(adverbs)
#
#
#         sentence_structure = random.randint(1, 3)
#         if sentence_structure == 1:
#             sentence = f"{subject} ({subject}) {verb} ({verb}) {obj} ({obj})."
#         elif sentence_structure == 2:
#             sentence = f"{subject} ({subject}) {verb} ({verb}) {adjective} ({adjective}) {obj} ({obj})."
#         else:
#             sentence = f"{subject} ({subject}) {adverb} ({adverb}), {verb} ({verb}) {obj} ({obj})."
#         yield sentence
#
#
#
# subjects = ["Я", "Ти", "Він", "Вона", "Вони"]
# verbs = ["біжу", "пригаю", "їм", "сплю", "танцюю"]
# objects = ["яблуко", "кіт", "книга", "м'яч", "дерево"]
# adjectives = ["великий", "малий", "червоний", "синій", "зелений"]
# adverbs = ["швидко", "повільно", "щасливо", "сумно", "голосно"]
#
#
# for sentence in generate_sentence(subjects, verbs, objects, adjectives, adverbs,  sentence_count=5):
#     print(sentence)
# def create_counter():
#     count = 0
#
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#
#     return counter
#
# counter = create_counter()
#
# print(counter())
# print(counter())
# print(counter())
# def handle_exceptions(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as e:
#             print(f"Помилка: {e}")
#     return wrapper
#
#
# @handle_exceptions
# def divide(x, y):
#     return x / y
#
# divide(10, 2)
#
# divide(10, 0)



