
---

### `user_mgmt.py` (Python)

```python
#!/usr/bin/env python3

import subprocess
import logging
import os

LOG_FILE = "/var/log/user_mgmt.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

def create_user(username, group, sudo=False):
    try:
        subprocess.run(["groupadd", "-f", group], check=True)
        subprocess.run(["useradd", "-m", "-g", group, username], check=True)
        subprocess.run(["chage", "-M", "90", "-m", "10", "-W", "7", username], check=True)
        if sudo:
            subprocess.run(["usermod", "-aG", "sudo", username], check=True)
        logging.info(f"Created user '{username}' in group '{group}' (sudo={sudo})")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error creating user: {e}")

def delete_user(username):
    try:
        subprocess.run(["deluser", "--remove-home", username], check=True)
        logging.info(f"Deleted user '{username}' and home directory")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error deleting user: {e}")

if __name__ == "__main__":
    print("1. Create User\n2. Delete User")
    choice = input("Enter choice: ")

    if choice == "1":
        user = input("Username: ")
        group = input("Group: ")
        sudo = input("Grant sudo? (y/n): ").lower() == 'y'
        create_user(user, group, sudo)
    elif choice == "2":
        user = input("Username to delete: ")
        delete_user(user)
    else:
        print("Invalid choice")
