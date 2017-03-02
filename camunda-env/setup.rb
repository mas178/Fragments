#-------------------
# Setup Camunda
#
# sample command:
#   $ itamae local --node-json camunda-7.4.json setup.rb
#-------------------
base_dir = Dir::pwd

#-------------------------------
# Edit server.xml to connect MySQL
#-------------------------------
url_h2 = 'h2:.\\/camunda-h2-dbs\\/process-engine;MVCC=TRUE;TRACE_LEVEL_FILE=0;DB_CLOSE_ON_EXIT=FALSE'
url_mysql = 'mysql:\\/\\/localhost:3306\\/camundabpm?autoReconnect=true'

execute 'Edit server.xml' do
  cwd "#{base_dir}/#{node[:camunda][:name]}/server/#{node[:tomcat]}/conf/"
  command <<-EOL
    grep -l 'org.h2.Driver' server.xml | xargs sed -i.bak -e 's/org.h2.Driver/com.mysql.jdbc.Driver/g'
    grep -l '#{url_h2}' server.xml | xargs sed -i.bak -e 's/#{url_h2}/#{url_mysql}/g';
    grep -l '\"sa\"' server.xml | xargs sed -i.bak -e 's/\"sa\"/\"root\"/g';
  EOL
end

#-------------------------------
# Edit tomcat-users.xml to add tomcat admin user
#-------------------------------
user_info = '\
  \\<role rolename=\\"manager-gui\\"\\/\\>\
  \\<role rolename=\\"admin-gui\\"\\/\\>\
  \\<user username=\\"tomcat\\" password=\\"password\\" roles=\\"manager-gui,admin-gui\\"\\/\\>\
\\<\\/tomcat-users\\>'

execute 'Edit tomcat-users.xml' do
  cwd "#{base_dir}/#{node[:camunda][:name]}/server/#{node[:tomcat]}/conf/"
  command <<-EOL
    grep -l '</tomcat-users>' tomcat-users.xml | xargs sed -i.bak -e 's/\\<\\/tomcat-users\\>/#{user_info}/g'
  EOL
end

#-------------------------------
# Copy JDBC Driver for MySQL to Tomcat
#-------------------------------
execute 'Copy JDBC Driver for MySQL' do
  cwd base_dir
  command <<-EOL
    cp ./#{node[:driver][:name]}/#{node[:driver][:name]}/#{node[:driver][:name]}-bin.jar ./#{node[:camunda][:name]}/server/#{node[:tomcat]}/lib
    rm -rf #{node[:driver][:name]}
  EOL
end

#-------------------------------
# Setup MySQL
#-------------------------------
execute 'Setup MySQL' do
  cwd "#{base_dir}/#{node[:camunda][:name]}/sql/create/"
  command <<-EOL
    mysql -u root -proot -e'DROP DATABASE IF EXISTS camundabpm;'
    mysql -u root -proot -e'CREATE DATABASE camundabpm;'
    mysql -u root -proot camundabpm < mysql_identity_#{node[:camunda][:version]}.sql
    mysql -u root -proot camundabpm < mysql_engine_#{node[:camunda][:version]}.sql
  EOL
end

#-------------------------------
# Tidy up
#-------------------------------
execute 'Tidy garbage files up' do
  cwd "#{base_dir}/#{node[:camunda][:name]}/"
  command <<-EOL
    cp sql/create/mysql_*.sql sql/
    rm -rf sql/create
    rm -rf sql/upgrade
    rm -rf sql/drop
    rm -rf server/#{node[:tomcat]}/webapps/h2
    rm -rf server/#{node[:tomcat]}/webapps/examples
    rm server/#{node[:tomcat]}/bin/*.bat
    rm *.bat
  EOL
end
