import os
import sys
import json
import logging
import paho.mqtt.client as mqtt
from mcrcon import MCRcon

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("minecraft_rcon_mqtt.log", mode="a")
    ],
)

# RCON connection details
RCON_HOST = os.getenv("RCON_HOST", "192.168.178.75")
RCON_PORT = int(os.getenv("RCON_PORT", 25575))
RCON_PASSWORD = os.getenv("RCON_PASSWORD", "sup3r53cr3t")

# MQTT Configuration
MQTT_BROKER = os.getenv("MQTT_BROKER", "192.168.178.75")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "minecraft/rcon")


def send_rcon_command(commands):
    """Sends a list of commands to a Minecraft server via RCON."""
    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, RCON_PORT) as mcr:
            for command in commands:
                command = command.strip()
                logging.info(f"Sending command: {command}")
                response = mcr.command(command)
                logging.info(f"Response: {response}")
    except Exception as e:
        logging.error(f"Error communicating with Minecraft RCON: {e}")


def on_message(client, userdata, msg):
    """Handles incoming MQTT messages containing JSON arrays of RCON commands."""
    try:
        payload = msg.payload.decode("utf-8").strip()
        logging.info(f"Received MQTT message: {payload}")

        # Parse JSON array of commands
        commands = json.loads(payload)
        if isinstance(commands, list):
            send_rcon_command(commands)
        else:
            logging.error("Invalid JSON format: Expected an array of commands.")
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON received: {e}")


def mqtt_listener():
    """Connects to an MQTT broker and listens for commands."""
    client = mqtt.Client()
    client.on_message = on_message

    try:
        logging.info(f"Connecting to MQTT Broker {MQTT_BROKER}:{MQTT_PORT}")
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.subscribe(MQTT_TOPIC)
        logging.info(f"Subscribed to MQTT topic: {MQTT_TOPIC}")
        client.loop_forever()
    except Exception as e:
        logging.error(f"MQTT connection error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    logging.info("Starting Minecraft RCON MQTT Client...")
    mqtt_listener()
