#!/usr/bin/env python3
# Copyright (c) 2018, Palo Alto Networks
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# Authors: Edward Arcuri, Nathan Embery, Scott Shoaf

import click
from skilletlib import Panos
from skilletlib import SkilletLoader
from skilletlib.exceptions import LoginException
from skilletlib.exceptions import SkilletLoaderException


@click.command()
@click.option("-i", "--TARGET_IP", help="IP address of the device (localhost)", type=str, default="localhost")
@click.option("-r", "--TARGET_PORT", help="Port to communicate to device (443)", type=int, default=443)
@click.option("-u", "--TARGET_USERNAME", help="Firewall Username (admin)", type=str, default="admin")
@click.option("-p", "--TARGET_PASSWORD", help="Firewall Password (admin)", type=str, default="admin")
@click.option("-svc", "--include_svc_setup", help="include service setup configuration", type=str, default="no")
@click.option("-s", "--infra_subnet", help="infrastructure subnet", type=str, default="192.168.254.0/24")
@click.option("-b", "--infra_bgp_as", help="infrastructure BGP AS", type=str, default="65534")
@click.option("-ph", "--portal_hostname", help="portal hostnamne", type=str, default="my-subdomain")
@click.option("-reg", "--deployment_region", help="deployment region", type=str, default="americas")
@click.option("-lam", "--deployment_locations_americas", help="deployment locations americas", type=str,
              default="us-east-1, us-west-1")
@click.option("-leu", "--deployment_locations_europe", help="deployment locations europe", type=str,
              default="eu-west-1")
@click.option("-lap", "--deployment_locations_apac", help="deployment locations apac", type=str,
              default="australia-east")
@click.option("-pool", "--ip_pool_cidr", help="regional ip pool", type=str, default="192.168.2.0/23")
@click.option("-u1", "--user1_password", help="User1 password", type=str, default="Paloalto1")
@click.option("-u2", "--user2_password", help="User2 password", type=str, default="Paloalto2")
@click.option("-f", "--conf_filename", help="Configuration File Name", type=str,
              default="prisma_access_full_config.xml")
def cli(target_ip, target_port, target_username, target_password, include_svc_setup, infra_subnet, infra_bgp_as,
        portal_hostname, deployment_region, deployment_locations_americas, deployment_locations_europe,
        deployment_locations_apac, ip_pool_cidr, user1_password, user2_password, conf_filename):
    """
    Import a full configuration. Defaults values in parenthesis.
    """

    # creating the jinja context from the skillet vars
    context = dict()
    context['include_svc_setup'] = include_svc_setup
    context['infra_subnet'] = infra_subnet
    context['infra_bgp_as'] = infra_bgp_as
    context['portal_hostname'] = portal_hostname
    context['deployment_region'] = deployment_region
    context['deployment_locations_americas'] = deployment_locations_americas.split(',')
    context['deployment_locations_europe'] = deployment_locations_europe.split(',')
    context['deployment_locations_apac'] = deployment_locations_apac.split(',')
    context['ip_pool_cidr'] = ip_pool_cidr
    context['user1_password'] = user1_password
    context['user2_password'] = user2_password
    context['conf_filename'] = conf_filename


    try:
        # render the template config file and create file_contents to use with import_file
        sl = SkilletLoader()
        skillet = sl.load_skillet_from_path('../full_config')
        output = skillet.execute(context)
        file_contents = output.get('template', '')

        # create device object and use panoply import_file to send a config file to the device
        device = Panos(api_username=target_username,
                       api_password=target_password,
                       hostname=target_ip,
                       api_port=target_port
                       )

        if not device.import_file(conf_filename, file_contents, 'configuration'):
            exit(1)

        exit(0)

    except LoginException as lxe:
        print(lxe)
        exit(1)
    except SkilletLoaderException as pe:
        print(pe)
        exit(1)

    # failsafe
    exit(1)


if __name__ == '__main__':
    cli()
