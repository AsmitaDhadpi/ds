import datetime
print('# 3 Reformatting data entry to match specific formatting criteria.')
baddate = datetime.date(2019, 10, 31) 
baddata=format(baddate,'%Y-%m-%d') 
gooddate = datetime.datetime.strptime(baddata,'%Y-%m-%d') 
gooddata=format(gooddate,'%d %B %Y') 
print('Bad Data : ',baddata) 
print('Good Data : ',gooddata) 
