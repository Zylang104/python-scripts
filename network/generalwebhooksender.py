import requests

def main():
    while True:
        webhook_url = input("welcome to the webhook sender, please enter the webhook url first: ")
        correct_input = input("is the webhook url correct? " + webhook_url + " (yes/no) ")
        
        if correct_input.lower() == "yes":
            break
        else:
            print("Please re-enter the correct webhook URL.")
            continue
    while True:
        try:
            messageinput = input("now enter the message you want to send to the webhook (type 'exit' to quit): ")
            if messageinput.lower() == 'exit':
                print("Exiting sender.")
                break
            send = requests.post(webhook_url, json={"content": messageinput})
            if send.status_code == 204:
                print("Message sent successfully.") 
            else:
                print("Failed to send message. Status code:", send.status_code)
        except requests.exceptions.RequestException as e:
            print(f"Connection Error: Could not send message. Please check the URL or your connection.")
            print("If the URL is wrong, you must restart the script.")
            break

main()