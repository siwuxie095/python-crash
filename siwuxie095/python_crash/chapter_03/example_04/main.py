"""

使用列表时避免索引错误


刚开始使用列表时，经常会遇到一种错误。假设你有一个包含三个元素的列表，却要求获取第四个元素：

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])

这将导致索引错误：

Traceback (most recent call last):
  File "motorcycles.py", line 2, in <module>
    print(motorcycles[3])
IndexError: list index out of range

Python试图向你提供位于索引 3 处的元素，但它搜索列表 motorcycles 时，却发现索引 3 处没有
元素。鉴于列表索引差一的特征，这种错误很常见。有些人从 1 开始数，因此以为第三个元素的索引为
3。然而在 Python 中，第三个元素的索引为 2，因为索引是从 0 开始的。

索引错误意味着 Python 在指定索引处找不到元素。程序发生索引错误时，请尝试将指定的索引减 1，
然后再次运行程序，看看结果是否正确。

别忘了，每当需要访问最后一个列表元素时，都可使用索引 -1。这在任何情况下都行之有效，即便你
最后一次访问列表后，其长度发生了变化：

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])

索引 -1 总是返回最后一个列表元素，这里为值 'suzuki'：

'suzuki'

仅当列表为空时，这种访问最后一个元素的方式才会导致错误：

motorcycles = []
print(motorcycles[-1])

列表 motorcycles 不包含任何元素，因此 Python 返回一条索引错误消息：

Traceback (most recent call last):
  File "motorcyles.py", line 3, in <module>
    print(motorcycles[-1])
IndexError: list index out of range

注意：发生索引错误却找不到解决办法时，请尝试将列表或其长度打印出来。列表可能与你以为的截然不同，
在程序对其进行了动态处理时尤其如此。通过查看列表或其包含的元素数，可帮助你找出这种逻辑错误。

"""