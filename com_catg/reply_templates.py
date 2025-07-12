reply_map = {
    "Praise": "Thank you for your kind words!",
    "Support": "We appreciate your encouragement!",
    "Constructive Criticism": "Thanks for the feedback! We'll work on improving it.",
    "Hate/Abuse": "Please keep the conversation respectful.",
    "Threat": "Your concern has been noted and escalated.",
    "Emotional": "We're glad this resonated with you.",
    "Spam": "This comment has been flagged as spam.",
    "Question/Suggestion": "Thanks for the suggestion! We'll consider it."
}

def get_reply(category):
    return reply_map.get(category, "Thank you for your comment.")
