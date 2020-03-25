# Prisma Access Skillets

A suite of deployment, configuration, and service information skillets for Prisma Access mobile users including:

    * Panorama instantiation in Azure
    * Panorama licensing, content updates, sw updates, and basic configuration
    * Prisma Access service setup and mobile user configuration
    * Prisma Access API queries to view service information

## Prerequisites

### License Activation and Customer Support Portal SuperUser Access

This is used to ensure Panorama can be dynamically licensed in Step 3. Also required is superuser access
to generate the One Time Password (OTP) to authorize Panorama connectivity to the cloud instance.

See [How to Activate Cortex Data Lake and Prisma Access for Evals](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClNg)
if additional information needed for license activation.

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

You can reference the 
[panHandler Quick Start Guide](https://live.paloaltonetworks.com/t5/Skillet-Tools/Install-and-Get-Started-With-Panhandler/ta-p/307916)
for more information about using panHandler to import and run skillets.

## Step 1 - Azure Login

Used to authorize the container to manage Azure resources.
Creates an identity used by the subsequent skillets to add resources to your Azure account.

## Step 2 - Panorama Deployment in Azure

This skillet uses a set of Terraform templates to deploy a new Panorama instance.

> Ensure the region selected supports the Standard D3 image

## Step 3 - Initial Panorama Configuration

Initial Panorama staging is done using Ansible playbooks. Includes:

    * DNS and NTP configuration
    * Licensing
    * Content and Software Updates
    * Prisma Access Plug-in installation
    
## Step 3.1 - Verify the Cloud Plugin using the One Time Password (OTP)

Before configuring Panorama, you must generate the OTP in the Customer Support Portal and add to Panorama

    * Access the Customer Support Portal (Must be a SuperUser) and generate the OTP
    * Go to Panorama > Cloud Services > Configuration and Click ```Verify```
    * Paste in the OTP and Submit
    
## Step 4 - Generate Config File and Import to Panorama

> Prior to this step enter the Prisma Access OTP using the Panorama Web UI

This skillet will capture configuration web form data and then generate a full xml config file that is then imported
to Panorama. This file will be referenced in Steps 5 and 6 using ```load config partial``` to merge configuration elements
into the candidate configuration.

The default filename for import is ```prisma_access_full_config.xml```

> If API access is not available, use the Manual skillet option to generate a configuration file to import to Panorama

## Step 5 - Initial Load Config Partial for Service Setup

After the file is imported, this skillet will configure service setup and add the mobile user template

> At the completion of Step 5 a Panorama commit is required before proceeding to step 6
    
## Step 6 - Load Config Partial for Mobile Users and Generate Certificates

```COMMIT to Panorama before running step 6```

This skillet will run through a series of load config partial commands and a certificate
generation to:

    * Configure Mobile User Setup and Onboarding
    * Generate certificates used as part of onboarding configuration
    
> At the completion of Step 6 commit to Panorama and push the configuration to Prisma Access

GUI instructions to commit the changes and push to Prisma Access are found in the 
[Admin Guide](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/administer-prisma-access/commit-push-and-revert-prisma-access-configuration-changes.html)

## Optional non-API Config File Generation

If API access to Panorama is not available, the following steps can be used as an alternative to steps 4, 5, and 6.


1. Run the Optional Manual skillet to generate a config file
2. Copy the xml file output to a file with name ```prisma_access_full_config.xml```
3. Import the file to Panorama (Panorama > Setup > Operations)
4. Use the CLI and follow the [manual steps for load config partial]((https://github.com/PaloAltoNetworks/prisma-access-skillets/blob/develop/stage_2_configuration/full_config/README.md))


## Retrieve Service Information

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

