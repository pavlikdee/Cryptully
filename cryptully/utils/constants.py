DEFAULT_TURN_SERVER = 'shanetully.com'
DEFAULT_PORT        = 9000

NICK_MAX_LEN = 32

# Operation modes
MODE_SERVER = 0
MODE_CLIENT = 1

# Protocol commands

# Server commands
COMMAND_REGISTER   = "REG"
COMMAND_RELAY      = "REL"

# Client commands

# Handshake commands
COMMAND_HELO       = "HELO"
COMMAND_REDY       = "REDY"
COMMAND_REJECT     = "REJ"
COMMAND_PUBLIC_KEY = "PUB_KEY"
COMMAND_AES_KEY    = "AES_KEY"
COMMAND_AES_IV     = "AES_IV"
COMMAND_AES_SALT   = "AES_SALT"

# Loop commands
COMMAND_MSG        = "MSG"
COMMAND_END        = "END"
COMMAND_ERR        = "ERR"
LOOP_COMMANDS = [COMMAND_MSG, COMMAND_END, COMMAND_ERR]

# Message sources
SENDER   = 0
RECEIVER = 1
SERVICE  = 2

# QT UI custom button codes
BUTTON_OKAY   = 0
BUTTON_CANCEL = 1
BUTTON_FORGOT = 2
