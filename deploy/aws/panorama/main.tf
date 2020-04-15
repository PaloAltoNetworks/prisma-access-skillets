############################################################################################
# Copyright 2020 Palo Alto Networks.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
############################################################################################

provider "aws" {
  access_key = "${var.access_key}"
  secret_key = "${var.secret_key}"
  region = "${var.region}"
}

resource "aws_key_pair" "key_pair" {
  key_name = "${var.resource_group}-kp"
  public_key = "${var.public_key}"

  tags = {
    "panhandler_resource_group" = "${var.resource_group}"
    NAME = "KP-${var.resource_group}"
  }
}
resource "aws_resourcegroups_group" "test" {
  name = "${var.resource_group}"

  resource_query {
    query = <<JSON
{
  "ResourceTypeFilters": [
    "AWS::AllSupported"
  ],
  "TagFilters": [
    {
      "Key": "panhandler_resource_group",
      "Values": ["${var.resource_group}"]
    }
  ]
}
JSON
  }
}

# Create a VPC for Panorama
resource "aws_vpc" "management-vpc" {
  cidr_block = "10.255.0.0/16"
  tags = {
    "panhandler_resource_group" = "${var.resource_group}"
    NAME = "VPC-${var.resource_group}"
  }
  enable_dns_hostnames = true
}

resource "aws_security_group" "management" {
  name = "Panorama Security Group"
  description = "Inbound filtering for Panorama"
  vpc_id = "${aws_vpc.management-vpc.id}"

  tags = {
    "panhandler_resource_group" = "${var.resource_group}"
    NAME = "SG-${var.resource_group}"
  }

//  This isn't needed for prisma access POC
//  ingress {
//    from_port   = 3978
//    to_port     = 3978
//    protocol    = "tcp"
//    cidr_blocks = ["0.0.0.0/0"]
//    description = "Firewalls to Panorama"
//  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "SSH access to Panorama"
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "HTTPS access to Panorama"
  }

  egress {
    to_port     = 0
    from_port   = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create a subnet for the primary Panorama
resource "aws_subnet" "management_subnet_primary" {
  vpc_id = "${aws_vpc.management-vpc.id}"
  cidr_block = "10.255.0.0/24"
  tags = {
    "panhandler_resource_group" = "${var.resource_group}"
    NAME = "mgmt-subnet-${var.resource_group}"
  }
}

# Create an IGW so Panorama can get to the Internet for updates and licensing
resource "aws_internet_gateway" "management_igw" {
  vpc_id = "${aws_vpc.management-vpc.id}"

  tags = {
    "panhandler_resource_group" = "${var.resource_group}"
  }
}

# Create a new route table that will have a default route to the IGW
resource "aws_route_table" "management_igw" {
  vpc_id = "${aws_vpc.management-vpc.id}"

  tags = {
    "panhandler_resource_group" = "${var.resource_group}"
  }
}

# Set the default route to point to the IGW
resource "aws_route" "in_default" {
  route_table_id = "${aws_route_table.management_igw.id}"
  destination_cidr_block = "0.0.0.0/0"
  gateway_id = "${aws_internet_gateway.management_igw.id}"
}

# Set the primary Panorama subnet to use the IGW route table
resource "aws_route_table_association" "management_igw_primary" {
  subnet_id = "${aws_subnet.management_subnet_primary.id}"
  route_table_id = "${aws_route_table.management_igw.id}"
}

# Create an interface and set the internal IP to the 4th IP address in the subnet.
resource "aws_network_interface" "management" {
  subnet_id = "${aws_subnet.management_subnet_primary.id}"
  private_ips = [
    "10.255.0.4"]
  security_groups = [
    "${aws_security_group.management.id}"]
  source_dest_check = true

  tags = {
    "panhandler_resource_group" = "${var.resource_group}"
  }
}

data "aws_ami" "panorama-vm" {
  most_recent = true
  owners = [
    "679593333241"]
  # owner id for Paloaltonetworks

  filter {
    name = "name"
    values = [
      "Panorama-AWS-${var.panorama_version}*"]
  }
}

# Create an external IP address and associate it to the management interface
resource "aws_eip" "management" {
  vpc = true
  network_interface = "${aws_network_interface.management.id}"

  tags = {
    "panhandler_resource_group" = "${var.resource_group}"
    NAME = "EIP-${var.resource_group}"
  }

  depends_on = ["aws_instance.panorama"]

}

resource "aws_instance" "panorama" {

  ami = "${data.aws_ami.panorama-vm.id}"
  instance_type = "m4.2xlarge"
  key_name = "${aws_key_pair.key_pair.id}"

  ebs_optimized = true

  network_interface {
    device_index = 0
    network_interface_id = "${aws_network_interface.management.id}"
  }

  # Setting this to true so that the disk is deleted when the instance is deleted.
  root_block_device {
    delete_on_termination = "true"
  }

  tags = {
    "panhandler_resource_group" = "${var.resource_group}"
    NAME = "Panorama-${var.resource_group}"
  }
}


