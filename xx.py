import ijson  
  
filename = '/Users/bretonguo/code/python/test/example.json'  
  
def explore_json(file_object, path=''):  
    prefix = path or ''  
    if prefix:  
        prefix += '.'  
  
    with open(file_object, 'r') as f:  
        parser = ijson.parse(f)  
        for prefix, event, value in parser:  
            if event == 'map_key':  
                # 当前是一个对象的键  
                print(f"{prefix[:-1]}: {value}")  
            elif event == 'start_map':  
                # 进入一个新的对象  
                print(f"进入对象: {prefix}")  
                # 你可以递归地调用 explore_json 来探索这个对象  
            elif event == 'end_map':  
                # 离开一个对象  
                print(f"离开对象: {prefix}")  
            elif event == 'start_array':  
                # 进入一个新的数组  
                print(f"进入数组: {prefix}")  
                # 你可以递归地调用 explore_json 并使用 {prefix}item 作为新的路径  
            elif event == 'end_array':  
                # 离开一个数组  
                print(f"离开数组: {prefix}")  
            elif event == 'string' or event == 'number' or event == 'boolean' or event == 'null':  
                # 处理基本数据类型  
                print(f"{prefix}{value}")  
            # 忽略其他事件，如'integer', 'float' 等，它们只是 'number' 的细分  
  
# 调用函数来探索文件  
explore_json(filename)