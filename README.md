<!--
 * @Author: shushigege
 * @Date: 2023-12-06 11:22:47
 * @LastEditTime: 2023-12-06 17:23:52
 * @email: shushigege@gmail.com
-->
# chatgpt
用于记录狗屁通中的学习过程  
国内镜像网站，可直接输入官方账号密码登录使用  
https://chat.xf233.com  
https://chat1.zhile.io  
官网地址：  https://openai.com/blog/chatgpt  
镜像站点主页： https://pypi.tuna.tsinghua.edu.cn/simple  
如果你想在使用pip时使用清华大学的PyPI镜像，可以执行以下命令  
pip install XXX -i https://pypi.tuna.tsinghua.edu.cn/simple

## 脚本学习
### 1.grep_demsg.py
是用于过滤bugreport中的内核log  
输出的内核log===>output.txt  
内存的信息log===>kernel_mem.txt  
这个命令将使用脚本中指定的默认前缀 "[START]" 和默认后缀 "[END]"，并将提取的文本保存到 output.txt 文件中。然后，将会根据关键词过滤出相应的行并保存到 kernel_mem.txt 文件中。如果你希望在命令行中指定不同的前缀和后缀，你可以添加额外的参数
使用方法：  
```python
<1>python grep_demsg.py your_input_file.txt --output_file output.txt  
<2>python grep_demsg.py your_input_file.txt --output_file output.txt  --prefix "[CUSTOM_START]" --suffix "[CUSTOM_END]" 
```

### 2.combine_log.py  
可以将拆分的offlinelog 组合到一块  
使用方法：  
```python
python combine_log.py 
```