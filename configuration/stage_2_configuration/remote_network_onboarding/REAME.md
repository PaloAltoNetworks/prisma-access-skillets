# Onboarding New Sites to Prisma Access

This skillet is used for each new remote site added to Prisma Access.

> All naming is based on the remote network site name

All configuration elements using 'local address' are not part of the skillet.
The service IP is only assigned after the configuration is committed and pushed to Prisma Access.
Local address configuration elements would be added in the GUI after the service IP is known.

### Plugin Onboarding

Plug-in configuration to add a new Remote Network site.
The configuration includes:

    * site name
    * bandwidth based on license allocation
    * region for the remote site connection
    * subnet(s) for the remote site
    * IPSEC tunnel association
    
> the skillet does not validate license allocations and what is available for the new site.


### IKE and IPSEC Crypto Profiles

profile configuration including the following settings:

    * DH group
    * encryption
    * authentication

### IKE Gateway

IKE gateway configuration.

options include:

    * peer type: ip address or dynamic
    * peer ID type (dynamic): ip address or fqdn
    * gateway preshared key
    * option to enable NAT traversal

### IPSEC Tunnel

IPSEC tunnel based on the IKE gateway.

If enabled, proxy-id configuration is included. A unique entry is added for each remote subnet.
Users can delete/edit the configuration details in the GUI.
