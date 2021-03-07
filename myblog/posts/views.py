from flask import render_template, Blueprint
from myblog.models import Post



post_blueprint = Blueprint('post_blueprint' , __name__ ,  template_folder="templates")



@post_blueprint.route('/posts')
def posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)