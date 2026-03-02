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
```
```bash
webhook-repo/
├─ app.py            # Flask webhook server
├─ requirements.txt  # Python dependencies
└─ README.md         # Project documentation
```
Notes

Test events can be sent without real commits.

Make sure Flask is running before sending events.

MongoDB Atlas must allow your IP (or use 0.0.0.0/0 for testing).

This setup is ready for assignment submission.

🔹 References

Flask Documentation

MongoDB Atlas

ngrok


