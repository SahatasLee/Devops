# Ruby version 3.1.0
require 'time'


# Define a custom Logstash filter plugin
def filter(event)
    puts "Ruby version: #{RUBY_VERSION}"
    
    t1 = event.get("@timestamp")
    offset = 7 * 3600
    event.set("new_timestamp", Time.at(t1 + offset))
    # strftime auto +7
    # +o is debug
    event.set("custom_timestamp", Time.at(t1 + 0).strftime("%d/%m/%Y, %H:%M:%S") ) 

    # Check if the event contains a 'service_name' field
    if event.get('servicename')
      service_name = event.get('servicename').downcase # Convert to lowercase for case-insensitive matching
  
      # Define a hash mapping service names to email addresses
      service_email_mapping = {
        # 'ptp-service' => 'ptp@email.com',
        # Add more service names and corresponding email addresses here
        'loadgenerator' => 'email@gmail.com',
        'frontend-proxy' => 'email@outlook.co.th'
      }
  
      # Check if the service name exists in the mapping
      if service_email_mapping.key?(service_name)
        # Set the 'email_sent' field to the corresponding email address
        event.set('email_sent', service_email_mapping[service_name])
      end
    end
  
    # Return the modified event
    return [event]
  end