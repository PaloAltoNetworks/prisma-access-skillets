import io
import json
import sys

from azure.cli.core import get_default_cli

output = io.StringIO()

sys.sterr = sys.stdout

get_default_cli().invoke(['login', "--use-device-code"], out_file=sys.stdout)
get_default_cli().invoke(['account', "list"], out_file=output)

accounts_str = output.getvalue()
try:
    accounts_json = json.loads(accounts_str)

    account_list = list()
    for account in accounts_json:
        out_dict = dict()
        out_dict['key'] = account.get('name', 'Unknown Name')
        out_dict['value'] = account.get('id', 'Unknown Id')
        account_list.append(out_dict)

    account_lst_encoded = json.dumps(account_list)
    print(f'###{account_lst_encoded}###')

except ValueError:
    print('Could not get list of accounts in Azure')
    sys.exit(1)

