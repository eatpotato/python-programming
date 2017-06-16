这是一个使用argparse进行命令行选项与参数解析的小例子

Examples:

git:(master) ✗ python parse_params.py -t -s test -c test1 -a a -a b  
simple_value     = test  
constant_value   = test1  
boolean_switch   = True  
collection       = ['a', 'b']  
