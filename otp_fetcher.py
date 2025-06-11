import requests
import time

BASE_URL = "https://www.1secmail.com/api/v1/"

# এখানে তুমি যেসব মেইল ইউজ করেছিলে
emails = [
    "pipegi6081@nobitcoin.net",
    "remen18023@byorby.com",
    "livayir992@aramask.com",
    "pajipuxu@hexi.pics"
]

def get_messages(login, domain):
    url = f"{BASE_URL}?action=getMessages&login={login}&domain={domain}"
    return requests.get(url).json()

def read_message(login, domain, message_id):
    url = f"{BASE_URL}?action=readMessage&login={login}&domain={domain}&id={message_id}"
    return requests.get(url).json()

def check_all_inboxes():
    print("[*] Checking inboxes...\n")
    for email in emails:
        login, domain = email.split("@")
        messages = get_messages(login, domain)
        print(f"[📨] Inbox for {email} - {len(messages)} message(s)")

        for msg in messages:
            print(f"\n📧 From: {msg['from']}")
            print(f"📌 Subject: {msg['subject']}")
            print(f"🕒 Date: {msg['date']}")
            content = read_message(login, domain, msg['id'])
            print(f"📄 Body:\n{content.get('textBody', '[No Text]')}")
            print("-" * 50)

if __name__ == "__main__":
    while True:
        check_all_inboxes()
        print("\n⏳ Waiting 15 seconds before next check...\n")
        time.sleep(15)
