from threading import Thread
import time
"""
    A basic scheduler class for scheduling recurring tasks by an interval of seconds.
    # Create Scheduler:
    scheduler = Scheduler()   
    # Add tasks in the form of functions
    scheduler.add_task(interval_s, func, args)
    # Start the scheduler, spawns a daemon thread that acts as an event-loop.
    scheduler.start()

    @author: anders simonsen
"""


class Scheduler():
    def __init__(self):
        self.tasks=[]
    
    def add_task(self,func,interval_s,args=()):
        self.tasks.append([func,args,interval_s,-1])
    @staticmethod
    def __event_loop(tasks):
        now=time.time()
        for task in tasks:
            task[3]=now
        while True:
            now = time.time()
            for task in tasks:
                if (now - task[3]) >= task[2]:
                    task[3]=now
                    task[0](*task[1])
            time.sleep(1)

    def start(self):
        t=Thread(target=self.__event_loop,args=[self.tasks,])
        t.daemon=True
        t.start()