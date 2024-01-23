# Define a hash that maps patterns to email addresses
email_map = {
  /^ptp/ => 'ptp@gmail.com',
  /^ddd/ => 'ddd@gmail.com',
  /^rtr/ => 'rtr@gmail.com'
}

# Input servicename
servicename = 'rtr-123@#$'

num = 0

# Find the matching email address
matching_email = nil
email_map.each do |pattern, email|
  puts num,pattern
  num += 1
  if servicename.match?(pattern)
    matching_email = email
    break
  end
end

# Print the matching email address if found
if matching_email
  puts "Matching email: #{matching_email}"
else
  puts "No matching email found for servicename: #{servicename}"
end
