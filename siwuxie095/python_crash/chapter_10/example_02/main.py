"""

从文件中读取数据


文本文件可存储的数据量多得难以置信：天气数据、交通数据、社会经济数据、文学作品等。每当需要分析或修改存储
在文件中的信息时，读取文件都很有用，对数据分析应用程序来说尤其如此。例如，可以编写一个这样的程序：读取一
个文本文件的内容，重新设置这些数据的格式并将其写入文件，让浏览器能够显示这些内容。

要使用文本文件中的信息，首先需要将信息读取到内存中。为此，你可以一次性读取文件的全部内容，也可以以每次一
行的方式逐步读取。



1、读取整个文件

要读取文件，需要一个包含几行文本的文件。下面首先创建一个文件，它包含精确到小数点后 30 位的圆周率值，且在
小数点后每 10 位处换行：

3.1415926535
  8979323846
  2643383279

要动手尝试后续示例，可在编辑器中输入这些数据行，再将文件保存为 pi_digits.txt。请将该文件保存到程序所在
的目录。

下面的程序打开并读取这个文件，再将其内容显示到屏幕上：

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

在这个程序中，第一行代码做了大量的工作。先来看看函数 open()。要以任何方式使用文件，那怕仅仅是打印其内容，
都得先打开文件，才能访问它。函数 open() 接受一个参数：要打开的文件的名称。Python 在当前执行的文件所在
的目录中查找指定的文件。在本例中，当前运行的是 file_reader.py，因此 Python 在 file_reader.py 所
在的目录中查找 pi_digits.txt。函数 open() 返回一个表示文件的对象。在这里，open('pi_digits.txt')
返回一个表示文件 pi_digits.txt 的对象，Python 将该对象赋给 file_object 供以后使用。

关键字 with 在不再需要访问文件后将其关闭。在这个程序中，注意到这里调用了 open()，但没有调用 close()。
也可以调用 open() 和 close() 来打开和关闭文件，但这样做时，如果程序存在 bug 导致方法 close() 未执
行，文件将不会关闭。这看似微不足道，但未妥善关闭文件可能导致数据丢失或受损。如果在程序中过早调用 close()，
你会发现需要使用文件时它已关闭（无法访问），这会导致更多的错误。并非在任何情况下都能轻松确定关闭文件的恰当
时机，但通过使用前面所示的结构，可让 Python 去确定：你只管打开文件，并在需要时使用它，Python 自会在合适
的时候自动将其关闭。

有了表示 pi_digits.txt 的文件对象后，使用方法 read()（前述程序的第二行）读取这个文件的全部内容，并将
其作为一个长长的字符 串赋给变量 contents。这样，通过打印 contents 的值，就可将这个文本文件的全部内容
显示出来：

3.1415926535
  8979323846
  2643383279

相比于原始文件，该输出唯一不同的地方是末尾多了一个空行。为何会多出这个空行呢？因为 read() 到达文件末尾
时返回一个空字符串，而将这个空字符串显示出来时就是一个空行。要删除多出来的空行，可在函数调用 print()
中使用 rstrip()：

with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents.rstrip())

之前说过，Python 方法 rstrip() 删除字符串末尾的空白。现在，输出与原始文件的内容完全相同：

3.1415926535
  8979323846
  2643383279



2、文件路径

将类似于 pi_digits.txt 的简单文件名传递给函数 open() 时，Python 将在当前执行的文件（即 .py 程序
文件）所在的目录中查找。

根据你组织文件的方式，有时可能要打开不在程序文件所属目录中的文件。例如，你可能将程序文件存储在了文件夹
python_work 中，而该文件夹中有一个名为 text_files 的文件夹用于存储程序文件操作的文本文件。虽然文
件夹 text_files 包含在文件夹 python_work 中，但仅向 open() 传递位于前者中的文件名称也不可行，
因为 Python 只在文件夹 python_work 中查找，而不会在其子文件夹 text_files 中查找。要让 Python
打开不与程序文件位于同一个目录中的文件，需要提供文件路径，让 Python 到系统的特定位置去查找。

由于文件夹 text_files 位于文件夹 python_work 中，可以使用相对文件路径来打开其中的文件。相对文件
路径让 Python 到指定的位置去查找，而该位置是相对于当前运行的程序所在目录的。例如，可这样编写代码：

with open('text_files/filename.txt') as file_object:

这行代码让 Python 到文件夹 python_work 下的文件夹 text_files 中去查找指定的 .txt 文件。

注意：显示文件路径时，Windows 系统使用反斜杠（\）而不是斜杠（/），但在代码中依然可以使用斜杠。

还可以将文件在计算机中的准确位置告诉 Python，这样就不用关心当前运行的程序存储在什么地方了。这称为绝对
文件路径。在相对路径行不通时，可使用绝对路径。例如，如果 text_files 并不在文件夹 python_work 中，
而在文件夹 other_files 中，则向 open() 传递路径 'text_files/filename.txt' 行不通，因为
Python 只在文件夹 python_work 中查找该位置。为明确指出希望 Python 到哪里去查找，需要提供完整的
路径。

绝对路径通常比相对路径长，因此将其赋给一个变量，再将该变量传递给 open() 会有所帮助：

file_path = '/home/ehmatthes/other_files/text_files/_filename_.txt'
with open(file_path) as file_object:

通过使用绝对路径，可读取系统中任何地方的文件。就目前而言，最简单的做法是，要么将数据文件存储在程序文件
所在的目录，要么将其存储在程序文件所在目录下的一个文件夹（如 text_files）中。

注意：如果在文件路径中直接使用反斜杠，将引发错误，因为反斜杠用于对字符串中的字符进行转义。例如，对于路
径 "C:\path\to\file.txt" ，其中的 \t 将被解读为制表符。如果一定要使用反斜杠，可对路径中的每个反
斜杠都进行转义，如 "C:\\path\\to\\file.txt"。



3、逐行读取

读取文件时，常常需要检查其中的每一行：可能要在文件中查找特定的信息，或者要以某种方式修改文件中的文本。
例如，你可能要遍历一个包含天气数据的文件，并使用天气描述中包含 sunny 字样的行。在新闻报道中，你可能
会查找包含标签 <headline> 的行，并按特定的格式设置它。

要以每次一行的方式检查文件，可对文件对象使用 for 循环：

❶ filename = 'pi_digits.txt'

❷ with open(filename) as file_object:
❸   for line in file_object:
        print(line)

在❶处，将要读取的文件的名称赋给变量 filename。这是使用文件时的一种常见做法。变量 filename 表示的
并非实际文件——它只是一个让 Python 知道到哪里去查找文件的字符串，因此可以轻松地将 'pi_digits.txt'
替换为要使用的另一个文件的名称。调用 open() 后，将一个表示文件及其内容的对象赋给了变量 file_object
（见❷）。这里也使用了关键字 with，让 Python 负责妥善地打开和关闭文件。为查看文件的内容，通过对文件
对象执行循环来遍历文件中的每一行（见❸）。

打印每一行时，发现空白行更多了：

3.1415926535

  8979323846

  2643383279

为何会出现这些空白行呢？因为在这个文件中，每行的末尾都有一个看不见的换行符，而函数调用 print() 也会
加上一个换行符，因此每行末尾都有两个换行符：一个来自文件，另一个来自函数调用 print()。要消除这些多余
的空白行，可在函数调用 print() 中使用 rstrip()：

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

现在，输出又与文件内容完全相同了：

3.1415926535
  8979323846
  2643383279



4、创建一个包含文件各行内容的列表

使用关键字 with 时，open() 返回的文件对象只在 with 代码块内可用。如果要在 with 代码块外访问文件的
内容，可在 with 代码块内将文件的各行存储在一个列表中，并在 with 代码块外使用该列表：可以立即处理文件
的各个部分，也可以推迟到程序后面再处理。

下面的示例在 with 代码块中将文件 pi_digits.txt 的各行存储在一个列表中，再在 with 代码块外打印：

filename = 'pi_digits.txt'

with open(filename) as file_object:
❶    lines = file_object.readlines()

❷ for line in lines:
    print(line.rstrip())

❶处的方法 readlines() 从文件中读取每一行，并将其存储在一个列表中。接下来，该列表被赋给变量 lines。
在 with 代码块外，依然可使用这个变量。在❷处，使用一个简单的 for 循环来打印 lines 中的各行。因为列
表 lines 的每个元素都对应于文件中的一行，所以输出与文件内容完全一致。



5、使用文件的内容

将文件读取到内存中后，就能以任何方式使用这些数据了。下面以简单的方式使用圆周率的值。首先，创建一个字符
串，它包含文件中存储的所有数字，且没有任何空格：

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

❶ pi_string = ''
❷ for line in lines:
    pi_string += line.rstrip()

❸ print(pi_string)
print(len(pi_string))

像前一个示例一样，首先打开文件，并将其中所有的行都存储在一个列表中。在❶处，创建了一个变量 pi_string，
用于指向圆周率的值。接下来，使用一个循环将各行加入 pi_string，并删除每行末尾的换行符（见❷）。在❸处，
打印这个字符串及其长度：

3.1415926535  8979323846  2643383279
36

变量 pi_string 指向的字符串包含原来位于每行左边的空格，为删除这些空格，可使用 strip() 而非 rstrip()：

--snip--
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

这样就获得了一个字符串，其中包含准确到 30 位小数的圆周率值。这个字符串长 32 字符，因为它还包含整数部分
的 3 和小数点：

3.141592653589793238462643383279
32

注意：读取文本文件时，Python 将其中的所有文本都解读为字符串。如果读取的是数，并要将其作为数值使用，就
必须使用函数 int() 将其转换为整数或使用函数 float() 将其转换为浮点数。



6、包含一百万位的大型文件

前面分析的都是一个只有三行的文本文件，但这些代码示例也可处理大得多的文件。如果有一个文本文件，其中包含
精确到小数点后 1 000 000 位而不是 30 位的圆周率值，也可创建一个包含所有这些数字的字符串。为此，无须
对前面的程序做任何修改，只要将这个文件传递给它即可。在这里，只打印到小数点后 50 位，以免终端为显示全部
1 000 000 位而不断滚动：

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

输出表明，创建的字符串确实包含精确到小数点后 1 000 000 位的圆周率值：

3.14159265358979323846264338327950288419716939937510...
1000002

对于可处理的数据量，Python 没有任何限制。只要系统的内存足够多，你想处理多少数据都可以。



7、圆周率值中包含你的生日吗

一直想知道自己的生日是否包含在圆周率值中。下面来扩展刚才编写的程序，以确定某个人的生日是否包含在圆周率
值的前 1 000 000 位中。为此，可将生日表示为一个由数字组成的字符串，再检查这个字符串是否包含在 pi_string
中：

--snip--
for line in lines:
    pi_string += line.strip()

❶ birthday = input("Enter your birthday, in the form mmddyy: ")
❷ if birthday in pi_string:
         print("Your birthday appears in the first million digits of pi!")
  else:
        print("Your birthday does not appear in the first million digits of pi.")

在❶处，提示用户输入生日。在❷处，检查这个字符串是否包含在 pi_string 中。下面来运行一下这个程序：

Enter your birthdate, in the form mmddyy: 120372
Your birthday appears in the first million digits of pi!

生日确实出现在了圆周率值中！读取文件的内容后，能以你能想到的任何方式对其进行分析。

"""