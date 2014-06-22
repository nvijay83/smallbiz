from tinydb import TinyDB, where
db = TinyDB('./data/db.json')
posttable = db.table('posts')
msgtable = db.table('messages')

def addpost(bid, post, imageurl, likes, dislikes, ts):
    posttable.insert({'busid':bid, 'posttext':post, 'url':imageurl, 'n_likes':likes, 'n_dislikes':dislikes, 'timestamp':ts})

def likepost(pid):
    l = posttable.search(where ('_id') == pid)
    if not l:
        return -1
    likes = l[0]['n_likes']
    likes += 1
    posttable.update({'n_likes':likes}, where ('_id') == pid)
    return 0

def addmsg(cid, bid, msg, ts):
    d = msgtable.search((where ('customer_id') == cid) & (where('busid') == bid))
    if not d:
        l = [(msg, ts)]
        msgtable.insert({'customer_id':cid, 'busid':bid, 'msg_id':l} )
    else:
	l = d[0]['msg_id']
	l.append([(msg, ts)])
        msgtable.update({'msg_id':l}, (where ('customer_id') == cid) & (where('busid') == bid))


def getfeed(cid):
    postrec = []
    print "feed"
    for bid in msgtable.search(where ('customer_id') == cid):
        print bid
        postrec.append(posttable.search(where ('busid') == bid['busid']))
    return postrec

def getmsg(cid, bid):
    return msgtable.search((where ('customer_id') == cid) & (where ('busid') == bid))

def printpost():
    l = posttable.all()
    print l

def printmsg():
    l = msgtable.all()
    print l

addpost(7, 'testing', 'http://test', 1, 0, 24)
addmsg(1, 7, 'text msg', 24)
rec = getfeed(1)
printpost()
printmsg()
