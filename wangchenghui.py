import itchat

# 登录
itchat.login()
# 发送消息
itchat.send(u'你好', 'filehelper')
friends = itchat.get_friends(update=True)[:]
total = len(friends) - 1
man = women = other = 0
 
for friend in friends[0:] :
    sex = friend["Sex"]
    if sex == 1 :
        man += 1
    elif sex == 2 :
        women += 1
    else :
        other += 1
def sex_classify(self):
        for friend in self.friends:
            if friend['Sex'] == 0:
                self.unknown += 1
            elif friend['Sex'] == 1:
                self.female += 1
            else:
                self.male += 1
 
        labels = ['unknown', 'male', 'female']
        sex_num = [self.unknown, self.female, self.male]
print("男性好友：%.2f%%" % (float(man) / total * 100))
print("女性好友：%.2f%%" % (float(women) / total * 100))
print("其他：%.2f%%" % (float(other) / total * 100))
