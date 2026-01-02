class ConversationState:
    def __init__(self):
        self.user_data = {}        # collected info
        self.missing_fields = []   # what we still need
        self.completed = False
