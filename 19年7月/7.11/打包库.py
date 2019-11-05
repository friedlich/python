###
# 直接在点7.11文件夹在终端中打开输入pyinstaller -F chongfubiquge.py 完事


# 发布命令介绍
# 有两种方法调用发布流程：
# ①直接使用Pyinstaller应用程序调用待发布脚本
# ②用Python调用pyinstaller-script脚本再调用待发布脚本
# 两种方法用起来没什么差别，方法①少个步骤，就用方法①了咯

# -w指令
# 直接发布的exe应用带命令行调试窗口，在指令内加入-w命令可以屏蔽

# -F指令
# 注意指令区分大小写。这里是大写。使用-F指令可以把应用打包成一个独立的exe文件，否则是一个带各种dll和依赖文件的文件夹

# -p指令
# 这个指令后面可以增加pyinstaller搜索模块的路径。因为应用打包涉及的模块很多。这里可以自己添加路径。不过经过笔者测试，
# site-packages目录下都是可以被识别的，不需要再手动添加

### 
# 这边使用最简单的-F参数生成文件，执行以下命令：
# 后面的路径为你的python文件的位置（如果第一步没有添加变量，这里还是要到Script下执行pyinstaller.exe文件）
# pyinstaller -F c:\...\your_python_file.py



# C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习>pyinstaller.exe -F c:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练
# 习\19年7月\7.11\chongfubiquge.py
# 179 INFO: PyInstaller: 3.5
# 179 INFO: Python: 3.6.5
# 181 INFO: Platform: Windows-10-10.0.17134-SP0
# 185 INFO: wrote C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\chongfubiquge.spec
# 210 INFO: UPX is not available.
# 223 INFO: Extending PYTHONPATH with paths
# ['c:\\Users\\asus\\Desktop\\Python\\风变Python爬虫精进\\爬虫阶段练习\\19年7月\\7.11',
#  'C:\\Users\\asus\\Desktop\\Python\\风变Python爬虫精进\\爬虫阶段练习']
# 224 INFO: checking Analysis
# 225 INFO: Building Analysis because Analysis-00.toc is non existent
# 225 INFO: Initializing module dependency graph...
# 245 INFO: Initializing module graph hooks...
# 255 INFO: Analyzing base_library.zip ...
# 7976 INFO: running Analysis Analysis-00.toc
# 8030 INFO: Adding Microsoft.Windows.Common-Controls to dependent assemblies of final executable
#   required by c:\users\asus\appdata\local\programs\python\python36\python.exe
# 13584 INFO: Caching module hooks...
# 13598 INFO: Analyzing c:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年7月\7.11\chongfubiquge.py
# 15026 INFO: Processing pre-find module path hook   distutils
# 17025 INFO: Processing pre-find module path hook   site
# 17027 INFO: site: retargeting to fake-dir 'c:\\users\\asus\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\PyInstaller\\fake-modules'
# 19541 INFO: Processing pre-safe import module hook   setuptools.extern.six.moves
# 27583 INFO: Processing pre-safe import module hook   urllib3.packages.six.moves
# 32137 INFO: Processing pre-safe import module hook   six.moves
# 38637 INFO: Loading module hooks...
# 38638 INFO: Loading module hook "hook-certifi.py"...
# 38644 INFO: Loading module hook "hook-cryptography.py"...
# 40004 INFO: Loading module hook "hook-distutils.py"...
# 40007 INFO: Loading module hook "hook-docx.py"...
# 40022 INFO: Loading module hook "hook-encodings.py"...
# 40480 INFO: Loading module hook "hook-gevent.py"...
# 41501 INFO: Determining a mapping of distributions to packages...
# 101852 WARNING: Unable to find package for requirement greenlet from package gevent.
# 101852 INFO: Packages required by gevent:
# ['cffi']
# 107194 INFO: Loading module hook "hook-lib2to3.py"...
# 107240 INFO: Loading module hook "hook-lxml.etree.py"...
# 107253 INFO: Loading module hook "hook-pkg_resources.py"...
# 109790 INFO: Processing pre-safe import module hook   win32com
# 110191 INFO: Loading module hook "hook-pycparser.py"...
# 110193 INFO: Loading module hook "hook-pydoc.py"...
# 110194 INFO: Loading module hook "hook-pythoncom.py"...
# 111419 INFO: Loading module hook "hook-pywintypes.py"...
# 112666 INFO: Loading module hook "hook-setuptools.py"...
# 121598 INFO: Loading module hook "hook-sysconfig.py"...
# 121601 INFO: Loading module hook "hook-win32com.py"...
# 122754 INFO: Loading module hook "hook-xml.dom.domreg.py"...
# 122755 INFO: Loading module hook "hook-xml.py"...
# 122757 INFO: Loading module hook "hook-_tkinter.py"...
# 124323 INFO: checking Tree
# 124324 INFO: Building Tree because Tree-00.toc is non existent
# 124324 INFO: Building Tree Tree-00.toc
# 124780 INFO: checking Tree
# 124781 INFO: Building Tree because Tree-01.toc is non existent
# 124781 INFO: Building Tree Tree-01.toc
# 124837 INFO: Loading module hook "hook-numpy.core.py"...
# 125127 INFO: Loading module hook "hook-numpy.py"...
# 125393 INFO: Looking for ctypes DLLs
# 125561 INFO: Analyzing run-time hooks ...
# 125586 INFO: Including run-time hook 'pyi_rth_certifi.py'
# 125590 INFO: Including run-time hook 'pyi_rth_pkgres.py'
# 125593 INFO: Including run-time hook 'pyi_rth_win32comgenpy.py'
# 125596 INFO: Including run-time hook 'pyi_rth_multiprocessing.py'
# 125607 INFO: Including run-time hook 'pyi_rth__tkinter.py'
# 125652 INFO: Looking for dynamic libraries
# 182266 INFO: Looking for eggs
# 182267 INFO: Using Python library c:\users\asus\appdata\local\programs\python\python36\python36.dll
# 182268 INFO: Found binding redirects:
# []
# 182316 INFO: Warnings written to C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\build\chongfubiquge\warn-chongfubiquge.txt
# 182827 INFO: Graph cross-reference written to C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\build\chongfubiquge\xref-chongfubiquge.html
# 183136 INFO: checking PYZ
# 183137 INFO: Building PYZ because PYZ-00.toc is non existent
# 183138 INFO: Building PYZ (ZlibArchive) C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\build\chongfubiquge\PYZ-00.pyz
# 188388 INFO: Building PYZ (ZlibArchive) C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\build\chongfubiquge\PYZ-00.pyz completed successfully.
# 188519 INFO: checking PKG
# 188520 INFO: Building PKG because PKG-00.toc is non existent
# 188520 INFO: Building PKG (CArchive) PKG-00.pkg
# 213598 INFO: Building PKG (CArchive) PKG-00.pkg completed successfully.
# 213741 INFO: Bootloader c:\users\asus\appdata\local\programs\python\python36\lib\site-packages\PyInstaller\bootloader\Windows-64bit\run.exe
# 213741 INFO: checking EXE
# 213742 INFO: Building EXE because EXE-00.toc is non existent
# 213743 INFO: Building EXE from EXE-00.toc
# 213744 INFO: Appending archive to EXE C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\dist\chongfubiquge.exe
# 213890 INFO: Building EXE from EXE-00.toc completed successfully.
