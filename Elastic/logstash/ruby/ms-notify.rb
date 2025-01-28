# Ruby version 3.1.0
# ms-notify.rb
require 'time'
require 'net/http'
require 'json'

SERVICE_MS_WEBHOOK_MAPPING = {
  /^ptp/ => 'https://tcctechnology0.webhook.office.com/webhookb2/f52fb4ab-e6f4-4544-966e-86eaf05e524a@b96cc57b-d146-48f5-a381-7cf474c23a9e/IncomingWebhook/a1238fe4f60a4e96aedf4771a70625a4/010496a7-e18c-4770-be6f-3d0d23ad144e/V2BXAefUjWdJN6T9L7GoKLHoEa0w0Omrpup_xoP8kn9_01',
  /^rtm/ => 'https://tcctechnology0.webhook.office.com/webhookb2/f52fb4ab-e6f4-4544-966e-86eaf05e524a@b96cc57b-d146-48f5-a381-7cf474c23a9e/IncomingWebhook/06dd90b68f6d409d985224dc18183bea/010496a7-e18c-4770-be6f-3d0d23ad144e/V265null9b7M9XSeL8dsRB71Djwyn8HVUbjNkyBGKFpJI1'
}

# Function to send notification to Microsoft Teams
def send_to_teams(webhook_url, message)
  uri = URI(webhook_url)
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  request = Net::HTTP::Post.new(uri.path, 'Content-Type' => 'application/json')
  request.body = message.to_json

  response = http.request(request)
  if response.code.to_i == 200
    puts "Message sent successfully!"
  else
    puts "Failed to send message. Code: #{response.code}, Message: #{response.message}"
  end
end

def ms_teams_notify(service_name)
  SERVICE_MS_WEBHOOK_MAPPING.each do |pattern, webhook_url|
    if service_name.match?(pattern)
      event.set('webhook_url', webhook_url)
      puts "webhook url:", webhook_url
      message = {
        text: "Notification from Logstash! Script version 1.0",
        themeColor: "0076D7",
        sections: [
          {
            activityTitle: "Service: #{event.get('[monitor][id]')}",
            activitySubtitle: "Notification sent by Ruby script",
            activityImage: "https://upload.wikimedia.org/wikipedia/commons/7/73/Ruby_logo.svg",
            markdown: true
          }
        ]
      }
      send_to_teams(event.get('[channel_token]'), message)
      break
    end
  end
end

def filter(event)

    if event.get('[monitor][id]')
      service_name = event.get('[monitor][id]').downcase
      puts "Service Name:", service_name
      ms_teams_notify(service_name)
    end
    
    return [event]
  end

