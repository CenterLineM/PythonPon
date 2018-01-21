



# 輸出輸入結果
from pycon.xmath import pi
from pycon.xmath import max
from pycon.xmath import sum
print (max(10, 5))
#print (sum(5, 1))
print (pi)

# 實作物件
from pycon.bank import Account 
acct = Account('Justin', '123-4567', 1000)
acct.deposit(500)
acct.withdraw(200)
print (acct)
