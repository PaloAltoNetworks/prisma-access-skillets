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


#############################################################################
## Required Variables                                                      ##
#############################################################################
# AWS Credential
variable "access_key" {
    description = "AWS Access Key"
    default = ""
}
variable "secret_key" {
    description = "AWS Secret Key"
    default = ""
}

variable "panorama_version" {
  description =  "Panorama Version"
  default = "9.0.5"
}

variable "resource_group" {
  description = "Resource Group"
  default = "some-unique-name"
}

variable "public_key" {
  description = "Public Key"
  default = ""
}

# AWS Region and Availablility Zone
variable "region" {
    default = "us-east-1"
}
