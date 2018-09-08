# Importing package
from iotapay import Iotapay

# Generate a random seed
seed = 'KGWH9PTURNDTSHSQVNLOSFMSTQLHRTTQGDTFJHEKRNPVDRQGHQENANLSXXCXGICCVWBQHMHWPYZSHJYTC'

# Initialising class
iotapay = Iotapay(seed)

# Calling Pay function
iotapay.pay({})
