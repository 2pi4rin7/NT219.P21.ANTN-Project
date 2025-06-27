def checker(user_attr, policy):
    user_attr = [attr.lower() for attr in user_attr]
    policy = [p.lower() for p in policy]
    
    for attr in user_attr:
        for p in policy:
            if p in attr:
                return True
    
    return False