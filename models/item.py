class Item:
    def __init__(self, name, description, address, contact, email, item_type):
        self.name = name
        self.description = description
        self.address = address
        self.contact = contact
        self.email = email
        self.item_type = item_type  # 物品类型

    def __str__(self):
        return f"Item(Name: {self.name}, Description: {self.description}, Address: {self.address})"

    def to_dict(self):
        """将物品对象转换为字典"""
        # 检查 item_type 是否有 to_dict 方法，并将其转换成字典
        item_type_dict = None
        if hasattr(self.item_type, 'to_dict'):
            item_type_dict = self.item_type.to_dict()  # 调用 ItemType 的 to_dict 方法
        else:
            item_type_dict = str(self.item_type)  # 如果没有 to_dict 方法，则转换为字符串

        return {
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'contact': self.contact,
            'email': self.email,
            'item_type': item_type_dict  # 这里是 item_type 的字典表示
        }