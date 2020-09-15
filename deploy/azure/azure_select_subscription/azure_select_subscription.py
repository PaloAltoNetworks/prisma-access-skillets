import io
import os
import sys

from azure.cli.core import get_default_cli

azure_account = os.environ.get('azure_account', None)

output = io.StringIO()

sys.sterr = sys.stdout

get_default_cli().invoke(['account', "set", "-s", azure_account], out_file=sys.stdout)
