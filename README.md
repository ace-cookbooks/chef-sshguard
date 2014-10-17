sshguard Cookbook
=============
A chef cookbook for installing sshguard

Requirements
------------
This has been tested on amazon linux.  It requires the iptables cookbook.

Note: This cookbook disables iptables default rules on rhel and fedora platforms.

#### packages
- `sshguard` - An rpm spec file can be found in this repository.

Usage
-----
#### sshguard::default

Just include `sshguard` in your node's `run_list`:

```json
{
  "name":"my_node",
  "run_list": [
    "recipe[test]"
  ]
}
```

Contributing
------------
1. Fork the repository on Github
2. Create a named feature branch (like `add_component_x`)
3. Write your change
4. Write tests for your change (if applicable)
5. Run the tests, ensuring they all pass
6. Submit a Pull Request using Github

License and Authors
-------------------
Authors: Ryan Schlesinger
