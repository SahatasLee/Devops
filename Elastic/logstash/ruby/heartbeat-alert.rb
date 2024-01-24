# heartbeat-alert.rb
require 'time'

# Define a custom Logstash filter plugin
def filter(event)
    # puts "Ruby version: #{RUBY_VERSION}"
    # Ruby version 3.1.0
    # puts "Service name:",event.get('[monitor][id]')

    # Define a hash that maps service names to one or more email addresses.
    # The keys in this hash are regular expressions (regex patterns) used to match service names,
    # and the values are the corresponding email addresses for those services.
    service_email_mapping = {
      # /Regex Pattern/ => 'email@email.com'
      # /^ptp/ => 'ptp@gmail.com'
      # /Regex Pattern/ => 'email-1@email.com, email-2@email.com',
      # Add more service names and corresponding email addresses here
      /^ptp/ => 'sahatasnutlee@gmail.com, sahataslee@outlook.co.th',
      /^rtm/ => 'sahataslee@icloud.com'
    }
    
    # Define an offset of 7 hours in seconds (7 * 3600 seconds).
    offset = 7 * 3600

    # Get the value of "@timestamp" from an event (assuming it's a timestamp in seconds since epoch).
    t1 = event.get("@timestamp")

    # Add the offset to the original timestamp and set it as "new_timestamp".
    event.set("new_timestamp", Time.at(t1 + offset))

    # strftime auto +7
    # Create a new timestamp with a fixed offset of 0 seconds and format it as "day/month/year, hour:minute:second".
    event.set("custom_timestamp", Time.at(t1 + 0).strftime("%d/%m/%Y, %H:%M:%S") ) 

    # Check if the event contains a 'service_name' field
    if event.get('[monitor][id]')
      # Convert to lowercase for case-insensitive matching
      service_name = event.get('[monitor][id]').downcase

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
    end
    # Debugging: Print a message indicating that an email has been sent and display the value of the 'email_sent' field from the 'event' data.
    # Debug email status
    # puts "Email sent:",event.get('email_sent')
    # Return the modified event
    return [event]
  end
  
