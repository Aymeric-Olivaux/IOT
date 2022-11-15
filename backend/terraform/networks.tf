# ------------------------------------------------------- Networks section --- #

# ----------------------------------------------------------------- Locals --- #

locals {
  internal_network_subnet_cidr = "10.0.0.0/24"
}


# ---------------------------------------------------------------- Routers --- #

data "openstack_networking_router_v2" "ext-router" {
  name = "SIGL-ext-router"
}


# --------------------------------------------------------------- Networks --- #

resource "openstack_networking_network_v2" "internal-network" {
  name           = "internal-network"
  admin_state_up = "true"
  shared         = "false"
  external       = "false"
}


# --------------------------------------------------------------- Subnets --- #

resource "openstack_networking_subnet_v2" "internal-network-subnet" {
  name            = "internal-network-subnet"
  network_id      = openstack_networking_network_v2.internal-network.id
  cidr            = local.internal_network_subnet_cidr
  ip_version      = 4
  enable_dhcp     = "true"
  dns_nameservers = ["1.1.1.1", "1.0.0.1"]
}


# ------------------------------------------------------- Router-Interface --- #

resource "openstack_networking_router_interface_v2" "internal-network-router-interface" {
  router_id = data.openstack_networking_router_v2.ext-router.id
  subnet_id = openstack_networking_subnet_v2.internal-network-subnet.id
}


# ----------------------------------------------------------- Floating IPs --- #

data "openstack_networking_floatingip_v2" "front_ip" {
  address = "192.168.0.182"
}