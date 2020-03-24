# Prisma Access Skillets

A suite of configuration and service information skillets for Prisma Access mobile users including:

* Service setup
* Mobile user setup
* Certificate generation
* Mobile user onboarding

## Using the Skillets

The skillets are staged in 3 steps:
* generate a full configuration file based on user input variables that is imported to Panorama
* use 'load config partial' after import to merge skillet elements into the candidate config
* Prisma API interactions to retrieve service information


## Config File Generation

This still takes user input and outputs to screen a complete xml file

To use:
* run the skillet after entering input values
* copy the output text and save locally as ```prisma_access_full_config.xml```
* import the file to Panorama but do not load as a candidate configuration

## Load Config Partial and Generate Certificates

This stage merges elements of the full config into the Panorama candidate configuration. It also creates a local
certificate and CA used by the mobile user configuration.

The step 2 skillet will use the Panorama API to perform the load config partial commands and cert generation.


If access to the API is not available, users can opt to access the CLI and use the 
[manual steps for load config partial](https://github.com/scotchoaf/prisma-access-skillets/blob/develop_partial/full_config/README.md)

Once the load config partial is complete, commit the configuration to Panorama and push changes to the cloud service.

GUI instructions to commit the changes are found in the 
[Admin Guide](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/administer-prisma-access/commit-push-and-revert-prisma-access-configuration-changes.html)


## Retrive Service Information

The details for using the API and information returned are found in the
[Admin Guide](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-panorama-admin/prisma-access-overview/retrieve-ip-addresses-for-prisma-access.html)

As an alternative to the curl commands and generating and update the option.txt file, the Step 3 skillet
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





