# coding: UTF-8
class crawler:
    def __init__(self,dbname):
        pass
    
    def __del__(self):
        pass
    
    def dbcommit(self):
        pass
    
    
    
    # エントリIDを取得したりそれが存在しない場合には追加
    # するための補助関数
    
    def getentryid(self, table, field, value, createnew=True):
        return None
    
    # 個々のページをインデックス    
    def addtoindex(self,url,soup):
        print "Indexing %s" % url
    
    # HTMLのページからタグのない状態でテキストを抽出
    def gettextonly(self,soup):
        return None
        
    # 空白以外の文字で単語を分割
    def separatewords(self,text):
        return None
    
    # URLが既にインデックスされていたらtrueを返す
    def isindexed(self,url):
        return False
        
    # 2つのページの間にリンクを付け加える
    def addlinkref(self,urlFrom,urlTo,linkText):
        pass
    
    # ページのリストを受け取り与えられた深さで幅優先の検索
    # そしてページをインデクシングする
    def crawl(self,pages,depth=2):
        pass
    
    #データベースのテーブルを作る
    def createindextables(self):
        pass
    