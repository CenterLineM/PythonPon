try:
    # 用 "raise" 來發起例外
    raise IndexError("This is an index error")
except IndexError as e:
    pass    # 毫無反應，就只是個什麼都沒做的pass。通常這邊會讓你做對例外的處理
except (TypeError, NameError):
    pass    # 有需要的話，多種例外可以一起處理
else:   # else 可有可無，但必須寫在所有的except後
    print "All good!"   # 只有在try的時候沒有產生任何except才會被執行
finally: # 不管什麼情況下一定會被執行
    print "We can clean up resources here"

# 除了try/finally以外，你可以用 with 來簡單的處理清理動作
with open("myfile.txt") as f:
    for line in f:
        print line


def add(x, y): # def 建立函式
    print "x is {0} and y is {1}".format(x, y)
    return x + y # return 回傳直

# 
add(5, 6)

add(y=6, x=5)
# 使用此方式順序不 影響執行

# 多變數函示 * 代表參數tuple
def varargs(*args):
    return args
varargs(1, 2, 3) # => (1, 2, 3)

# 第二型
def keyword_args(**kwargs):
    return kwargs

#EX
keyword_args(big="foot", loch="ness") # =>{"big": "foot", "loch": "ness"}

#可同時使用多個多變數
def all_the_args(*args, **kwargs):
    print args
    print kwargs

# 可反向操作
# * 將變數展開順序排序的操作 *來表示參數tuple
# ** 將變數展開為keyword 排序 之 變數 **來表示參數dictionary
args =(1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args) 
all_the_args(**kwargs)  
all_the_args(*args, **kwargs)
# 逆丟得參數


# 你可以把args跟kwargs傳到下一個函式內
# 分別用 * 跟 ** 將它展開就可以了
def pass_all_the_args(*args, **kwargs):
    all_the_args(*args, **kwargs)
    print varargs(*args)
    print keyword_args(**kwargs)
        
