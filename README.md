# Automated User and Group Management System

This project automates Linux user and group management using Bash and Python. It focuses on identity and access control, enforcing password policies and sudo permissions to simulate secure user provisioning in an enterprise environment.

## Features

- Create or delete users and groups
- Enforce password complexity and expiry policies
- Assign or revoke sudo privileges
- Log actions to a system log file

## Technologies Used

- Bash
- Python (3.x)
- `passwd`, `chage`, `usermod`, `groupadd`, etc.

## Usage

### Bash Script

```bash
sudo ./user_mgmt.sh

### Python Script

sudo python3 user_mgmt.py