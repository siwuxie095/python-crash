"""

传递列表


你经常会发现，向函数传递列表很有用，其中包含的可能是名字、数或更复杂的对象（如字典）。将列表传递给
函数后，函数就能直接访问其内容。下面使用函数来提高处理列表的效率。

假设有一个用户列表，要问候其中的每位用户。下面的示例将包含名字的列表传递给一个名为 greet_users()
的函数，这个函数问候列表中的每个人：

def greet_users(names):
    \"""向列表中的每位用户发出简单的问候。\"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

❶ usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

这里将 greet_users() 定义为接受一个名字列表，并将其赋给形参 names。这个函数遍历收到的列表，并
对其中的每位用户打印一条问候语。❶处定义了一个用户列表 usernames，然后调用 greet_users() 并将
该列表传递给它：

Hello, Hannah!
Hello, Ty!
Hello, Margot!

输出完全符合预期。每位用户都看到了一条个性化的问候语。每当需要问候一组用户时，都可调用这个函数。



1、在函数中修改列表

将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的，这让你能够
高效地处理大量数据。

来看一家为用户提交的设计制作 3D 打印模型的公司。需要打印的设计存储在一个列表中，打印后将移到另一
个列表中。下面是在不使用函数的情况下模拟这个过程的代码：

# 首先创建一个列表，其中包含一些要打印的设计。
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止。
# 打印每个设计后，都将其移到列表completed_models中。
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# 显示打印好的所有模型。
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

这个程序首先创建一个需要打印的设计列表，以及一个名 completed_models 的空列表，每个设计打印后都
将移到其中。只要列表 unprinted_designs 中还有设计，while 循环就模拟打印设计的过程：从该列表
末尾删除一个设计，将其赋给变量 current_design，并显示一条消息指出正在打印当前的设计，然后将该
设计加入到列表 completed_models 中。循环结束后，显示已打印的所有设计：

Printing model: dodecahedron
Printing model: robot pendant
Printing model: phone case

The following models have been printed:
dodecahedron
robot pendant
phone case

为重新组织这些代码，可编写两个函数，每个都做一件具体的工作。大部分代码与原来相同，只是效率更高。第
一个函数负责处理打印设计的工作，第二个概述打印了哪些设计：

❶ def print_models(unprinted_designs, completed_models):
    \"""
    模拟打印每个设计，直到没有未打印的设计为止。
    打印每个设计后，都将其移到列表completed_models中。
    \"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

❷ def show_completed_models(completed_models):
    \"""显示打印好的所有模型。\"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

❶处定义了函数 print_models()，它包含两个形参：一个需要打印的设计列表和一个打印好的模型列表。给定
这两个列表，该函数模拟打印每个设计的过程：将设计逐个从未打印的设计列表中取出，并加入打印好的模型列表
中。❷处定义了函数 show_completed_models()，它包含一个形参：打印好的模型列表。给定这个列表，函数
show_completed_models() 显示打印出来的每个模型的名称。

这个程序的输出与未使用函数的版本相同，但组织更为有序。完成大部分工作的代码都移到了两个函数中，让主程序
更容易理解。只要看看主程序，就会发现这个程序的功能清晰得多：

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

这里创建了一个未打印的设计列表，还创建了一个空列表，用于存储打印好的模型。接下来，由于已经定义了两个
函数，只需调用它们并传入正确的实参即可。这里调用 print_models() 并向它传递两个列表。像预期一样，
print_models() 模拟打印设计的过程。接下来，调用 show_completed_models()，并将打印好的模型
列表传递给它，让其能够指出打印了哪些模型。描述性的函数名让别人阅读这些代码时也能明白，尽管没有任何
注释。

相比于没有使用函数的版本，这个程序更容易扩展和维护。如果以后需要打印其他设计，只需再次调用对应函数
print_models() 即可。如果发现需要对打印代码进行修改，只需修改这些代码一次，就能影响所有调用该
函数的地方。与必须分别修改程序的多个地方相比，这种修改的效率更高。

该程序还演示了这样一种理念：每个函数都应只负责一项具体的工作。第一个函数打印每个设计，第二个显示打印
好的模型。这优于使用一个函数来完成这两项工作。编写函数时，如果发现它执行的任务太多，请尝试将这些代码
划分到两个函数中。别忘了，总是可以在一个函数中调用另一个函数，这有助于将复杂的任务划分成一系列步骤。



2、禁止函数修改列表

有时候，需要禁止函数修改列表。例如，假设像前一个示例那样，你有一个未打印的设计列表，并编写了一个函数
将这些设计移到打印好的模型列表中。你可能会做出这样的决定：即便打印好了所有设计，也要保留原来的未打印
的设计列表，以供备案。但由于你将所有的设计都移出了 unprinted_designs，这个列表变成了空的，原来的
列表没有了。为解决这个问题，可向函数传递列表的副本而非原件。这样，函数所做的任何修改都只影响副本，而
原件丝毫不受影响。

要将列表的副本传递给函数，可以像下面这样做：

function_name(list_name_[:])

切片表示法 [:] 创建列表的副本。在 printing_models.py 中，如果不想清空未打印的设计列表，可像下面
这样调用 print_models()：

print_models(unprinted_designs[:], completed_models)

这样一来函数 print_models() 依然能够完成工作，因为它获得了所有未打印的设计的名称，但使用的是列表
unprinted_designs 的副本，而不是列表 unprinted_designs 本身。对于列表 completed_models
也像以前一样，将包含打印好的模型的名称，但函数所做的修改不会影响到列表 unprinted_designs。

虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分的理由，否则还是应该将原始列表传递给函数。
这是因为让函数使用现成的列表可避免花时间和内存创建副本，从而提高效率，在处理大型列表时尤其如此。

"""