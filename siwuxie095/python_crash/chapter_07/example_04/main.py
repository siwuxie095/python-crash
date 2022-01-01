"""

使用 while 循环处理列表和字典


到目前为止，每次都只处理了一项用户信息：获取用户的输入，再将输入打印出来或做出应答；循环再次运行时，
获悉另一个输入值并做出响应。然而，要记录大量的用户和信息，需要在 while 循环中使用列表和字典。

for 循环是一种遍历列表的有效方式，但不应在 for 循环中修改列表，否则将导致 Python 难以跟踪其中
的元素。要在遍历列表的同时对其进行修改，可使用 while 循环。通过将 while 循环同列表和字典结合起
来使用，可收集、存储并组织大量输入，供以后查看和显示。



1、在列表之间移动元素

假设有一个列表包含新注册但还未验证的网站用户。验证这些用户后，如何将他们移到另一个已验证用户列表中
呢？一种办法是使用一个 while 循环，在验证用户的同时将其从未验证用户列表中提取出来，再将其加入另一
个已验证用户列表中。代码可能类似于下面这样：

# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表。
❶ unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止。
# 将每个经过验证的用户都移到已验证用户列表中。
❷ while unconfirmed_users:
❸    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
❹    confirmed_users.append(current_user)

# 显示所有已验证的用户。
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

首先创建一个未验证用户列表（见❶），其中包含用户 Alice、Brian 和 Candace，还创建了一个空列表，
用于存储已验证的用户。❷处的 while 循环将不断运行，直到列表 unconfirmed_users 变成空的。在
此循环中，❸处的方法 pop() 以每次一个的方式从列表 unconfirmed_users 末尾删除未验证的用户。
由于 Candace 位于列表 unconfirmed_users 末尾，其名字将首先被删除、赋给变量 current_user
并加入列表 confirmed_users 中（见❹）。接下来是 Brian，然后是 Alice。

为模拟用户验证过程，这里打印一条验证消息并将用户加入已验证用户列表中。未验证用户列表越来越短，而
已验证用户列表越来越长。未验证用户列表为空后结束循环，再打印已验证用户列表：

Verifying user: Candace
Verifying user: Brian
Verifying user: Alice

The following users have been confirmed:
Candace
Brian
Alice



2、删除为特定值的所有列表元素

之前曾使用函数 remove() 来删除列表中的特定值。这之所以可行，是因为要删除的值只在列表中出现一次。
如果要删除列表中所有为特定值的元素，该怎么办呢？

假设你有一个宠物列表，其中包含多个值为 'cat' 的元素。要删除所有这些元素，可不断运行一个 while
循环，直到列表中不再包含值 'cat' ，如下所示：

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

首先创建一个列表，其中包含多个值为 'cat' 的元素。打印这个列表后，Python 进入 while 循环，因
为它发现 'cat' 在列表中至少出现了一次。进入该循环后，Python 删除第一个 'cat' 并返回到 while
代码行，然后发现 'cat' 还包含在列表中，因此再次进入循环。它不断删除 'cat'，直到这个值不再包含
在列表中，然后退出循环并再次打印列表：

['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']



3、使用用户输入来填充字典

可使用 while 循环提示用户输入任意多的信息。下面创建一个调查程序，其中的循环每次执行时都提示输入
被调查者的名字和回答。这里将收集的数据存储在一个字典中，以便将回答同被调查者关联起来：

responses = {}

# 设置一个标志，指出调查是否继续。
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答。
❶    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 将回答存储在字典中。
❷    responses[name] = response

    # 看看是否还有人要参与调查。
❸    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

 # 调查结束，显示结果。
print("\n--- Poll Results ---")
❹ for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

这个程序首先定义了一个空字典（responses），并设置了一个标志（polling_active）用于指出调查是否
继续。只要 polling_active 为 True，Python 就运行 while 循环中的代码。

在这个循环中，提示用户输入其名字及其喜欢爬哪座山（见❶）。将这些信息存储在字典 responses 中（见❷），
然后询问用户是否继续调查（见❸）。如果用户输入 yes，程序将再次进入 while 循环；如果用户输入 no，
标志 polling_active 将被设置为 False，而 while 循环将就此结束。最后一个代码块（见❹）显示调查
结果。

如果运行这个程序，并输入一些名字和回答，输出将类似于下面这样：

What is your name? Eric
Which mountain would you like to climb someday?
Denali Would you like to let another person respond? (yes/ no) yes

What is your name? Lynn
Which mountain would you like to climb someday?
Devil's Thumb Would you like to let another person respond? (yes/ no) no

--- Poll Results ---
Eric would like to climb Denali.
Lynn would like to climb Devil's Thumb.

"""