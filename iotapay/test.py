# Importing package
from iotapay import Iotapay

# Generate a random seed
seed = 'KGWH9PTURNDTSHSQVNLOSFMSTQLHRTTQGDTFJHEKRNPVDRQGHQENANLSXXCXGICCVWBQHMHWPYZSHJYTC'

# Initialising class
iotapay = Iotapay('https://potato.iotasalad.org:14265', seed)
# iotapay = Iotapay(seed, address)

# Calling Pay function
data = {
        'json_data': {
            'version': '0.1',
        'tag': 'ACYCLICIOTAPAYLIOTA99999999'
        },
        'to_address': 'JRNRWSOMSVMCGXOWBAZZNM9IJZFFQKQUMWFPWMVAICNFLAVMJYIPLOQOGPCHLQX9EJFIAIUQXJIMKDVPWGDTXMDKT9',
        # SEED: 'JVKFSJXZOUWXZESUWANGHK9WPNESHWDTWL9QUXYQCYIFZHMWLJKPPBXPPFZLLXMDEHNMHF9KVXUGWURGG',
        'amount': 2
    }

paid_result = iotapay.pay(data)
print('paid_result:', paid_result)
