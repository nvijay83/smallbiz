__author__ = 'vijay'


from flask import Flask, request
from flask.ext import restful
import time

app = Flask(__name__)
api = restful.Api(app)


class Business(restful.Resource):
    def get(self, b_id):
        '''
            get all the postings
        '''
        print "b_id is %d"%b_id
        #json = db.get_posts(b_id)
        pass

    def put(self, b_id):
        post = request.form['post']
        #image = request.form['image']
        t = time.time()
        print "post is %s, %d"%(post, t)
        #db.write(b_id, post, 0, 0, t)

class Customer(restful.Resource):
    def get(self, c_id):
        print "customer id is %d", c_id
        pass



class Likes(restful.Resource):
    def put(self, b_id, post_id):
        like = request.form['like']
        print "customer id %d, post_id %d, like %d",(b_id,post_id, like)
        #db.write(c_id,post_id, like)


api.add_resource(Business, '/business/<int:b_id>')
api.add_resource(Customer, '/customer/<int:c_id>')
api.add_resource(Likes, '/business/<int:b_id>/<int:post_id>')


if __name__ == '__main__':
    app.run(debug=True)