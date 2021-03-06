# [IOTAPAY](https://iotapay.dev/)

<img src="https://i.imgur.com/XVMqjeA.png" width="200">

[![PyPI](https://img.shields.io/pypi/v/iotapay.svg)](https://pypi.org/project/iotapay/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/iotapay.svg)](https://www.python.org/downloads/) 
[![PyPI - Downloads](https://img.shields.io/pypi/dm/iotapay.svg)](https://pypi.org/project/iotapay/)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/acycliclabs/iotapay-py)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/acycliclabs/iotapay-py)

[![Join Discord](https://img.shields.io/discord/417944032111493152?logo=discord&label=join%20discord")](https://discord.gg/vg92AZn)
[![Follow on Twitter](https://img.shields.io/twitter/follow/acycliclabs?style=social&logo=twitter)](https://twitter.com/intent/follow?screen_name=acycliclabs)

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
