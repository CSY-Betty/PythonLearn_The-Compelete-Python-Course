friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
start_with_r = filter(lambda friend: friend.startswith('R'), friends)

another_starts_with_r = (f for f in friends if f.startswith('R'))  # list comprehension

friends_lower = map(lambda x: x.lower(), friends)  # map() very popular in other programmimg lauguages
friends_lower = [friends_lower() for friend in friends]  # list comprehension
friends_lower = (friends_lower() for friend in friends)  # generator comprehension

print(next(friends_lower))

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


user = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'tecladoisawesome', 'password': 'youaretoo'}
]

users = [User.from_dict(user) for  user in users]
users - map(User.from_dict, users)