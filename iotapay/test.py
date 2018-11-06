# Importing package
from iotapay import Iotapay

# Generate a random seed
seed = 'KGWH9PTURNDTSHSQVNLOSFMSTQLHRTTQGDTFJHEKRNPVDRQGHQENANLSXXCXGICCVWBQHMHWPYZSHJYTC'

provider_url = 'https://potato.iotasalad.org:14265'

# Initialising class
iotapay = Iotapay(provider_url, seed)
# iotapay = Iotapay(seed, address)

# Calling Pay function
# pay_request_data = {
#         'json_data': {
#             'version': '0.1',
#         'tag': 'ACYCLICIOTAPAYLIOTA99999999'
#         },
#         'to_address': 'JRNRWSOMSVMCGXOWBAZZNM9IJZFFQKQUMWFPWMVAICNFLAVMJYIPLOQOGPCHLQX9EJFIAIUQXJIMKDVPWGDTXMDKT9',
#         # SEED: 'JVKFSJXZOUWXZESUWANGHK9WPNESHWDTWL9QUXYQCYIFZHMWLJKPPBXPPFZLLXMDEHNMHF9KVXUGWURGG',
#         'amount': 2
#     }
#
# paid_result = iotapay.pay(pay_request_data)
# print('paid_result:', paid_result)

# Get Balance API
get_balance_data = {
        'address': 'JRNRWSOMSVMCGXOWBAZZNM9IJZFFQKQUMWFPWMVAICNFLAVMJYIPLOQOGPCHLQX9EJFIAIUQXJIMKDVPWGDTXMDKT9'
    }

balance_result = iotapay.get_balance(get_balance_data)
print('balance_result:', balance_result)
