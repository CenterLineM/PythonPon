try:
    # �� "raise" �ӵo�_�ҥ~
    raise IndexError("This is an index error")
except IndexError as e:
    pass    # �@�L�����A�N�u�O�Ӥ��򳣨S����pass�C�q�`�o��|���A����ҥ~���B�z
except (TypeError, NameError):
    pass    # ���ݭn���ܡA�h�بҥ~�i�H�@�_�B�z
else:   # else �i���i�L�A�������g�b�Ҧ���except��
    print "All good!"   # �u���btry���ɭԨS�����ͥ���except�~�|�Q����
finally: # ���ޤ��򱡪p�U�@�w�|�Q����
    print "We can clean up resources here"

# ���Ftry/finally�H�~�A�A�i�H�� with ��²�檺�B�z�M�z�ʧ@
with open("myfile.txt") as f:
    for line in f:
        print line


def add(x, y): # def �إߨ禡
    print "x is {0} and y is {1}".format(x, y)
    return x + y # return �^�Ǫ�

# 
add(5, 6)

add(y=6, x=5)
# �ϥΦ��覡���Ǥ� �v�T����

# �h�ܼƨ�� * �N��Ѽ�tuple
def varargs(*args):
    return args
varargs(1, 2, 3) # => (1, 2, 3)

# �ĤG��
def keyword_args(**kwargs):
    return kwargs

#EX
keyword_args(big="foot", loch="ness") # =>{"big": "foot", "loch": "ness"}

#�i�P�ɨϥΦh�Ӧh�ܼ�
def all_the_args(*args, **kwargs):
    print args
    print kwargs

# �i�ϦV�ާ@
# * �N�ܼƮi�}���ǱƧǪ��ާ@ *�Ӫ�ܰѼ�tuple
# ** �N�ܼƮi�}��keyword �Ƨ� �� �ܼ� **�Ӫ�ܰѼ�dictionary
args =(1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args) 
all_the_args(**kwargs)  
all_the_args(*args, **kwargs)
# �f��o�Ѽ�


# �A�i�H��args��kwargs�Ǩ�U�@�Ө禡��
# ���O�� * �� ** �N���i�}�N�i�H�F
def pass_all_the_args(*args, **kwargs):
    all_the_args(*args, **kwargs)
    print varargs(*args)
    print keyword_args(**kwargs)
        
