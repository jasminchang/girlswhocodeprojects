from random import*

firstnameList=["Alex","Andy", "Amanda", "Abby", "Mona", "Sarah", "Brooke", "Gabe", "Devon", "Remy", "Ellie", "Ryan", "Jessica", "Jackie"]
lastnameList=[" Chan"," Lee"," Smith", " Brown", " Wilson", " Miller", " Johnson", " Snyder", " Allen", " Richardson", " Anderson", " Pearson", " Chang"]
aRandomIndex=randint(0, len(firstnameList)-1)
bRandomIndex=randint(0, len(lastnameList)-1)
print(firstnameList[aRandomIndex]+ lastnameList[bRandomIndex])
