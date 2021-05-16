import pickle

class Company:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.clts = []

    def newClass(self, new):
      self.clts.append(new)

class test1:
  def __init__(self, a):
    self.a = a

it1 = test1('sdf')
it2 = test1('fasd')

with open('company_data', 'wb') as output:
    company1 = Company('banana', 40)
    company1.newClass(it1)
    pickle.dump(company1, output, pickle.HIGHEST_PROTOCOL)

    company2 = Company('spam', 42)
    company2.newClass(it2)
    pickle.dump(company2, output, pickle.HIGHEST_PROTOCOL)

del company1
del company2

with open('company_data', 'rb') as input:
    company1 = pickle.load(input)
    print(company1.name)  # -> banana
    print(company1.value)  # -> 40
    print(company1.clts[0].a)

    company2 = pickle.load(input)
    print(company2.name) # -> spam
    print(company2.value)  # -> 42
    print(company2.clts[0].a)