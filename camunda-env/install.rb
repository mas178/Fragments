#-------------------
# Download and decompress files to develop on Camunda
#
# sample command:
#   $ itamae local --node-json camunda-7.4.json install.rb
#-------------------
define :install do
  name = node[params[:name]][:name]
  url  = node[params[:name]][:url]

  directory "download"
  directory "#{Dir::pwd}/#{name}"

  execute "Download #{name}" do
    cwd "#{Dir::pwd}/download"
    command "wget #{url}#{name}.tar.gz"
    not_if "test -e #{name}.tar.gz"
  end

  execute "Decompress #{name}" do
    cwd "#{Dir::pwd}"
    command "tar xzvf download/#{name}.tar.gz -C #{name}"
  end
end

# Download and decompress Camunda BPM & Tomcat
install :camunda

# Download and decompress JDBC Driver for MySQL
install :driver

# Install MySQL
package 'mysql'

# Install Gradle
package 'gradle'
