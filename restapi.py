__author__ = 'vijay'


from flask import Flask, request
from flask.ext import restful
import time
from post import getposts, addpost, getfeed, likepost, dislikepost,addmsg,getmsg

app = Flask(__name__)
api = restful.Api(app)


class Business(restful.Resource):
    def get(self, b_id):
        '''
            get all the postings
        '''
        print "b_id is %d"%b_id
        return getposts(b_id)

    def put(self, b_id):
        post = request.form['post']
        #image = request.form['image']
        t = time.time()
        print "post is %s, %d"%(post, t)
        addpost(b_id, post, '', 0, 0, t)
        return 0

class Customer(restful.Resource):
    def get(self, c_id):
        print "customer id is %d", c_id
        return getfeed(c_id)



class Posts(restful.Resource):
    def put(self, post_id):
        like = request.form['like']
        print "post_id %d, like %d",(post_id, like)
        if like == 'True':
            likepost(post_id)
        else:
            dislikepost(post_id)

class Messages(restful.Resource):
    def get(self, cid, bid):
        return getmsg(cid, bid)

    def put(self, bid, cid):
        msg = request.form['message']
        addmsg(bid, cid, msg, time.time())



api.add_resource(Business, '/business/<int:b_id>')
api.add_resource(Customer, '/customer/<int:c_id>')
api.add_resource(Posts, '/post/<int:post_id>')
api.add_resource(Messages, '/message/<int:bid>/<int:cid>')


if __name__ == '__main__':
    app.run(debug=True)