# camunda-env

[Itamae](https://github.com/itamae-kitchen/itamae) scripts to setup development environment of [Camunda](https://camunda.org/).

### Technical environment

- Mac OS X El Capitan Version 10.11.3
- Ruby 2.2.2p95
- Itamae v1.9.3

### Sample command

```sh
# Install Camunda, Tomcat, MySQL, JDBC Driver
itamae local --node-json camunda-7.4.json install.rb

# Edit server.xml / tomcat-users.xml, Copy JDBC Driver, Setup DB and Tidy files up
itamae local --node-json camunda-7.4.json setup.rb

# Start Camunda
itamae local --node-json camunda-7.4.json start.rb

# Stop Camunda
itamae local --node-json camunda-7.4.json stop.rb

# Restart Camunda
itamae local --node-json camunda-7.4.json stop.rb start.rb
```
