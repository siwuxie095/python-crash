# 1、查看系统可用字体
from matplotlib.font_manager import FontManager
fm = FontManager()
mat_fonts = set(f.name for f in fm.ttflist)
print(mat_fonts)

# 2、找到 Matplotlib 安装目录
import matplotlib
print(matplotlib.matplotlib_fname())

# 3、打开 matplotlibrc 文件，搜索 font.sans-serif，取消前面的注释 #，将 Arial Unicode MS
# 字体贴在冒号后，形如："font.sans-serif: Arial Unicode MS, DejaVu Sans, ..."

# 4、将 Arial Unicode.ttf 文件（系统内字体文件）粘贴到与 matplotlibrc 文件同级的 fonts/ttf
# 文件夹中

# 5、最终使用方法如下，这样即可正常显示中文

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus']=False


# 6、如果使用了 plt.style.use('seaborn')，就一定要放在这两句前面，不然无法正常显示中文，如下

import matplotlib.pyplot as plt

plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus']=False