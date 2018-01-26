import pandas as pd

def read_website (url, category):
    df = pd.read_html(url, header = 0)
    
    for i in range(2, 5):
        df[i].rename(inplace = True, columns = {'序号': 'No.', '刊物简称': 'Acronym', '刊物全称': 'Journal', '出版社': 'Publisher', '网址': 'Website'})
        file_name = str('Journal_Rank_'+ J_rank(i) + '__' + category + '.csv')
        df[i].to_csv(file_name, index = False)

    
    for i in range(5, 8):
        df[i].rename(inplace = True, columns = {'序号': 'No.', '会议简称': 'Acronym', '会议全称': 'Conference', '出版社': 'Publisher', '网址': 'Website'})
        file_name = str('Conference_Rank_' + C_rank(i) + '__' + category + '.csv')
        df[i].to_csv(file_name, index = False)
        
# Here we created two dictionaries below to help changing the file name. 
def J_rank(x):
    return {2 : 'A', 3 : 'B', 4 : 'C'}.get(x, 0)

def C_rank(x):
    return {5 : 'A', 6 : 'B', 7 : 'C'}.get(x, 0)

# 计算机体系结构/并行与分布计算/存储系统:  
url_1 = 'http://history.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2903028135780' 
category_1 = 'Computer Architecture & Parallel and Distributed Computing & Storage System'

#计算机网络:
url_2 = 'http://history.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2903028135856'
category_2 = 'Computer Networks'

#网络与信息安全:
url_3 = 'http://history.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2903940690850'
category_3 = 'Network and Information Security'

#软件工程/系统软件/程序设计语言:
url_4 = 'http://history.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2903028135775'
category_4 = 'Software Engineering & System Software & Programming Language'

#数据库/数据挖掘/内容检索"\:
url_5 = 'http://history.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2903940690081'
category_5 = 'Database & Data Mining & Knowledge Discovery'

#计算机科学理论
url_6 = 'http://history.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2903940690325'
category_6 = 'Theory of Computer Science'

#计算机图形学与多媒体:
url_7 = 'http://history.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2903940690854'
category_7 = 'Computer Graphics and Multimedia'

#人工智能:
url_8 = 'http://history.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2903940690839'
category_8 = 'Artificial Intelligence'

#人机交互与普适计算:
url_9 = 'http://history.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2903940690320'
category_9 = 'Computer-Human Interaction & Ubiquitous Computing'

#交叉/综合/新兴:
url_10 = 'http://history.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2903940690316'
category_10 = 'Interdisciplinary & Intergration & Inovation'


read_website(url_1, category_1)
read_website(url_2, category_2)
read_website(url_3, category_3)
read_website(url_4, category_4)
read_website(url_5, category_5)
read_website(url_6, category_6)
read_website(url_7, category_7)
read_website(url_8, category_8)
read_website(url_9, category_9)
read_website(url_10, category_10)

