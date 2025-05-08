#!/bin/bash

#Messages
START_PROCESS="Starting new process: ... "
ENDS_PROCESS="Finalizing the process:"
DONE_MESSAGE="${ENDS_PROCESS} ------> Done!"

# shellcheck disable=SC2028

###### PROCESS #####################
echo "${START_PROCESS} Install the requirements.txt ...${RESET}"
echo "Installing requirements using the following command: pip install -r requirements.txt"
pip install -r requirements.txt
echo "Install.sh: $DONE_MESSAGE"
