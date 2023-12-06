# chatgpt
用于记录狗屁通中的学习过程

1.grep_demsg.py是用于过滤bugreport中的内核log
输出的内核log===>output.txt
内存的信息log===>kernel_mem.txt
这个命令将使用脚本中指定的默认前缀 "[START]" 和默认后缀 "[END]"，并将提取的文本保存到 output.txt 文件中。然后，将会根据关键词过滤出相应的行并保存到 kernel_mem.txt 文件中。如果你希望在命令行中指定不同的前缀和后缀，你可以添加额外的参数
使用方法：
<1>python grep_demsg.py your_input_file.txt --output_file output.txt
<2>python grep_demsg.py your_input_file.txt --output_file output.txt --prefix "[CUSTOM_START]" --suffix "[CUSTOM_END]"

2.combine_log.py
使用方法：
可以将拆分的offlinelog 组合到一块
python combine_log.py 
