# Prisma Access Skillet

Coming soon...

Suite of skillets for initial Prisma Access deployment and configuration


## Azure Deployment

This repository also contains a set of Terraform templates and associated Ansible Playbooks to deploy
a fully configured Panorama with Prisma Access Plugin into Azure.


## Pre-reqs
### Accept the EULA for Panorama in Azure
In the Azure Portal, open Azure Cloud Shell and run the following command (**BASH ONLY!**):
```
# Accept VM-Series EULA for desired currently-available version of Panorama (see above command for urn)
$ az vm image terms accept --urn paloaltonetworks:panorama:byol:8.1.2

```

### Ensure you have the latest Panhandler

For GUI driven deployments using docker containers, ensure you have the latest Panhandler installed on your machine.
The only requirement for Panhandler is Docker.

```bash

$ curl -s -k -L http://bit.ly/34kXVEn | bash

```

> This will install the development version of Panhandler. 
