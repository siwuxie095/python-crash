"""

使用 Web API


Web API 是网站的一部分，用于与使用具体 URL 请求特定信息的程序交互。这种请求称为 API 调用。请求的数据将以
易于处理的格式（如 JSON 或 CSV）返回。依赖于外部数据源的大多数应用程序依赖于 API 调用，如集成社交媒体网站
的应用程序。



1、Git 和 GitHub

这里的可视化基于来自 GitHub 的信息，这是一个让程序员能够协作开发项目的网站。这里将使用 GitHub 的 API 来
请求有关该网站中 Python 项目的信息，再使用 Plotly 生成交互式可视化图表，呈现这些项目的受欢迎程度。

GitHub 的名字源自 Git，后者是一个分布式版本控制系统，帮助人们管理为项目所做的工作，避免一个人所做的修改影
响其他人所做的修改。在项目中实现新功能时，Git 跟踪你对每个文件所做的修改。确定代码可行后，你提交所做的修改，
而 Git 将记录项目最新的状态。如果犯了错，想撤销所做的修改，你可以轻松地返回到以前的任何可行状态。GitHub
上的项目都存储在仓库中，后者包含与项目相关联的一切：代码、项目参与者的信息、问题或 bug 报告，等等。

GitHub 用户可以给喜欢的项目加星（star）以表示支持，还可以跟踪自己可能想使用的项目。在这里，将编写一个程序，
自动下载 GitHub 上星级最高的 Python 项目的信息，并对这些信息进行可视化。



2、使用 API 调用请求数据

GitHub 的 API 让你能够通过 API 调用来请求各种信息。要知道 API 调用是什么样的，请在浏览器的地址栏中输入
如下地址并按回车键：

https://api.github.com/search/repositories?q=language:python&sort=stars

这个调用返回 GitHub 当前托管了多少个 Python 项目，以及有关最受欢迎的 Python 仓库的信息。下面来仔细研究
这个调用。开头的 https://api.github.com/ 将请求发送到 GitHub 网站中响应 API 调用的部分，接下来的
search/repositories 让 API 搜索 GitHub 上的所有仓库。

repositories 后面的问号指出需要传递一个实参。q 表示查询，而等号（=）让你能够开始指定查询。这里使用 lan-
guage:python 指出只想获取主要语言为 Python 的仓库的信息。最后的 &sort=stars 指定将项目按星级排序。

下面显示了响应的前几行。

{
❶  "total_count": 8417607,
❷   "incomplete_results": true,
❸  "items": [
    {
      "id": 54346799,
      "node_id": "MDEwOlJlcG9zaXRvcnk1NDM0Njc5OQ==",
      "name": "public-apis",
      "full_name": "public-apis/public-apis",
--snip--

从响应可知，该 URL 并不适合人工输入，因为它采用了适合程序处理的格式。到目前为止（2022/01/16），GitHub
总共有 8 417 607 个 Python 项目（见❶）。"incomplete_results" 的值为 false（见❷），由此知道请求
是成功的（并非不完整的）。倘若 GitHub 无法处理该 API，此处返回的值将为 true。接下来的列表中显示了返回的
"items"，其中包含 GitHub 上最受欢迎的 Python 项目的详细信息（见❸）。



3、安装 Requests

Requests 包让 Python 程序能够轻松地向网站请求信息并检查返回的响应。要安装 Requests，可使用 pip：

python -m pip install --user requests

这个命令让 Python 运行模块 pip，并在当前用户的 Python 安装中添加 Requests 包。如果你运行程序或安装包
时使用的是命令 python3 或其他命令，请务必在这里使用同样的命令。如下：

python3 -m pip install --user requests

注意：如果该命令在 macOS 系统上不管用，可以尝试删除标志 --user 再次运行。



4、处理 API 响应

下面来编写一个程序，它自动执行 API 调用并处理结果，以找出 GitHub 上星级最高的 Python 项目：

❶ import requests

# 执行API调用并存储响应。
❷ url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
❸ headers = {'Accept': 'application/vnd.github.v3+json'}
❹ r = requests.get(url, headers=headers)
❺ print(f"Status code: {r.status_code}")

# 将API响应赋给一个变量。
❻ response_dict = r.json()

# 处理结果。
print(response_dict.keys())

在❶处，导入模块 requests。在❷处，存储 API 调用的 URL。最新的 GitHub API 版本为第 3 版，因此通过指
定 headers 显式地要求使用这个版本的 API（见❸），再使用 requests 调用 API（见❹）。

这里调用 get() 并将 URL 传递给它，再将响应对象赋给变量 r。响应对象包含一个名为 status_code 的属性，
指出了请求是否成功（状态码 200 表示请求成功）。在❺处，打印 status_code，核实调用是否成功。

这个 API 返回 JSON 格式的信息，因此使用方法 json() 将这些信息转换为一个 Python 字典（见❻），并将结果
存储在 response_dict 中。

最后，打印 response_dict 中的键，输出如下：

Status code: 200
dict_keys(['total_count', 'incomplete_results', 'items'])

状态码为 200，由此知道请求成功了。响应字典只包含三个键：'total_count'、'incomplete_results' 和
'items'。下面来看看响应字典内部是什么样的。

注意：像这样简单的调用应该会返回完整的结果集，因此完全可以忽略与 'incomplete_results' 关联的值。但在
执行更复杂的 API 调用时，应检查这个值。



5、处理响应字典

将 API 调用返回的信息存储到字典后，就可处理其中的数据了。下面来生成一些概述这些信息的输出。这是一种不错的
方式，可确认收到了期望的信息，进而开始研究感兴趣的信息：

import requests

# 执行API调用并存储响应。
--snip--

# 将API响应赋给一个变量。
response_dict = r.json()
❶ print(f"Total repositories: {response_dict['total_count']}")

# 探索有关仓库的信息。
❷ repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# 研究第一个仓库。
❸ repo_dict = repo_dicts[0]
❹ print(f"\nKeys: {len(repo_dict)}")
❺ for key in sorted(repo_dict.keys()):
    print(key)

在❶处，打印与 'total_count' 相关联的值，它指出了 GitHub 总共包含多少个 Python 仓库。

与 'items' 关联的值是个列表，其中包含很多字典，而每个字典都包含有关一个 Python 仓库的信息。在❷处，将
这个字典列表存储在 repo_dicts 中。接下来，打印 repo_dicts 的长度，以获悉获得了多少个仓库的信息。

为更深入地了解每个仓库的信息，提取 repo_dicts 中的第一个字典，并将其存储在 repo_dict 中（见❸）。接
下来，打印这个字典包含的键数，看看其中有多少信息（见❹）。在❺处，打印这个字典的所有键，看看其中包含哪些
信息。

输出让你对实际包含的数据有了更清晰的认识：

Status code: 200
Total repositories: 8434673
Repositories returned: 30

❶ Keys: 78
allow_forking
archive_url
archived
assignees_url
--snip--
url
visibility
watchers
watchers_count

GitHub 的 API 返回有关仓库的大量信息：repo_dict 包含 78 个键（见❶）。通过仔细查看这些键，可大致知道
可提取有关项目的哪些信息（要准确地获悉API将返回哪些信息，要么阅读文档，要么像这里一样使用代码来查看）。

下面来提取repo_dict 中与一些键相关联的值：

--snip--
# 研究有关仓库的信息。
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# 研究第一个仓库。
repo_dict = repo_dicts[0]
print("\nSelected information about first repository:")
❶ print(f"Name: {repo_dict['name']}")
❷ print(f"Owner: {repo_dict['owner']['login']}")
❸ print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
❹ print(f"Created: {repo_dict['created_at']}")
❺ print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")

这里打印的值对应于表示第一个仓库的字典中的很多键。在❶处，打印了项目的名称。项目所有者是由一个字典表示的，
因此❷处使用键 owner 来访问表示所有者的字典，再使用键 key 来获取所有者的登录名。在❸处，打印项目获得了
多少个星的评级，以及该项目 GitHub 仓库的 URL。接下来，显示项目的创建时间（见❹）和最后一次更新的时间
（见❺）。最后，打印仓库的描述。输出类似于下面这样：

Status code: 200
Total repositories: 8440238
Repositories returned: 30

Selected information about first repository:
Name: public-apis
Owner: public-apis
Stars: 174277
Repository: https://github.com/public-apis/public-apis
Created: 2016-03-20T23:49:42Z
Updated: 2022-01-16T11:49:52Z
Description: A collective list of free APIs

从上述输出可知，到目前为止（2022/01/16），GitHub 上星级最高的 Python 项目为 public-apis，其所有
者为用户 public-apis，有 174 277 多位 GitHub 用户给这项目加星了。可以看到这个项目仓库的 URL，其
创建时间为 2016 年 3 月，且最近更新了。最后，描述指出项目 system-design-primer 包含一系列深受欢迎
的 Python 资源。



6、概述最受欢迎的仓库

对这些数据进行可视化时，想涵盖多个仓库。下面就来编写一个循环，打印 API 调用返回的每个仓库的特定信息，以便
能够在可视化中包含所有这些信息：

--snip--
# 研究有关仓库的信息。
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

❶ print("\nSelected information about each repository:")
❷ for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")

在❶处，打印了一条说明性消息。在❷处，遍历 repo_dicts 中的所有字典。在这个循环中，打印每个项目的名称、所
有者、星级、 在 GitHub 上的 URL 以及描述：

Status code: 200
Total repositories: 8622944
Repositories returned: 30

Selected information about each repository:

Name: public-apis
Owner: public-apis
Stars: 174276
Repository: https://github.com/public-apis/public-apis
Description: A collective list of free APIs

Name: Python
Owner: TheAlgorithms
Stars: 127448
Repository: https://github.com/TheAlgorithms/Python
Description: All Algorithms implemented in Python

Name: awesome-python
Owner: vinta
Stars: 113339
Repository: https://github.com/vinta/awesome-python
Description: A curated list of awesome Python frameworks, libraries, software and resources

在上述输出中，有些有趣的项目可能值得一看。但不要在这上面花费太多时间，因为即将创建的可视化图表能让你更容易
地看清结果。



7、监视 API 的速率限制

大多数 API 存在速率限制，也就是说，在特定时间内可执行的请求数存在限制。要获悉是否接近了 GitHub 的限制，
请在浏览器中输入 https://api.github.com/rate_limit，你将看到类似于下面的响应：

{
    "resources":{
        "core":{
            "limit":60,
            "remaining":60,
            "reset":1642337680,
            "used":0,
            "resource":"core"
        },
❶        "search":{
❷             "limit":10,
❸            "remaining":10,
❹            "reset":1642334140,
            "used":0,
            "resource":"search"
        }
    },
--snip--

这里关心的信息是搜索 API 的速率限制（见❶）。从❷处可知，极限为每分钟 10 个请求，而在当前分钟内，还可执行
10 个请求（见❸）。reset 值指的是配额将重置的 Unix 时间或新纪元时间（1970年1月1日午夜后多少秒）（见❹）。
用完配额后，你将收到一条简单的响应，由此知道已到达 API 极限。到达极限后，必须等待配额重置。

注意：很多 API 要求注册获得 API 密钥后才能执行 API 调用。到目前为止（2022/01/16），GitHub 没有这样的
要求，但获得 API 密钥后，配额将高得多。

"""