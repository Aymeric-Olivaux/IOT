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

# ---------------------------------------------------------------- Default --- #

data "openstack_networking_secgroup_v2" "default" {
  name = "default"
}