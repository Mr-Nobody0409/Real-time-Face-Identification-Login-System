max_attempts = 100
verify_threshold = 3

class AuthState:
    def __init__(self):
        self.attempts = 0
        self.verify_count = 0
        self.authenticated = False

    def reset(self):
        self.verify_count = 0

    def increment(self):
        self.verify_count += 1

    def success(self):
        return self.verify_count >= verify_threshold
