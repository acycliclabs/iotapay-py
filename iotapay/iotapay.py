# iotapay main class
from iota import Address, ProposedTransaction, Tag, Transaction, Iota, TryteString, json
import time, json

class iotapay:
    def __init__(self, provider, seed, address=None):
        self.seed = seed
        self.provider = provider
        self.api = Iota(self.provider, self.seed)

    def pay(self, data):
        try:
            json_data = data['json_data']
            json_string = json.dumps(json_data)
            trytes = TryteString.from_string(json_string)
            # Send Transfer
            sent_transfer = self.api.send_transfer(
                    depth = 3,
                    transfers = [
                            ProposedTransaction(
                                address =  Address(data['to_address']),
                                value = data['amount'],
                                tag = Tag(data['tag']),
                                message = trytes,
                            ),
                        ]
                    )
            bo = sent_transfer['bundle']
            return {
                    'status': 200,
                    'transaction_hash': bo.as_json_compatible()[0]['hash_'],
                    'message': 'Successfully Sent!'
                }
        except Exception as pe:
            # print('pe:', pe)
            return {
                    'status': 400,
                    'error': '',
                    # 'balance': str(pe.context['total_balance']),
                    'message': str(pe).split('(')[0]
                }

    def get_balance(self, data):
        try:
            if 'address' in data:
                balance_result = self.api.get_balances([data['address']])
                balance = balance_result['balances'][0]
            else:
                gna_result = self.api.get_new_addresses(index=0, count=50) # generate 50 addresses.
                addresses = gna_result['addresses']
                balance_result = self.api.get_balances(addresses)
                balance = 0
                for i in range(len(balance_result['balances'])):
                    balance = balance + balance_result['balances'][i]
            return {
                    'status': 200,
                    'balance': balance,
                    'message': 'Successfully Retrieved!'
                }
        except Exception as pe:
            # print('pe:', pe)
            return {
                    'status': 400,
                    'error': '',
                    # 'balance': str(pe.context['total_balance']),
                    # 'message': str(pe).split('(')[0]
                }

    def collect(self, data):
        print('send request to collect payment.')
        return;

    def generate_invoice(self, data):
        print('generate invoice.')
        return;
