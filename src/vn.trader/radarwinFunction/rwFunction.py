# encoding: UTF-8

"""
包含一些开发中常用的函数
"""

#----------------------------------------------------------------------
# 根据当前账户信息判断是否可买卖
#参数
# params:buy,sell
# positionDict:当前账户信息
# pos:买/卖量
# price：买/卖价格
def getPosition(params, positionDict, pos, price):
    if params == 'buy':
        posData = positionDict['cny']
        if posData.position < pos * price:
            return False
    elif params == 'sell':
        posData = positionDict['btc']
        if posData.position < pos:
            return False
    return True



 
