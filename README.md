<img width="1024" height="1024" alt="Image" src="https://github.com/user-attachments/assets/e9d94c37-3267-4fc5-b013-a04f343a6f20" />

This Python script extracts all saved WiFi profiles and their passwords on a Windows machine and sends the collected information via email.

---

## Features

- Retrieves all WiFi profiles saved on the system.
- Extracts the WiFi password for each profile.
- Sends the collected information to a specified email address using Gmail SMTP.

---

## Requirements

- Python 3.x
- Windows OS (uses `netsh` command)
- An email account (Gmail recommended) with an **App Password** generated (if using 2FA).

---

## Usage

1. Clone or download the repository.

2. Modify the script:

   - Replace `YOUR_EMAIL@gmail.com` with your sender Gmail address.
   - Replace `YOUR_APP_PASSWORD` with your Gmail app password (not your regular password).

3. Run the script on a Windows machine with Python installed:

```bash
python main.py
```
