"""

异常


Python 使用称为异常的特殊对象来管理程序执行期间发生的错误。每当发生让 Python 不知所措的错误时，它都会
创建一个异常对象。如果你编写了处理该异常的代码，程序将继续运行；如果未对异常进行处理，程序将停止并显示
traceback，其中包含有关异常的报告。

异常是使用 try-except 代码块处理的。try-except 代码块让 Python 执行指定的操作，同时告诉 Python
发生异常时怎么办。使用 try-except 代码块时，即便出现异常，程序也将继续运行：显示你编写的友好的错误消息，
而不是令用户迷惑的 traceback。



1、处理 ZeroDivisionError 异常

下面来看一种导致 Python 引发异常的简单错误。你可能知道，不能用数除以 0，但还是让 Python 这样做：

print(5/0)

显然，Python 无法这样做，因此你将看到一个 traceback：

Traceback (most recent call last):
  File "division_calculator.py", line 1, in <module>
    print(5/0)
❶ ZeroDivisionError: division by zero

在上述 traceback 中，❶处指出的错误 ZeroDivisionError 是个异常对象。Python 无法按你的要求做时，
就会创建这种对象。在这种情况下，Python 将停止运行程序，并指出引发了哪种异常，从而可根据这些信息对程序
进行修改。下面来告诉 Python，发生这种错误时怎么办。这样，如果再次发生此类错误，就有备无患了。



2、使用 try-except 代码块

当你认为可能会发生错误时，可编写一个 try-except 代码块来处理可能引发的异常。你让 Python 尝试运行
一些代码，并告诉它如果这些代码引发了指定的异常该怎么办。

处理 ZeroDivisionError 异常的 try-except 代码块类似于下面这样：

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

将导致错误的代码行 print(5/0) 放在一个 try 代码块中。如果 try 代码块中的代码运行起来没有问题，
Python 将跳过 except 代码块；如果 try 代码块中的代码导致了错误，Python 将查找与之匹配的 except
代码块并运行其中的代码。

在本例中，try 代码块中的代码引发了 ZeroDivisionError 异常，因此 Python 查找指出了该怎么办的
except 代码块，并运行其中的代码。这样，用户看到的是一条友好的错误消息，而不是 traceback：

You can't divide by zero!

如果 try-except 代码块后面还有其他代码，程序将接着运行，因为已经告诉了 Python 如何处理这种错误。
下面来看一个捕获错误后程序继续运行的示例。



3、使用异常避免崩溃

发生错误时，如果程序还有工作尚未完成，妥善地处理错误就尤其重要。这种情况经常会出现在要求用户提供输入的程序
中；如果程序能够妥善地处理无效输入，就能再提示用户提供有效输入，而不至于崩溃。

下面来创建一个只执行除法运算的简单计算器：

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
❶    first_number = input("\nFirst number: ")
    if first_number == 'q':
         break
❷    second_number = input("Second number: ")
    if second_number == 'q':
        break
❸    answer = int(first_number) / int(second_number)
    print(answer)

在❶处，程序提示用户输入一个数，并将其赋给变量 first_number。如果用户输入的不是表示退出的 q，就再提示
用户输入一个数，并将其赋给变量 second_number（见❷）。接下来，计算这两个数的商（见❸）。该程序没有采取
任何处理错误的措施，因此在执行除数为 0 的除法运算时，它将崩溃：

Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 5
Second number: 0
Traceback (most recent call last):
  File "division_calculator.py", line 9, in <module>
    answer = int(first_number) / int(second_number)
ZeroDivisionError: division by zero

程序崩溃可不好，但让用户看到 traceback 也不是个好主意。不懂技术的用户会被搞糊涂，怀有恶意的用户还会通过
traceback 获悉你不想他知道的信息。例如，他将知道你的程序文件的名称，还将看到部分不能正确运行的代码。有
时候，训练有素的攻击者可根据这些信息判断出可对你的代码发起什么样的攻击。



4、else 代码块

通过将可能引发错误的代码放在 try-except 代码块中，可提高程序抵御错误的能力。错误是执行除法运算的代码行
导致的，因此需要将它放到 try-except 代码块中。这个示例还包含一个 else 代码块。依赖 try 代码块成功执
行的代码都应放到 else 代码块中：

--snip--
while True:
    --snip--
    if second_number == 'q':
         break
❶    try:
         answer = int(first_number) / int(second_number)
❷    except ZeroDivisionError:
         print("You can't divide by 0!")
❸    else:
        print(answer)

让 Python 尝试执行 try 代码块中的除法运算（见❶），这个代码块只包含可能导致错误的代码。依赖 try 代码
块成功执行的代码都放在 else 代码块中。在本例中，如果除法运算成功，就使用 else 代码块来打印结果（见❸）。

except 代码块告诉 Python，出现 ZeroDivisionError 异常时该如何办（见❷）。如果 try 代码块因除零
错误而失败，就打印一条友好的消息，告诉用户如何避免这种错误。程序继续运行，用户根本看不到 traceback：

Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 5
Second number: 0
You can't divide by 0!

First number: 5
Second number: 2
2.5

First number: q

try-except-else 代码块的工作原理大致如下。Python 尝试执行 try 代码块中的代码，只有可能引发异常的代
码才需要放在 try 语句中。有时候，有一些仅在 try 代码块成功执行时才需要运行的代码，这些代码应放在 else
代码块中。except 代码块告诉 Python，如果尝试运行 try 代码块中的代码时引发了指定的异常该怎么办。

通过预测可能发生错误的代码，可编写健壮的程序。它们即便面临无效数据或缺少资源，也能继续运行，从而抵御无意的
用户错误和恶意的攻击。



5、处理 FileNotFoundError 异常

使用文件时，一种常见的问题是找不到文件：查找的文件可能在其他地方，文件名可能不正确，或者这个文件根本就不
存在。对于所有这些情形，都可使用 try-except 代码块以直观的方式处理。

现在来尝试读取一个不存在的文件。下面的程序尝试读取文件 alice.txt 的内容，但该文件没有存储在 alice.py
所在的目录中：

filename = 'alice.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read()

相比于之前的文件打开方式，这里有两个不同之处。一是使用变量 f 来表示文件对象，这是一种常见的做法。二是给
参数 encoding 指定了值，在系统的默认编码与要读取文件使用的编码不一致时，必须这样做。

Python 无法读取不存在的文件，因此它引发一个异常：

Traceback (most recent call last):
  File "alice.py", line 3, in <module>
    with open(filename, encoding='utf-8') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'

上述 traceback 的最后一行报告了 FileNotFoundError 异常，这是 Python 找不到要打开的文件时创建的
异常。在本例中，这个错误是函数 open() 导致的。因此，要处理这个错误，必须将 try 语句放在包含 open()
的代码行之前：

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
         contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

在本例中，try 代码块引发了 FileNotFoundError 异常，因此 Python 找到与该错误匹配的 except 代码
块，并运行其中的代码。最终的结果是显示一条友好的错误消息，而不是 traceback：

Sorry, the file alice.txt does not exist.

如果文件不存在，这个程序就什么都做不了，错误处理代码也意义不大。下面来扩展这个示例，看看在你使用多个文件
时，异常处理可提供什么样的帮助。



6、分析文本

你可以分析包含整本书的文本文件。很多经典文学作品都是简单以文本文件的形式提供的，因为它们不受版权限制。
这里使用的文本来自古登堡计划，该计划提供了一系列不受版权限制的文学作品。如果你要在编程项目中使用文学
文本，这是一个很不错的资源。

下面来提取童话《爱丽丝漫游奇境记》（Alice in Wonderland）的文本，并尝试计算它包含多少个单词。这
里将使用方法 split()， 它能根据一个字符串创建一个单词列表。

下面是对只包含童话名 "Alice in Wonderland" 的字符串调用方法 split() 的结果：

>>> title = "Alice in Wonderland"
>>> title.split()
['Alice', 'in', 'Wonderland']

方法 split() 以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。结果是一个包含
字符串中所有单词的列表，虽然有些单词可能包含标点。为计算《爱丽丝漫游奇境记》包含多少个单词，这里将
对整篇小说调用 split()，再计算得到的列表包含多少个元素，从而确定整篇童话大致包含多少个单词：

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
         contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # 计算该文件大致包含多少个单词。
❶    words = contents.split()
❷    num_words = len(words)
❸    print(f"The file {filename} has about {num_words} words.")

这里将文件 alice.txt 移到了正确的目录中，让 try 代码块能够成功执行。在❶处，对变量 contents
（它现在是一个长长的字符串，包含童话《爱丽丝漫游奇境记》的全部文本）调用方法 split()，以生成一个
列表，其中包含这部童话中的所有单词。使用 len() 来确定这个列表的长度时，就能知道原始字符串大致包
含多少个单词了（见❷）。在❸处，打印一条消息，指出文件包含多少个单词。这些代码都放在 else 代码块
中，因为仅当 try 代码块成功执行时才执行它们。输出指出了文件 alice.txt 包含多少个单词：

The file alice.txt has about 29465 words.

这个数稍大一点，因为使用的文本文件包含出版商提供的额外信息，但还是成功估算出了童话《爱丽丝漫游奇境
记》的篇幅。



7、使用多个文件

下面多分析几本书。这此之前，先将这个程序的大部分代码移到一个名为 count_words() 的函数中。这样，
对多本书进行分析时将更容易：

def count_words(filename):
❶    \"""计算一个文件大致包含多少个单词。\"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = 'alice.txt'
count_words(filename)

这些代码大多与原来一样，只是移到了函数 count_words() 中，并增加了缩进量。修改程序的同时更新注释
是个不错的习惯，因此这里将注释改成文档字符串，并稍微调整了一下措辞（见❶）。

现在可以编写一个简单的循环，计算要分析的任何文本包含多少个单词了。为此，将要分析的文件的名称存储在
一个列表中，然后对列表中的每个文件调用 count_words()。这里将尝试计算《爱丽丝漫游奇境记》《悉达多》
（Siddhartha）、《白鲸》（Moby Dick）和《小妇人》（Little Women）分别包含多少个单词，它们都
不受版权限制。这里故意没有将 siddhartha.txt 放到 word_count.py 所在的目录中，从而展示该程序
在文件不存在时应对得有多出色：

def count_words(filename):
    --snip--

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

文件 siddhartha.txt 不存在，但这丝毫不影响该程序处理其他文件：

The file alice.txt has about 29465 words.
Sorry, the file siddhartha.txt does not exist.
The file moby_dick.txt has about 215830 words.
The file little_women.txt has about 189079 words.

在本例中，使用 try-except 代码块提供了两个重要的优点：避免用户看到 traceback，以及让程序继续
分析能够找到的其他文件。如果不捕获因找不到 siddhartha.txt 而引发的 FileNotFoundError 异常，
用户将看到完整的 traceback，而程序将在尝试分析《悉达多》后停止运行。它根本不会分析《白鲸》和《小
妇人》。



8、静默失败

在前一个示例中，告诉用户有一个文件找不到。但并非每次捕获到异常都需要告诉用户，有时候你希望程序在发生
异常时保持静默，就像什么都没有发生一样继续运行。要让程序静默失败，可像通常那样编写 try 代码块，但在
except 代码块中明确地告诉 Python 什么都不要做。Python 有一个 pass 语句，可用于让 Python 在
代码块中什么都不要做：

def count_words(filename):
    \"""计算一个文件大致包含多少个单词。\"""
    try:
        --snip--
    except FileNotFoundError:
❶         pass
    else:
        --snip--

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

相比于前一个程序，这个程序唯一的不同之处是❶处的 pass 语句。现在，出现 FileNotFoundError 异常
时，将执行 except 代码块中的代码，但什么都不会发生。这种错误发生时，不会出现 traceback，也没有
任何输出。用户将看到存在的每个文件包含多少个单词，但没有任何迹象表明有一个文件未找到：

The file alice.txt has about 29465 words.
The file moby_dick.txt has about 215830 words.
The file little_women.txt has about 189079 words.

pass 语句还充当了占位符，提醒你在程序的某个地方什么都没有做，并且以后也许要在这里做些什么。例如，
在这个程序中，可能决定将找不到的文件的名称写入文件 missing_files.txt 中。用户看不到这个文件，
但我们可以读取它，进而处理所有找不到文件的问题。



9、决定报告哪些错误

该在什么情况下向用户报告错误？又该在什么情况下静默失败呢？如果用户知道要分析哪些文件，他们可能希望
在有文件却没有分析时出现一条消息来告知原因。如果用户只想看到结果，并不知道要分析哪些文件，可能就无
须在有些文件不存在时告知他们。向用户显示他不想看到的信息可能会降低程序的可用性。Python 的错误处理
结构让你能够细致地控制与用户分享错误信息的程度，要分享多少信息由你决定。

编写得很好且经过详尽测试的代码不容易出现内部错误，如语法或逻辑错误，但只要程序依赖于外部因素，如用
户输入、存在指定的文件、有网络链接，就有可能出现异常。凭借经验可判断该在程序的什么地方包含异常处理
块，以及出现错误时该向用户提供多少相关的信息。

"""