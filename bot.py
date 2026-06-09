import os
import time
import requests
from bs4 import BeautifulSoup

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = "1190315327"

URL = "https://vgik.info/abiturient/higher/spetsialitet/aktyerskiy-fakultet/"

last_hash = None

def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": text
        },
        timeout=30
    )

while True:
    try:
        html = requests.get(URL, timeout=30).text

        soup = BeautifulSoup(html, "html.parser")

        text = soup.get_text(" ", strip=True)

        current_hash = hash(text)

        if last_hash is None:
            last_hash = current_hash

        elif current_hash != last_hash:
            send_message(
                "⚡ Обнаружены изменения на странице актерского факультета ВГИК. Проверь записи к Мерзликину и Федорову."
            )
            last_hash = current_hash

    except Exception as e:
        print(e)

    time.sleep(300)
