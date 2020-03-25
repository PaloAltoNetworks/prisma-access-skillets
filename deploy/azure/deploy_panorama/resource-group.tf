//# ********** RESOURCE GROUP **********
//# Configure the Providers
provider "azurerm" {
  version = "=1.37.0"
}

provider "random" {}

//# Create a resource group
resource "azurerm_resource_group" "resourcegroup" {
	name		= "${var.virtualMachineRG}"
	location	= "${var.Location}"
}