if __name__ == '__main__':
    from settings import *
    import tornado
    app = Application()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()