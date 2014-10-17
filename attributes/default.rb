# Disable the default rules that use the nonexistant 'FWD' chain.
if platform_family?('rhel', 'fedora')
  force_default['iptables']['install_rules'] = false
end
