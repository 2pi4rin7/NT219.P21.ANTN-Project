# cloud_storage/server/abac.py
def checker(user_attr, policy):
    """
    Kiểm tra xem thuộc tính của người dùng có thỏa mãn chính sách không
    
    Args:
        user_attr: List các thuộc tính của người dùng
        policy: List các thuộc tính được phép
        
    Returns:
        bool: True nếu thỏa mãn, False nếu không
    """
    # Chuyển đổi tất cả thành chữ thường để so sánh
    user_attr = [attr.lower() for attr in user_attr]
    policy = [p.lower() for p in policy]
    
    # Kiểm tra xem có bất kỳ thuộc tính nào của người dùng nằm trong chính sách không
    for attr in user_attr:
        for p in policy:
            if p in attr:
                return True
    
    return False