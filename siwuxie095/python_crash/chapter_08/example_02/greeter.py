def greet_user():
    """显示简单的问候语。"""
    print("Hello!")

greet_user()



print("-----")
def greet_user(username):
    """显示简单的问候语。"""
    print(f"Hello, {username.title()}!")

greet_user('jesse')