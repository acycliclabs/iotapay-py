# IOTAPAY

![PyPI](https://img.shields.io/pypi/v/iotapay.svg) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/iotapay.svg) 

Python library to Pay using IOTA

# Setup

Install the library `pip install iotapay`

Import package: `from iotapay.iotapay import Iotapay`

Initialize: `Iotapay('https://url:14265', 'TWQH9ETUWNDTRHSQVNLOSFMSTQLHRTZQGDTFUHEKRNPVDRQGHQEARNLSXXCXGICCVWBQHOHWPYZSHJYTC')`

## Basic functions

### Get Balance.
`pay = Iotapay('https://url:14265', 'YOUR SEED')`

Retrieve balance: `pay.get_balance({})`


### Pay

```
data = {
        'json_data': {
            'version': '0.0.9',
        },
        'tag': 'ACYCLICIOTAPAYLIOTA99999999',
        'to_address': 'ADDRESS',
        'amount': 10
    }
```

Pay : `pay.pay(data)`


#### More Functions coming soon.

NOTE: Please, use proper iota node url, ADDRESS and your SEED to initialise. These are simple dummy values. NOT meant for production usage.
