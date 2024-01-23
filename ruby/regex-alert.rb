# Define a hash that maps patterns to email addresses
email_map = {
    /^frontend/ => 'frontend@gmail.com',
    /^load/ => 'load@outlook.co.th'
}

# Input servicename
servicename = 'frontend-#?!'

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
