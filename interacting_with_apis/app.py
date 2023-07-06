import time
from libs.openexchange import OpenExchangeClient

APP_ID = "4eb0af99644b4211aa2c5c4151bf20eb"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end - start)

usd_amount = 1000
start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end - start)
print(f"USD{usd_amount} is GBP{gbp_amount:.2f}")
