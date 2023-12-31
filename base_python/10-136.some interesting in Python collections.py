"""
collections module
* Counter
* defaultdict
* Ordereddict
* namedtuple
* deque
"""

from collections import Counter

device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]

temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.0])

from collections import defaultdict

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

alma_maters = defaultdict(list)  # list() a function call

for coworker, place in coworkers:
    alma_maters[coworker].append(place)

alma_maters.default_factory = int # None or int or str.....

print(alma_maters['Rolf'])

my_company = 'Teclado'

coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]

coworker_companies = defaultdict(lambda: my_company)

for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies[coworkers[0]])
print(coworker_companies['Rolf'])


from collections import OrderedDict

o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 12
o['Jen'] = 3

print(o)

o.move_to_end('Rolf')
o.move_to_end('Jen', last=False)
print(o)

o.popitem()
print(o)

from collections import namedtuple

account = ('checking', 1850.90)

Account = namedtuple('Account', ['name', 'balance'])

account = Account('checking', 1850.90)
accountNamedTuple = Account._make(account)  # Account(*account)

print(account.name)
print(account)
print(accountNamedTuple._asdict())

from collections import deque

friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
friends.append('Jose')
friends.appendleft('Anthony')
print(friends)

friends.pop()
friends.popleft()
print(friends)