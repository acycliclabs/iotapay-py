# Importing package
from iotapay import Iotapay

# Generate a random seed
seed = ''

provider_url = 'https://potato.iotasalad.org:14265'

# Initialising class
iotapay = Iotapay(provider_url, seed)
# iotapay = Iotapay(seed, address)

# Calling Pay function
pay_request_data = {
        'json_data': {
            'version': '0.1',
        },
        'tag': 'ACYCLICIOTAPAYLIOTA99999999',
        'to_address': '',
        'amount': 9
    }

# paid_result = iotapay.pay(pay_request_data)
# print('paid_result:', paid_result)

# Get Balance API
# Case 1: Get balance for particular address.
# get_balance_data = { 'address': '' }

# Case 2: Get balance for n (currently 50) addresses connected to the seed.
get_balance_data = {}

# balance_result = iotapay.get_balance({})
# print('balance_result:', balance_result)
