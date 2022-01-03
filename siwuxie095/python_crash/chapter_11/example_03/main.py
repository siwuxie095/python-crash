"""

测试类


在之前，你编写了针对单个函数的测试，下面来编写针对类的测试。很多程序中都会用到类，因此证明你的类能够
正确工作大有裨益。如果针对类的测试通过了，你就能确信对类所做的改进没有意外地破坏其原有的行为。



1、各种断言方法

Python 在 unittest.TestCase 类中提供了很多断言方法。前面说过，断言方法检查你认为应该满足的条件
是否确实满足。如果该条件确实满足，你对程序行为的假设就得到了确认，可以确信其中没有错误。如果你认为应
该满足的条件实际上并不满足，Python 将引发异常。

下面描述了 6 个常用的断言方法。使用这些方法可核实返回的值等于或不等于预期的值，返回的值为 True 或
False，以及返回的值在列表中或不在列表中。只能在继承 unittest.TestCase 的类中使用这些方法，随后
来看看如何在测试类时使用其中之一。

unittest 模块中的断言方法（方法和用途）：
（1）assertEqual(a, b)：核实 a == b
（2）assertNotEqual(a, b)：核实 a != b
（3）assertTrue(x)：核实 x 为 True
（4）assertFalse(x)：核实 x 为 False
（5）assertIn(item , list)：核实 item 在 list 中
（6）assertNotIn(item , list)：核实 item 不在 list 中



2、一个要测试的类

类的测试与函数的测试相似，你所做的大部分工作是测试类中方法的行为。不过还是存在一些不同之处，下面编写
一个要测试的类。来看一个帮助管理匿名调查的类：

class AnonymousSurvey:
    \"""收集匿名调查问卷的答案。\"""

    def __init__(self, question):
        \"""存储一个问题，并为存储答案做准备。\"""
        self.question = question
        self.responses = []

    def show_question(self):
        \"""显示调查问卷。\"""
        print(self.question)

    def store_response(self, new_response):
        \"""存储单份调查答卷。\"""
        self.responses.append(new_response)

    def show_results(self):
        \"""显示收集到的所有答卷。\"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

这个类首先存储了一个调查问题（见❶），并创建了一个空列表，用于存储答案。这个类包含打印调查问题的方法
（见❷），在答案列表中添加新答案的方法（见❸），以及将存储在列表中的答案都打印出来的方法（见❹）。要
创建该类的实例，只需提供一个问题即可。有了表示调查的实例后，就可使用 show_question() 来显示其中
的问题，使用 store_response() 来存储答案并使用 show_results() 来显示调查结果。

为证明 AnonymousSurvey 类能够正确工作，编写一个使用它的程序：

from survey import AnonymousSurvey

# 定义一个问题，并创建一个调查。
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案。 my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# 显示调查结果。
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

这个程序定义了一个问题（"What language did you first learn to speak? "），并使用该问题创
建了一个 AnonymousSurvey 对象。接下来，这个程序调用 show_question() 来显示问题，并提示用户
输入答案。

在收到每个答案的同时将其存储起来。用户输入所有答案（输入 q 要求退出）后，调用 show_results()
来打印调查结果：

What language did you first learn to speak?
Enter 'q' at any time to quit.

Language: English
Language: Spanish
Language: English
Language: Mandarin
Language: q

Thank you to everyone who participated in the survey!
Survey results:
- English
- Spanish
- English
- Mandarin

AnonymousSurvey 类可用于进行简单的匿名调查。假设将它放在了模块 survey 中，并想进行改进：让每位
用户都可输入多个答案；编写一个方法，只列出不同的答案并指出每个答案出现了多少次；再编写一个类，用于管
理非匿名调查。

进行上述修改存在风险，可能影响 AnonymousSurvey 类的当前行为。例如，允许每位用户输入多个答案时，
可能会不小心修改处理单个答案的方式。要确认在开发这个模块时没有破坏既有行为，可以编写针对这个类的测试。



3、测试 AnonymousSurvey 类

下面来编写一个测试，对 AnonymousSurvey 类的行为的一个方面进行验证：如果用户面对调查问题只提供一个
答案，这个答案也能被妥善地存储。为此，将在这个答案被存储后，使用方法 assertIn() 来核实它确实在答案
列表中：

import unittest
from survey import AnonymousSurvey

❶ class TestAnonymousSurvey(unittest.TestCase):
    \"""针对AnonymousSurvey类的测试。\"""

❷    def test_store_single_response(self):
        \"""测试单个答案会被妥善地存储。\"""
        question = "What language did you first learn to speak?"
❸        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
❹        self.assertIn('English', my_survey.responses)

if __name__ == '__main__':
    unittest.main()

首先导入模块 unittest 和要测试的类 AnonymousSurvey。将测试用例命名为 TestAnonymousSurvey，
它也继承了 unittest.TestCase（见❶）。第一个测试方法验证：调查问题的单个答案被存储后，会包含在
调查结果列表中。对于这个方法，一个不错的描述性名称是 test_store_single_response()（见❷）。
如果这个测试未通过，就能通过输出中的方法名得知，在存储单个调查答案方面存在问题。

要测试类的行为，需要创建其实例。在❸处，使用问题 "What language did you first learn to
speak?" 创建一个名为 my_survey 的实例，然后使用方法 store_response() 存储单个答案 English。
接下来，检查 English 是否包含在列表 my_survey.responses 中，以核实这个答案是否被妥善地存储了
（见❹）。

当运行 test_survey.py 时，测试通过了：

.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK

这很好，但只能收集一个答案的调查用途不大。下面来核实当用户提供三个答案时，它们也将被妥善地存储。为此，
在 TestAnonymousSurvey 中再添加一个方法：

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    \"""针对AnonymousSurvey类的测试。\"""

    def test_store_single_response(self):
        --snip--

    def test_store_three_responses(self):
        \"""测试三个答案会被妥善地存储。\"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
❶        responses = ['English','Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

❷        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()

这里将该方法命名为 test_store_three_responses()，并像对 test_store_single_response()
所做的一样，在其中创建一个调查对象。定义一个包含三个不同答案的列表（见❶），再对其中每个答案调用
store_response()。存储这些答案后，使用一个循环来确认每个答案都包含在 my_survey.responses
中（见❷）。

再次运行 test_survey.py 时，两个测试（针对单个答案的测试和针对三个答案的测试）都通过了：

..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

前述做法的效果很好，但这些测试有些重复的地方。下面使用 unittest 的另一项功能来提高其效率。



4、方法 setUp()

在前面的 test_survey.py 中，在每个测试方法中都创建了一个 AnonymousSurvey 实例，并在每个方法
中都创建了答案。unittest.TestCase 类包含的方法 setUp() 使得只需创建这些对象一次，就能在每个
测试方法中使用。如果在 TestCase 类中包含了方法 setUp()，Python 将先运行它，再运行各个以 test_
打头的方法。这样，在你编写的每个测试方法中，都可使用在方法 setUp() 中创建的对象。

下面使用 setUp() 来创建一个调查对象和一组答案，供方法 test_store_single_response() 和
test_store_three_responses() 使用：

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    \"""针对AnonymousSurvey类的测试。\"""

    def setUp(self):
        \"""
        创建一个调查对象和一组答案，供使用的测试方法使用。
        \"""
        question = "What language did you first learn to speak?"
❶        self.my_survey = AnonymousSurvey(question)
❷        self.responses = ['English','Spanish', 'Mandarin']

    def test_store_single_response(self):
        \"""测试单个答案会被妥善地存储。\"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        \"""测试三个答案会被妥善地存储。\"""
        question = "What language did you first learn to speak?"
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()

方法setUp() 做了两件事情：创建一个调查对象（见❶），以及创建一个答案列表（见❷）。存储这两样东西的
变量名包含前缀 self（即存储在属性中），因此可在这个类的任何地方使用。这让两个测试方法都更简单，因为
它们都不用创建调查对象和答案了。方法 test_store_single_response() 核实 self.responses 中
的第一个答案 self.responses[0] 被妥善地存储，而方法 test_store_three_response() 核实
self.responses 中的全部三个答案都被妥善地存储。

再次运行 test_survey.py 时，这两个测试也都通过了。如果要扩展 AnonymousSurvey，使其允许每位
用户输入多个答案，这些测试将很有用。修改代码以接受多个答案后，可运行这些测试，确认存储单个答案或一
系列答案的行为未受影响。

测试自己编写的类时，方法 setUp() 让测试方法编写起来更容易：可在 setUp() 方法中创建一系列实例并
设置其属性，再在测试方法中直接使用这些实例。相比于在每个测试方法中都创建实例并设置其属性，这要容易
得多。

注意：运行测试用例时，每完成一个单元测试，Python 都打印一个字符：测试通过时打印一个句点，测试引发
错误时打印一个 E，而测试导致断言失败时则打印一个 F。这就是你运行测试用例时，在输出的第一行中看到的
句点和字符数量各不相同的原因。如果测试用例包含很多单元测试，需要运行很长时间，就可通过观察这些结果
来获悉有多少个测试通过了。

"""