import os
import sys
import logging
from mcrcon import MCRcon

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("minecraft_rcon.log", mode="a")
    ],
)

# Get RCON connection details from environment variables
RCON_HOST = os.getenv("RCON_HOST", "192.168.178.75")
RCON_PORT = int(os.getenv("RCON_PORT", 25575))
RCON_PASSWORD = os.getenv("RCON_PASSWORD", "sup3r53cr3t")


def send_rcon_command(commands):
    """Sends a command (or multiple commands) to a Minecraft server via RCON."""
    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, RCON_PORT) as mcr:
            for command in commands:
                command = command.strip()
                logging.info(f"Sending command: {command}")
                response = mcr.command(command)
                logging.info(f"Response: {response}")
    except Exception as e:
        logging.error(f"Error communicating with Minecraft RCON: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error("Usage: python minecraft_rcon_client.py '<command1>;<command2>'")
        sys.exit(1)

    command_input = sys.argv[1]
    commands = command_input.split(";")  # Supports multiple commands separated by `;`
    send_rcon_command(commands)
