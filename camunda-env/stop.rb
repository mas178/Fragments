#-------------------
# Stop Camunda
#
# sample command:
#   itamae local --node-json camunda-7.4.json stop.rb
#-------------------
execute 'Stop Camunda' do
  cwd "#{Dir::pwd}/#{node[:camunda][:name]}/server/#{node[:tomcat]}/bin/"
  command './shutdown.sh'
end
