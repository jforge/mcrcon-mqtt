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


## Example

```bash
CON_PORT=25675 python minecraft_rcon_client.py /list
2025-02-02 11:38:43,214 - INFO - Sending command: /list
2025-02-02 11:38:43,225 - INFO - Response: There are 1 of a max of 10 players online: XYZ
```

