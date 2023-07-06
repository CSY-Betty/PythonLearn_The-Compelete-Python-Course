friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
start_with_r = filter(lambda friend: friend.startswith('R'), friends)  # arg 1: function that returns True/False

print(next(start_with_r))
print(list(start_with_r))

