# DS_AGENT

1. Copy all inside the agent.sh file
2. ssh to server
3. mkdir TrendMicroDSAgent && cd TrendMicroDSAgent
4. vi agent.sh

        mkdir TrendMicroDSAgent && cd TrendMicroDSAgent && vi agent.sh

5. paste data, save & exit
6. chmod 755 agent.sh

    chmod 755 agent.sh && ./agent.sh && systemctl status ds_agent

7. ./agent.sh

    output:

        Downloading agent package...
        Installing agent package...
        Selecting previously unselected package ds-agent.
        (Reading database ... 215483 files and directories currently installed.)
        Preparing to unpack /tmp/agent.deb ...
        Unpacking ds-agent (20.0.0.7303) ...
        Setting up ds-agent (20.0.0.7303) ...
        Grant permission 0755 for the working directory
        Grant permission 0755 for the directory '/var/opt'
        Enable ds_agent with systemd
        Created symlink /etc/systemd/system/multi-user.target.wants/ds_agent.service → /lib/systemd/system/ds_agent.service.
        Processing triggers for systemd (245.4-4ubuntu3.20) ...
        Install the agent package successfully
        HTTP Status: 200 - OK
        2023-06-30 12:12:38.822914 [+0700]: Activation will be re-attempted 30 time(s) in case of failure
        2023-06-30 12:12:38.823121 [+0700]: dsa_control
        HTTP Status: 200 - OK
        Response:
        Attempting to connect to https://agents.workload.sg-1.cloudone.trendmicro.com:443/
        SSL handshake completed successfully - initiating command session.
        Connected with ECDHE-RSA-AES256-GCM-SHA384 to peer at agents.workload.sg-1.cloudone.trendmicro.com
        Received a 'GetHostInfo' command from the manager.
        Received a 'SetDSMCert' command from the manager.
        Received a 'SetAgentCredentials' command from the manager.
        Received a 'GetAgentEvents' command from the manager.
        Received a 'SetAgentStatus' command from the manager.
        Received a 'GetInterfaces' command from the manager.
        Received a 'GetAgentEvents' command from the manager.
        Received a 'GetHostMetaDataQueryCapabilities' command from the manager.
        Received a 'GetHostMetaData' command from the manager.
        Received a 'GetCapabilities' command from the manager.
        Received a 'GetAgentStatus' command from the manager.
        Received a 'GetAgentEvents' command from the manager.
        Received a 'GetDockerVersion' command from the manager.
        Received a 'GetCRIOVersion' command from the manager.
        Received a 'SetXDRInformation' command from the manager.
        Received a 'SetSecurityConfiguration' command from the manager.
        Received a 'GetAgentEvents' command from the manager.
        Received a 'GetAgentStatus' command from the manager.
        Received a 'GetIoT' command from the manager.
        Received a 'SetDSMCACert' command from the manager.
        Command session completed.

8. systemctl status ds_agent

    output:

        ● ds_agent.service - Trend Micro Deep Security Agent
            Loaded: loaded (/lib/systemd/system/ds_agent.service; enabled; vendor preset: enabled)
            Active: active (running) since Fri 2023-06-30 12:12:21 +07; 5min ago
        Main PID: 888854 (ds_agent)
            Tasks: 13 (limit: 1024)
            Memory: 50.3M
            CGroup: /system.slice/ds_agent.service
                    ├─888854 /opt/ds_agent/ds_agent -w /var/opt/ds_agent -b -i -e /opt/ds_agent/ext
                    └─888855 /opt/ds_agent/ds_agent -w /var/opt/ds_agent -b -i -e /opt/ds_agent/ext

        Jun 30 12:12:21 kafv39s1 systemd[1]: Starting Trend Micro Deep Security Agent...
        Jun 30 12:12:21 kafv39s1 groupadd[888836]: group added to /etc/group: name=tm_dsa, GID=1008
        Jun 30 12:12:21 kafv39s1 groupadd[888836]: group added to /etc/gshadow: name=tm_dsa
        Jun 30 12:12:21 kafv39s1 groupadd[888836]: new group: name=tm_dsa, GID=1008
        Jun 30 12:12:21 kafv39s1 ds_agent.init[888808]: Starting ds_agent: [OK]
        Jun 30 12:12:21 kafv39s1 systemd[1]: Started Trend Micro Deep Security Agent.
