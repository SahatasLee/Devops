# custom_email_filter.rb
require 'time'

# Define a hash mapping service names to email addresses
service_email_mapping = {
  # /Regex Pattern/ => 'email@email.com'
  # /^ptp/ => 'loadgenerator@gmail.com'
  # /Regex Pattern/ => 'email-1@email.com, email-2@email.com',
  # Add more service names and corresponding email addresses here
  /^ptp/ => 'ptp@gmail.com',
  /^rtr/ => 'rtr@outlook.co.th'
}

# Define a custom Logstash filter plugin
def filter(event)
    t1 = event.get("@timestamp")
    t1 = Time.parse(t1)
    offset = 7 * 3600
    event.set("newtimestamp", Time.at(t1 + offset))
    t2 = Time.at(t1 + 0)
    event.set("t2", t2.strftime("%d/%m/%Y, %H:%M:%S") ) 

    # Check if the event contains a 'service_name' field
    if event.get('servicename')
      service_name = event.get('servicename').downcase # Convert to lowercase for case-insensitive matching

      # Find the matching email address
      # Loops each service_email_mapping
      email_map.each do |pattern, email|
        # Check if the service name exists in the mapping
        if servicename.match?(pattern)
          # Set the 'email_sent' field to the corresponding email address
          event.set('email_sent', email)
          break
        end
      end
    end
  
    # Return the modified event
    return [event]
  end
  
