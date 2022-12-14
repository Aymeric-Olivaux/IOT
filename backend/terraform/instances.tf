# ------------------------------------------------------ Instances section --- #

# ----------------------------------------------------------------- Locals --- #

locals {
  user_data           = file("./cloud-init.yaml")
  private_ip          = "10.0.0.10"
  availability_zone   = "eu-west-3a"
  default_volume_size = 50
}


# ----------------------------------------------------------------- Images --- #

data "openstack_images_image_v2" "ubuntu-22-04" {
  name = "ubuntu-22.04-2022"
}


# ---------------------------------------------------------------- Flavors --- #

data "openstack_compute_flavor_v2" "instance-flavor" {
  name = "c4.large"
}


# -------------------------------------------------------------- Instances --- #

resource "openstack_compute_instance_v2" "instance" {
  name              = "iot"
  flavor_id         = data.openstack_compute_flavor_v2.instance-flavor.id
  key_pair          = openstack_compute_keypair_v2.kp_sigl_admin.name
  user_data         = local.user_data
  availability_zone = local.availability_zone
  network {
    name        = openstack_networking_network_v2.internal-network.name
    fixed_ip_v4 = local.private_ip
  }
  security_groups = [
    openstack_networking_secgroup_v2.ssh.name,
    openstack_networking_secgroup_v2.http.name,
    openstack_networking_secgroup_v2.https.name,
    openstack_networking_secgroup_v2.api.name,
    data.openstack_networking_secgroup_v2.default.name
  ]

  block_device {
    uuid                  = data.openstack_images_image_v2.ubuntu-22-04.id
    source_type           = "image"
    destination_type      = "volume"
    volume_size           = local.default_volume_size
    delete_on_termination = true
  }

  depends_on = [
    openstack_networking_subnet_v2.internal-network-subnet
  ]
}


# ------------------------------------------------ Floating IP association --- #

resource "openstack_compute_floatingip_associate_v2" "front" {
  floating_ip = data.openstack_networking_floatingip_v2.front_ip.address
  instance_id = openstack_compute_instance_v2.instance.id
}
