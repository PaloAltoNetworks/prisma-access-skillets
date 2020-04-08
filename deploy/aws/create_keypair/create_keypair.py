#!/usr/bin/env python3
############################################################################################
# Copyright 2020 Palo Alto Networks.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
############################################################################################

# Quick tool to check if a key pair exists, creating it if needed, then returning the public key
# via a JSON str
#
# nembery - 04-07-2020 During C-19
#

from paramiko import RSAKey
import json
import os


def get_public_key(private_key_path: str, public_key: str) -> str:
    """
    Check if a public key exists at the supplied path and create it if needed. Returns the contents of the public
    key

    :param private_key_path: full path to the existing key or where the key will be created
    :param public_key: full path to the existing public key file
    :return: contents of the public key
    """
    if os.path.exists(private_key_path) and os.path.exists(public_key):
        with open(public_key, 'r') as pk:
            pk_contents = pk.read()

    else:
        pk_contents = create_keypair(private_key_path)

    if not pk_contents.startswith('ssh-rsa'):
        raise Exception('This does not look like an SSH key')

    return pk_contents


def create_keypair(private_key_path: str) -> str:
    """
    Create the key-pair using the supplied filename

    :param private_key_path: full path to the key pair to generate
    :return: string contents of the public key
    """

    private_key = RSAKey.generate(bits=2048)
    private_key.write_private_key_file(private_key_path, password=None)

    pub = RSAKey(filename='/tmp/pk', password=None)

    public_key_contents = f'{pub.get_name()} {pub.get_base64()} panhandler'
    with open("%s.pub" % private_key_path, "w") as f:
        f.write(public_key_contents)

    return public_key_contents


def main():
    filename = os.environ.get('private_key_path', '/tmp/deploy_key')
    pub_filename = f'{filename}.pub'

    public_key = get_public_key(filename, pub_filename)

    status = dict()
    status['public_key'] = public_key

    return json.dumps(status)


if __name__ == '__main__':
    output = main()
    print(output)






