# ------------------------------------------------ Security groups section --- #

# -------------------------------------------------------------------- SSH --- #

resource "openstack_networking_secgroup_v2" "ssh" {
  name        = "ssh_secgroup"
  description = "Allow SSH traffic"
}

resource "openstack_networking_secgroup_rule_v2" "ssh_ingress" {
  direction         = "ingress"
  ethertype         = "IPv4"
  port_range_min    = 22
  port_range_max    = 22
  protocol          = "tcp"
  security_group_id = openstack_networking_secgroup_v2.ssh.id
}


# ------------------------------------------------------------------- HTTP --- #

resource "openstack_networking_secgroup_v2" "http" {
  name        = "http_secgroup"
  description = "Allow HTTP traffic"
}

resource "openstack_networking_secgroup_rule_v2" "http_ingress" {
  direction         = "ingress"
  ethertype         = "IPv4"
  port_range_min    = 80
  port_range_max    = 80
  protocol          = "tcp"
  security_group_id = openstack_networking_secgroup_v2.http.id
}


# ------------------------------------------------------------------ HTTPS --- #

resource "openstack_networking_secgroup_v2" "https" {
  name        = "https_secgroup"
  description = "Allow HTTPS traffic"
}

resource "openstack_networking_secgroup_rule_v2" "https_ingress" {
  direction         = "ingress"
  ethertype         = "IPv4"
  port_range_min    = 443
  port_range_max    = 443
  protocol          = "tcp"
  security_group_id = openstack_networking_secgroup_v2.https.id
}


# -------------------------------------------------------------------- API --- #

resource "openstack_networking_secgroup_v2" "api" {
  name        = "api_secgroup"
  description = "Allow API traffic"
}

resource "openstack_networking_secgroup_rule_v2" "api_ingress" {
  direction         = "ingress"
  ethertype         = "IPv4"
  port_range_min    = 8000
  port_range_max    = 8000
  protocol          = "tcp"
  security_group_id = openstack_networking_secgroup_v2.api.id
}


# ---------------------------------------------------------------- Default --- #

data "openstack_networking_secgroup_v2" "default" {
  name = "default"
}