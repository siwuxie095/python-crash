"""

Hacker News API


为探索如何使用其他网站的 API 调用，下面来看看 Hacker News。在 Hacker News 网站，用户分享编程和技术方面的文章，
并就这些文章展开积极的讨论。Hacker News 的 API 让你能够访问有关该网站所有文章和评论的信息，且不要求通过注册获得
密钥。

下面的调用返回本书编写期间最热门的文章的信息：

https://hacker-news.firebaseio.com/v0/item/19155826.json

如果在浏览器中输入这个 URL，将发现响应位于一对花括号内，表明这是一个字典。如果不改进格式，这样的响应难以阅读。下面
像之前的地震地图项目那样，通过方法 json.dump() 来运行这个 URL，以便对返回的信息进行探索：

import requests
import json

# 执行API调用并存储响应。
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# 探索数据的结构。
response_dict = r.json()
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)

这里的所有代码都在前两章使用过，你应该不会感到陌生。输出是一个字典，其中包含有关 ID 为 19155826 的文章的信息：

{
    "by": "jimktrains2",
❶    "descendants": 221,
    "id": 19155826,
❷    "kids": [
        19156572,
        19158857,
        --snip--
    ],
    "score": 728,
    "time": 1550085414,
❸    "title": "Nasa\u2019s Mars Rover Opportunity Concludes a 15-Year Mission",
    "type": "story",
❹    "url": "https://www.nytimes.com/2019/02/13/science/mars-opportunity-rover-dead.html"
}

这个字典包含很多键。与键 'descendants' 相关联的值是文章被评论的次数（见❶）。与键 'kids' 相关联的值包含文章所
有评论的 ID（见❷）。每个评论本身也可能有评论，因此文章的后代（descendant）数量可能比其 'kids' 的数量多。这个
字典中还包含当前文章的标题（见❸）和 URL（见❹）。

下面的 URL 返回一个列表，其中包含 Hacker News 上当前排名靠前的文章的 ID：

https://hacker-news.firebaseio.com/v0/topstories.json

通过使用这个调用，可获悉当前有哪些文章位于主页，再生成一系列类似于前面的 API 调用。通过使用这种方法，可概述当前位
于 Hacker News 主页的每篇文章：

from operator import itemgetter
import requests

# 执行API调用并存储响应。
❶ url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# 处理有关每篇文章的信息。
❷ submission_ids = r.json()
❸ submission_dicts = []
for submission_id in submission_ids[:30]:
    # 对于每篇文章，都执行一个API调用。
❹    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # 对于每篇文章，都创建一个字典。
❺    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
❻    submission_dicts.append(submission_dict)

❼ submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

❽ for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

首先，执行一个 API 调用，并打印响应的状态（见❶）。这个 API 调用返回一个列表，其中包含 Hacker News 上当前最热
门的 500 篇文章的 ID。接下来，将响应对象转换为一个 Python 列表（见❷），并将其存储在 submission_ids 中。后
面将使用这些 ID 来创建一系列字典，其中每个字典都存储了一篇文章的信息。

在❸处，创建一个名为 submission_dicts 的空列表，用于存储前面所说的字典。接下来，遍历前 30 篇文章的 ID。对于
每篇文章，都执行一个 API 调用，其中的 URL 包含 submission_id 的当前值（见❹）。这里打印请求的状态和文章 ID，
以便知道请求是否成功。

在❺处，为当前处理的文章创建一个字典，并在其中存储文章的标题、讨论页面的链接和评论数。然后，将 submission_dict
附加到 submission_dicts 末尾（见❻）。

Hacker News 上的文章是根据总体得分排名的，而总体得分取决于很多因素，包含被推荐的次数、评论数和发表时间。这里要
根据评论数对字典列表 submission_dicts 进行排序，为此使用了模块 operator 中的函数 itemgetter()（见❼）。
这里向这个函数传递了键 'comments'，因此它从该列表的每个字典中提取与键 'comments' 关联的值。这样，函数 sort-
ed() 将根据这个值对列表进行排序。这里将列表按降序排列，即评论最多的文章位于最前面。

对列表排序后遍历它（见❽），并打印每篇热门文章的三项信息：标题、讨论页面的链接和评论数：

Status code: 200
id: 29955475	status: 200
id: 29954266	status: 200
id: 29954607	status: 200
--snip--

Title: Why Galesburg has no money
Discussion link: http://news.ycombinator.com/item?id=29954607
Comments: 104

Title: Shenanigans on Microsoft Feedback Hub
Discussion link: http://news.ycombinator.com/item?id=29954266
Comments: 101

Title: Cheezam – Shazam for Cheese
Discussion link: http://news.ycombinator.com/item?id=29955475
Comments: 25

--snip--

无论使用哪个 API 来访问和分析信息，流程都与此类似。有了这些数据后，就可进行可视化，指出最近哪些文章引发了最激烈
的讨论。基于这种方式，应用程序可以为用户提供网站（如Hacker News）的定制化阅读体验。

要深入了解通过 Hacker News API 可访问哪些信息，请参阅其文档页面。

"""