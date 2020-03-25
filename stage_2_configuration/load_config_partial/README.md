## Load Config Partial and Generate Certificates

This stage merges elements of the full config into the Panorama candidate configuration. It also creates a local
certificate and CA used by the mobile user configuration.

The step 2 skillet will use the Panorama API to perform the load config partial commands and cert generation.

If access to the API is not available, users can opt to access the CLI and use the 
[manual steps for load config partial](https://github.com/scotchoaf/prisma-access-skillets/blob/develop_partial/full_config/README.md)

Once the load config partial is complete, commit the configuration to Panorama and push changes to the cloud service.

GUI instructions to commit the changes are found in the 
[Admin Guide](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/administer-prisma-access/commit-push-and-revert-prisma-access-configuration-changes.html)
