# custom_email_filter.rb
require 'time'


# Define a custom Logstash filter plugin
def filter(event)
    t1 = event.get("@timestamp")
    t1 = Time.parse(t1)
    offset = 7 * 3600
    event.set("newtimestamp", Time.at(t1 + offset))
    t2 = Time.at(t1 + offset)
    event.set("T2", t2.strftime("%d/%m/%Y, %H:%M:%S") ) 

    # Check if the event contains a 'service_name' field
    if event.get('servicename')
      service_name = event.get('servicename').downcase # Convert to lowercase for case-insensitive matching
  
      # Define a hash mapping service names to email addresses
      service_email_mapping = {
        # 'ptp-service' => 'ptp@email.com',
        # Add more service names and corresponding email addresses here
        'loadgenerator' => 'loadgenerator@gmail.com',
        'frontend-proxy' => 'frontend-proxy@gmail.com'
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
  