# Loading the Rendered Full Config

The full configuration is designed to be imported to Panorama and then config elements load and merged into
the existing configuration using the CLI ```load config partial``` commands below.

After running the skillet, save the config file as ```prisma_access_full_config.xml``` and import to Panorama.

Use the manual commands below to merge the config elements to the candidate config or use the Step 2 Load Config Partial
skillet to leverage the Panorama API to merge the configuration.

## Load Config Partial Commands

### Service Setup

Includes:

* template, template-stack, device-group elements
* infrastructure subnet and BGP AS initial configuration

```bash
load config partial from-xpath /config/devices/entry[@name='localhost.localdomain']/template/entry[@name='Service_Conn_Template'] to-xpath /config/devices/entry[@name='localhost.localdomain']/template/entry[@name='Service_Conn_Template'] mode merge from prisma_access_full_config.xml
load config partial from-xpath /config/devices/entry[@name='localhost.localdomain']/template-stack/entry[@name='Service_Conn_Template_Stack'] to-xpath /config/devices/entry[@name='localhost.localdomain']/template-stack/entry[@name='Service_Conn_Template_Stack'] mode merge from prisma_access_full_config.xml
load config partial from-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='Service_Conn_Device_Group'] to-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='Service_Conn_Device_Group'] mode merge from prisma_access_full_config.xml
load config partial from-xpath /config/devices/entry[@name='localhost.localdomain']/plugins/cloud_services/service-connection to-xpath /config/devices/entry[@name='localhost.localdomain']/plugins/cloud_services/service-connection mode merge from prisma_access_full_config.xml
```

### Mobile User Setup and Onboarding

Includes:

* zone configuration
* default security pre-rules for mobile users
* auth profile for local-DB and sample users
* global-protect gateway config
* global-protect tunnel config
* global-protect portal config
* plug-in onboarding configuration

NOTE: The target template and certificate generation are operational commands and performed in tandem with mobile user
configuration. These certs are normally auto-generated in the web UI for use in mobile onboarding configuration.

```bash
load config partial from-xpath /config/devices/entry[@name='localhost.localdomain']/template/entry[@name='Mobile_User_Template'] to-xpath /config/devices/entry[@name='localhost.localdomain']/template/entry[@name='Mobile_User_Template'] mode merge from prisma_access_full_config.xml
load config partial from-xpath /config/devices/entry[@name='localhost.localdomain']/template-stack/entry[@name='Mobile_User_Template_Stack'] to-xpath /config/devices/entry[@name='localhost.localdomain']/template-stack/entry[@name='Mobile_User_Template_Stack'] mode merge from prisma_access_full_config.xml
load config partial from-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='Mobile_User_Device_Group'] to-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='Mobile_User_Device_Group'] mode merge from prisma_access_full_config.xml
run set system setting target template name Mobile_User_Template
run request certificate generate ca yes certificate-name "Authentication Cookie CA" name "Authentication Cookie CA" algorithm RSA rsa-nbits 2048
run request certificate generate signed-by "Authentication Cookie CA" certificate-name "Authentication Cookie Cert" name "Authentication Cookie Cert" algorithm RSA rsa-nbits 2048
run set system setting target none
load config partial from-xpath /config/devices/entry[@name='localhost.localdomain']/plugins/cloud_services/mobile-users to-xpath /config/devices/entry[@name='localhost.localdomain']/plugins/cloud_services/mobile-users mode merge from prisma_access_full_config.xml
```

