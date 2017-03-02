#-------------------
# Start Camunda
#
# sample command:
#   itamae local --node-json camunda-7.4.json start.rb
#-------------------
execute 'Start Camunda' do
  cwd "#{Dir::pwd}/#{node[:camunda][:name]}/"
  command './start-camunda.sh'
end
