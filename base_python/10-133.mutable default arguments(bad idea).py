def create_account(name: str, holder: str, account_holders: list = []):
    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }

a1 =create_account('cheecking', 'Rolf')
a2 =create_account('savings', 'Jen')

print(a2)