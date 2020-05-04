# Prisma Access Skillets

A suite of deployment, configuration, and service information skillets for Prisma Access 
Service Setup, Mobile Users, and Remote Networks including:

    * Panorama instantiation in Azure
    * Panorama licensing, content updates, sw updates, and basic configuration
    * Prisma Access service setup, mobile user, and remote network configuration/onboarding
    * Prisma Access API queries to view service information
    
The skillets are grouped into functional Collections:

    * Prisma Access Setup Panorama: initial deployment and setup
    * Prisma Access Service Setup: initial Prisma Access setup configuration
    * Prisma Access Mobile Users: mobile user configuration elements
    * Prisma Access Remote Network: remote network configuration elements
    * Prisma Access Assess Tools: utilities for post-configuration information

## Prerequisites

### License Activation and Customer Support Portal SuperUser Access

This is used to ensure Panorama can be dynamically licensed in Step 3. Also required is superuser access
to generate the One Time Password (OTP) to authorize Panorama connectivity to the cloud instance.

See [How to Activate Cortex Data Lake and Prisma Access for Evals](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClNg)
if additional information needed for license activation.

### Accept the EULA for Panorama in Azure or AWS
In the Azure Portal, open Azure Cloud Shell and run the following command (**BASH ONLY!**):
```
# Accept VM-Series EULA for desired currently-available version of Panorama (see above command for urn)
$ az vm image terms accept --urn paloaltonetworks:panorama:byol:8.1.2

```

For AWS, visit this link to accept the EULA: https://aws.amazon.com/marketplace/pp?sku=eclz7j04vu9lf8ont8ta3n17o 


### Ensure you have the latest Panhandler

For GUI driven deployments using docker containers, ensure you have the latest Panhandler installed on your machine.
The only requirement for Panhandler is Docker.

```bash

$ curl -s -k -L http://bit.ly/2xui5gM | bash

```

You can reference the 
[panHandler Quick Start Guide](https://live.paloaltonetworks.com/t5/Skillet-Tools/Install-and-Get-Started-With-Panhandler/ta-p/307916)
for more information about using panHandler to import and run skillets.


## Deployment

#### Step 1 - Deploy Panorama

First, Choose which public cloud you will use for Panorama Deployment. Currently suppored options are:
* Azure
* AWS

Second, the skillet uses a set of Terraform templates to deploy a new Panorama instance.

> Ensure the region selected supports the required image type


#### Step 2 - Initial Panorama Setup

Initial Panorama staging is done using Ansible playbooks. Includes:

    * DNS and NTP configuration
    * Licensing
    * Content and Software Updates
    * Prisma Access Plug-in installation
    
#### Step 2.1 - Verify the Cloud Plugin using the One Time Password (OTP)

Before configuring Panorama, you must generate the OTP in the Customer Support Portal and add to Panorama

    * Access the Customer Support Portal (Must be a SuperUser) and generate the OTP
    * Go to Panorama > Cloud Services > Configuration and Click ```Verify```
    * Paste in the OTP and Submit


## Serivce Setup Configuration

#### Step 1 - Initial Prisma Access Configuration

Add the service infrastructure subnet and BGP AS.


## Mobile User Configuration

#### Step 1 - Generate Config File and Import to Panorama

> Prior to this step enter the Prisma Access OTP using the Panorama Web UI

This skillet will capture configuration web form data and then generate a full xml config file that is then imported
to Panorama. This file will be referenced in Steps 5 and 6 using ```load config partial``` to merge configuration elements
into the candidate configuration.

The default filename for import is ```prisma_access_full_config.xml```

> If API access is not available, use the Manual skillet option to generate a configuration file to import to Panorama

#### Step 2 - Initial Load Config Partial for Service Setup

After the file is imported, this skillet will configure service setup and add the mobile user template

> At the completion of Step 2 a Panorama commit is required before proceeding to step 6
    
#### Step 3 - Generate Certificates and Complete Mobile User Configuration

> COMMIT to Panorama before running step 3

This skillet will run through a series of load config partial commands and a certificate
generation to:

    * Configure Mobile User Setup and Onboarding
    * Generate certificates used as part of onboarding configuration
    
> At the completion of Step 3 commit to Panorama and push the configuration to Prisma Access

GUI instructions to commit the changes and push to Prisma Access are found in the 
[Admin Guide](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/administer-prisma-access/commit-push-and-revert-prisma-access-configuration-changes.html)

#### Optional non-API Config File Generation

If API access to Panorama is not available, the following steps can be used as an alternative to steps 1, 2, and 3.


1. Run the Optional Manual skillet to generate a config file
2. Copy the xml file output to a file with name ```prisma_access_full_config.xml```
3. Import the file to Panorama (Panorama > Setup > Operations)
4. Use the CLI and follow the [manual steps for load config partial](https://github.com/PaloAltoNetworks/prisma-access-skillets/blob/master/stage_2_configuration/full_config/README.md)

## Remote Network Configuration

Initial Remote Network configuration and per-site onboarding.

#### Step 1 - Initial Configuration

Setup the device-group, template, template-stack, and zone configuration.

#### Step 2 - Site Onboarding

Configure the IKE/IPSEC crypto profiles, IKE gateway, IPSEC tunnel, and plugin onboarding.

Details for each elements can be found by reviewing the [ Remote Network onboarding skillet](https://url.com)
content.

## Assess

#### Retrieve Service Information

The details for using the API and information returned are found in the
[Admin Guide](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-panorama-admin/prisma-access-overview/retrieve-ip-addresses-for-prisma-access.html)

As an alternative to the curl commands and generating and update the option.txt file, this skillet
creates a simple web interface to input the API key and capture user selections for the arguments and choices.

The output of the API is shown on screen.


## Support Policy

The code and templates in the repo are released under an as-is, best effort,
support policy. These scripts should be seen as community supported and
Palo Alto Networks will contribute our expertise as and when possible.
We do not provide technical support or help in using or troubleshooting the
components of the project through our normal support options such as
Palo Alto Networks support teams, or ASC (Authorized Support Centers)
partners and backline support options. The underlying product used
(the VM-Series firewall) by the scripts or templates are still supported,
but the support is only for the product functionality and not for help in
deploying or using the template or script itself. Unless explicitly tagged,
all projects or work posted in our GitHub repository
(at https://github.com/PaloAltoNetworks) or sites other than our official
Downloads page on https://support.paloaltonetworks.com are provided under
the best effort policy.

