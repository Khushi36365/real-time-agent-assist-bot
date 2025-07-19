def detect_intent(transcript):
    # Simple keyword-based intent detection
    intents = {
        "password": "Password Reset",
        "reset": "Password Reset",
        "account": "Account Locked",
        "locked": "Account Locked",
        "billing": "Billing Issue",
        "payment": "Billing Issue",
        "refund": "Refund Request",
        "order": "Order Inquiry",
        "delivery": "Delivery Status"
    }

    for keyword, intent in intents.items():
        if keyword in transcript.lower():
            return intent

    return "General Query"