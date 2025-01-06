class User:
    def __init__(self, username, password, address, contact, role='user', is_verified=False):
        self.username = username
        self.password = password
        self.address = address
        self.contact = contact
        self.role = role  # user or admin
        self.is_verified = is_verified  # 是否已通过管理员审批

    def approve(self):
        self.is_verified = True

    def __str__(self):
        return f"User({self.username}, {self.role})"
