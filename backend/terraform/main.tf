# ----------------------------------------------------------- Main section --- #

terraform {
  required_providers {
    openstack = {
      source  = "terraform-provider-openstack/openstack"
      version = "~> 1.42.0"
    }
  }
}

provider "openstack" {
  cloud       = "openstack"
  use_octavia = "true"
}