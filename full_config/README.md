# Loading the Rendered Full Config

### Load Config Partial Commands:

Use the CLI to onboard mobile users

* global-protect gateway config
* global-protect tunnel config
* global-protect portal config
* plug-in onboarding configuration

```bash
load config partial from-xpath /config/devices/entry[@name="localhost.localdomain"]/template/entry[@name="Mobile_User_Template"]/config/devices/entry[@name="localhost.localdomain"]/vsys/entry[@name="vsys1"] to-xpath /config/devices/entry[@name="localhost.localdomain"]/template/entry[@name="Mobile_User_Template"]/config/devices/entry[@name="localhost.localdomain"]/vsys/entry[@name="vsys1"] mode merge from prisma_access_full_config.xml
load config partial from-xpath /config/devices/entry[@name="localhost.localdomain"]/template/entry[@name="Mobile_User_Template"]/config/devices/entry[@name="localhost.localdomain"] to-xpath /config/devices/entry[@name="localhost.localdomain"]/template/entry[@name="Mobile_User_Template"]/config/devices/entry[@name="localhost.localdomain"] mode merge from prisma_access_full_config.xml
load config partial from-xpath /config/devices/entry[@name="localhost.localdomain"]/template/entry[@name="Mobile_User_Template"]/config/devices/entry[@name="localhost.localdomain"]/vsys/entry[@name="vsys1"] to-xpath /config/devices/entry[@name="localhost.localdomain"]/template/entry[@name="Mobile_User_Template"]/config/devices/entry[@name="localhost.localdomain"]/vsys/entry[@name="vsys1"] mode merge from prisma_access_full_config.xml
load config partial from-xpath /config/devices/entry[@name="localhost.localdomain"]/plugins/cloud_services/mobile-users to-xpath /config/devices/entry[@name="localhost.localdomain"]/plugins/cloud_services/mobile-users mode merge from prisma_access_full_config.xml
```

