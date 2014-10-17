name             "sshguard"
maintainer       "Ace of Sales"
maintainer_email "cookbooks@aceofsales.com"
license          "Apache 2.0"
description      "Configures sshguard"
long_description IO.read(File.join(File.dirname(__FILE__), 'README.md'))
version          "1.0.0"

depends "iptables"
