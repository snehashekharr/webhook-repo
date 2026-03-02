# GitHub Webhook Receiver (Flask + MongoDB)

## 🔹 Purpose
This Flask application **receives GitHub webhook events** (push events) and stores them in **MongoDB Atlas**.  
It allows testing webhook integrations locally via **ngrok** and provides a full end-to-end demonstration.

---

## 🔹 Features
- Receives JSON payloads from GitHub webhooks.
- Inserts each payload into a MongoDB Atlas collection.
- Prints received events in the Flask console for verification.
- Supports local testing using ngrok.
- Includes timestamp (`received_at`) for each event.

---

## 🔹 Requirements
- Python 3.10+
- Flask
- pymongo
- ngrok (for local testing)

Install dependencies:
```bash
pip install -r requirements.txt
