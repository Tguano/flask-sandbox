from flask import render_template, request

from blog import blog
from flask_security import current_user
from auth.models import User

# from blog.models import Post


# Подключать Blueprint с префиксом blog

@blog.route("/", defaults={'blog': None})
@blog.route('/<blog_owner>', methods=['GET', 'POST'])
def user_name_view(blog_owner):
    # posts = Post.query.<обработчики>
    posts = [{
                    'title': 'titleOne',
                    'theme': 'themeOne',
                    'body': 'testOne'
            },
            {
                    'title': 'titleTwo',
                    'theme': 'themeTwo',
                    'body': 'testTwo'
            }]

    if current_user.is_authenticated:
        username = current_user.nickname
        if username == blog_owner:
            is_owner = True
        else:
            is_owner = False
    else:
        username = 'anonymous'
        is_owner = False

    return render_template('blog/index.html', is_owner=is_owner, username=username, posts=posts)
