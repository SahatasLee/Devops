# custom_email_filter.rb
require 'time'

# Define a custom Logstash filter plugin
def filter(event)
    puts "Ruby version: #{RUBY_VERSION}"
    t1 = event.get("@timestamp")
    offset = 7 * 3600
    event.set("new_timestamp", Time.at(t1 + offset))
    # strftime auto +7
    event.set("custom_timestamp", Time.at(t1 + 0).strftime("%d/%m/%Y, %H:%M:%S") ) 

    # Check if the event contains a 'service_name' field
    if event.get('servicename')
      service_name = event.get('servicename').downcase # Convert to lowercase for case-insensitive matching
    elsif event.get('service.name')
      service_name = event.get('[service][name]').downcase # Convert to lowercase for case-insensitive matching
    else 
      return [event]
    end

    # Define a hash mapping service names to email addresses
    service_email_mapping = {
      # /Regex Pattern/ => 'email@email.com'
      # /^ptp/ => 'ptp@gmail.com'
      # /Regex Pattern/ => 'email-1@email.com, email-2@email.com',
      # Add more service names and corresponding email addresses here
      /^frontend/ => 'sahatasnutlee@gmail.com, sahataslee@outlook.co.th',
      /^load/ => 'sahataslee@icloud.com'
    }

    # Find the matching email address
    # Loops each service_email_mapping
    service_email_mapping.each do |pattern, email|
      # Check if the service name exists in the mapping
      if service_name.match?(pattern)
        # Set the 'email_sent' field to the corresponding email address
        event.set('email_sent', email)
        break
      end
    end

    puts "this is  from event.get #{event.get("email_sent")}"

    # Return the modified event
    return [event]
  end
  
