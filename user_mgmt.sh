#!/bin/bash

LOG_FILE="/var/log/user_mgmt.log"

log_action() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

create_user() {
    read -p "Username: " USERNAME
    read -p "Group: " GROUP
    read -p "Grant sudo? (y/n): " SUDO

    groupadd -f "$GROUP"
    useradd -m -g "$GROUP" "$USERNAME"
    chage -M 90 -m 10 -W 7 "$USERNAME"

    if [ "$SUDO" == "y" ]; then
        usermod -aG sudo "$USERNAME"
    fi

    log_action "Created user $USERNAME in group $GROUP (sudo=$SUDO)"
    echo "User created."
}

delete_user() {
    read -p "Username to delete: " USERNAME
    deluser --remove-home "$USERNAME"
    log_action "Deleted user $USERNAME and their home directory"
    echo "User deleted."
}

echo "1. Create User"
echo "2. Delete User"
read -p "Enter choice: " CHOICE

if [ "$EUID" -ne 0 ]; then
    echo "Run as root"
    exit 1
fi

case $CHOICE in
    1) create_user ;;
    2) delete_user ;;
    *) echo "Invalid choice" ;;
esac
