# Minecraft RCON client with MQTT support

This Minecraft RCON client is created to be run
with MQTT support to process commands from a remote broker

## Warning

This is absolutely insecure and no safeguards are planned.

No warranties in any form.

Use it with care.

Please add safeguards like MQTT over TLS and other
typical safety measures as needed.

I recommend to run it containerized in a local network
environment only with no ports exposed ports to the public, 
add at least  TLS encryption and basic auth for the MQTT channel.

## Setup

```
pip install -r ./requirements.txt
```

## Run

### Simple client

The simple client just takes semicolon separated commands as
command line arguments and sends them to the RCON endpoint.

Response output is stdout.

```
python minecraft_rcon_client.py "<command1>;<command2>;..."
```

### MQTT client

The MQTT client listens to a configurable MQTT broker topic
and expects a json array of command strings.

Response output is stdout.

```
python minecraft_rcon_client_mqtt.py
```

```
mosquitto_pub -h <mqtt-broker-host-ip> -p <mqtt-broker-port> -t 'minecraft/rcon' -m '[ "say hello, players!.", "time set 900" ]'
```

```
INFO - Received MQTT message: [ "say hello, players!.", "time set 900" ]
INFO - Sending command: say hello, players!.
INFO - Response:
INFO - Sending command: time set 900
INFO - Response: Set the time to 900
```


## Example

```
python minecraft_rcon_client.py "say Hello, players!;time set day"
```

```
RCON_PORT=25675 python minecraft_rcon_client.py list
2025-02-02 11:38:43,214 - INFO - Sending command: list
2025-02-02 11:38:43,225 - INFO - Response: There are 1 of a max of 10 players online: XYZ
```
