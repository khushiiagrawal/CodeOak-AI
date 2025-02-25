# WhatsTaskAuto

**WhatsTaskAuto** is a Python project that automates the sending of WhatsApp messages at a scheduled time using the Twilio API. The script takes user input for the recipient's name, WhatsApp number, and message, then sends the message at a specific future time.

## Features:
- Sends WhatsApp messages using Twilio's API.
- Allows scheduling messages by inputting a future date and time.
- Uses environmental variables for Twilio credentials to ensure security.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/WhatsTaskAuto.git
cd WhatsTaskAuto
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install required libraries

```bash
pip install twilio python-dotenv
```

or, if using `requirements.txt`, add:

```
twilio
python-dotenv
```

Then install with:

```bash
pip install -r requirements.txt
```

### 4. Set up the `.env` file

Create a `.env` file in the root directory of the project with the following content:

```
SID=your_twilio_account_sid
TOKEN=your_twilio_auth_token
```

Make sure to replace `your_twilio_account_sid` and `your_twilio_auth_token` with your actual Twilio SID and Token.

---

## Usage

1. Run the script:

```bash
python main.py
```

2. The program will prompt you for:
   - The recipient's name.
   - The recipient's WhatsApp number (with country code).
   - The message you want to send.
   - The date and time to send the message.

3. The script will calculate the delay between the current time and the scheduled time and wait until the time arrives to send the message.

---

## WhatsApp Automation with Twilio

This project demonstrates a simple use case of WhatsApp automation using Twilio's API. You can customize and extend this script to automate messages for different purposes:

- **Reminders**: Set up reminders for tasks or appointments.
- **Notifications**: Send automatic notifications to users at specified times.
- **Marketing**: Send promotional messages to customers based on a schedule.

You can modify the script to loop over a list of recipients, create more complex scheduling, or even integrate it into a larger system to send messages based on external events.

---

## Requirements

- Python 3.x
- Twilio Account
- Twilio WhatsApp Sandbox set up (use Twilio's sandbox number `whatsapp:+14155238886`)





