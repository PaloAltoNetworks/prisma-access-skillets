# Scripted Config File Generation and Panorama Import

This skillet avoids the manual steps for creating an xml configuration and importing to Panorama.

Requirement is API access to Panorama.

Steps perfromed by this python skillet:

1. First time run: load the python virtual environment
2. Use the web form data to generate an xml configuration file
3. Import the file to Panorama

Once this skillet has finished, the next step is to use to the API load config partial skillet
to merge config file elements into the candidate configuration.

Included in the generated configuration file:

* template, template-stack, device-group elements
* infrastructure subnet and BGP AS initial configuration
* zone configuration
* default security pre-rules for mobile users
* auth profile for local-DB and sample users
* global-protect gateway config
* global-protect tunnel config
* global-protect portal config
* plug-in onboarding configuration