#a = (('w','s','d'),('a', 'b', 'c'))

b = (('\u718a\u7f8e\u5a1f212122', 'https://wwc.alicdn.com/avatar/getAvatar.do?userIdStr=PCQuMkPIXmx4vCv4vkZzO8ZevHlIvG-IM8xWPkxuOFvT&amp;width=160&amp;height=160&amp;type=sns', '2018-09-12', '1.00'), ('\u718a\u7f8e\u5a1f212122', 'https://wwc.alicdn.com/avatar/getAvatar.do?userIdStr=PCQuMkPIXmx4vCv4vkZzO8ZevHlIvG-IM8xWPkxuOFvT&amp;width=160&amp;height=160&amp;type=sns', '2018-12-02','1.00'))

c = [{"nick_name": "hejunshihundan520","pic_url": "https://wwc.alicdn.com/avatar/getAvatar.do?userIdStr=O8xbXm84vHkuOHRIvmIGvkQ0MF9hMG--MCkSPC*ePHxT&amp;width=160&amp;height=160&amp;type=sns","draw_time": 53,"draw_money": "0.50"},{"nick_name": "smine0827","pic_url": "https://wwc.alicdn.com/avatar/getAvatar.do?userIdStr=O8RhvGH0vmk0vFIWvmQGOFQ4MmIyO884P0gWOmR-OHxT&amp;width=160&amp;height=160&amp;type=sns","draw_time": 49,"draw_money": "3.10"},{"nick_name": "她他购test","pic_url": "https://wwc.alicdn.com/avatar/getAvatar.do?userIdStr=Mmk4XmkYv8g0MH7HOmxWPmHbXmHLP8g4v8P-PFgbPmNT&amp;width=160&amp;height=160&amp;type=sns","draw_time": 49,"draw_money": "500.00"}]

d = [{"nick_name": "hejunshihundan520","pic_url": "https://wwc.alicdn.com/avatar/getAvatar.do?userIdStr=O8xbXm84vHkuOHRIvmIGvkQ0MF9hMG--MCkSPC*ePHxT&amp;width=160&amp;height=160&amp;type=sns","draw_time": 53,"draw_money": "0.50"},{"nick_name": "smine0827","pic_url": "https://wwc.alicdn.com/avatar/getAvatar.do?userIdStr=O8RhvGH0vmk0vFIWvmQGOFQ4MmIyO884P0gWOmR-OHxT&amp;width=160&amp;height=160&amp;type=sns","draw_time": 49,"draw_money": "3.10"},{"nick_name": "她他购test","pic_url": "https://wwc.alicdn.com/avatar/getAvatar.do?userIdStr=Mmk4XmkYv8g0MH7HOmxWPmHbXmHLP8g4v8P-PFgbPmNT&amp;width=160&amp;height=160&amp;type=sns","draw_time": 49,"draw_money": "500.00"}]

L = []

for i in c:
    print(tuple(i.values()))
    L.append(tuple(i.values()))

print(L)

#for i in b:
#    print('元祖中的内容：', i)