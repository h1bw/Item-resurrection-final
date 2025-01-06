class ItemType:
    def __init__(self, type_name, attributes):
        self.type_name = type_name
        self.attributes = attributes  # 属性的字典

    def to_dict(self):
        """将 ItemType 对象转换为字典"""
        return {
            'type_name': self.type_name,
            'attributes': self.attributes  # 假设 attributes 已经是一个字典
        }
    
    def __str__(self):
        return f"ItemType({self.type_name}, Attributes: {self.attributes})"
