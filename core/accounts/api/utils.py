from threading import Thread


class EmailThreading(Thread):
     # override the constructor
    def __init__(self, email_obj):
        # execute the base constructor
        Thread.__init__(self)
        self.email_obj = email_obj
        # store the value
    def run(self):
        self.email_obj.send()