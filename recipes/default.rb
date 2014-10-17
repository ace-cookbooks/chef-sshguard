include_recipe 'iptables'
iptables_rule "sshguard"

package 'sshguard' do
  action :install
end

service 'sshguard' do
  supports status: true, start: true, stop: true, restart: true
  action [:enable, :start]
end
