# iotapay main class
from iota import Address, ProposedTransaction, Tag, Transaction, Iota, TryteString, json
import time, json


# Generate a random seed.
tag = Tag('ACYCLICIOTAPAYLIOTA99999999') # Tag for in the message.

class Iotapay:
    def __init__(self, provider, seed, address=None):
        self.seed = seed
        self.provider = provider
        # self.api = Iota(self.provider)
        self.api = Iota(self.provider, self.seed)

    def pay(self, data):
        try:
            json_data = data['json_data']
            json_string = json.dumps(json_data)
            trytes = TryteString.from_string(json_string)
            print('sending transfer ...')
            # Send Transfer
            sent_transfer = self.api.send_transfer(
                    depth = 3,
                    transfers = [ProposedTransaction(address =  Address(Address(data['to_address'],)),
                      value = data['amount'],
                      tag = tag,
                      message = trytes,),],)
            print('sent_transfer', sent_transfer)
            bo = sent_transfer['bundle']
            print('bundle', bo)
            return {
                    'status': 200,
                    'transaction_hash': bo.as_json_compatible()[0]['hash_'],
                    'message': 'Successfully Sent!'
                }
        except Exception as pe:
            print('pe:', pe)
            return {
                    'status': 400,
                    'error': '',
                    'balance': str(pe.context['total_balance']),
                    'message': str(pe).split('(')[0]
                }

    def get_balance(self, data):
        try:
            if 'address' in data:
                balance_result = self.api.get_balances([data['address']])
                print('balance_result:', balance_result)
                # {'balances': [0], 'milestone': None, 'duration': 1, 'milestoneIndex': 870196, 'references': ['NRZPIXFHBKGDEZCVEBHZQTJFDWKBPZSHZXEMCEOEDQYXOSYQKMXYYTHHUUJAKWX9YWNEIJPS9PFXZ9999']}
                balance = balance_result['balances'][0]
                # print('balance:', balance)
                return {
                        'status': 200,
                        'balance': balance,
                        'message': 'Successfully Retrieved!'
                    }
        except Exception as pe:
            print('pe:', pe)
            return {
                    'status': 400,
                    'error': '',
                    # 'balance': str(pe.context['total_balance']),
                    # 'message': str(pe).split('(')[0]
                }

    def collect(self, data):
        print('send request to collect payment.')
        return;
