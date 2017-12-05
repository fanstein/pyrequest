# coding=utf8
import web

urls = (
    '/index', 'index',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello'
)


# 参数获取
# web.input()
# 请求头获取
# web.ctx.env

class index:
    def GET(self):
        query = web.input()
        return query


class blog:
    def GET(self):
        return "blog"

    def POST(self):
        data = web.input()
        print data
        return data


class hello:
    def GET(self, name):
        return "hello" + name


def start():
    app = web.application(urls, globals())
    app.run()


if __name__ == "__main__":
    start()
