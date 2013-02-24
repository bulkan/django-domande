#!/usr/bin/env python

import sys
import os
import sched, time

from subprocess import call

import pyinotify
import pynotify





def main():

    if len(sys.argv)==1:
        print "Please pass a command to excute as a parameter"
        print "For example autorun.py 'ruby foo.rb'"
        sys.exit()

    if not pynotify.init ("summary-body"):
        sys.exit (1)

    passed = pynotify.Notification(u'autotest.py \u2713', u'All tests passed')
    failed = pynotify.Notification(u'autotest.py \u2718', u'Tests are failing')

    command = sys.argv[1]

    running_tests = False

    s = sched.scheduler(time.time, time.sleep)
    def tester(running_tests):
        if running_tests:
            return
        running_tests = True
        if call(command, shell=True):
            failed.show()
        else:
            passed.show()
        running_tests = False


    wm = pyinotify.WatchManager()
    mask = pyinotify.IN_MODIFY

    extensions = ['py']

    class ActionProcesser(pyinotify.ProcessEvent):
        def process_IN_MODIFY(self, event, ext='py'):
            if all(not event.pathname.endswith(ext) for ext in extensions):
                return
            if s.empty():
                s.enter(15, 1, tester, (running_tests,))
                s.run()

    notifier = pyinotify.Notifier(wm, ActionProcesser())
    wdd = wm.add_watch(os.path.join(os.getcwd(), 'domande'), mask, rec=True)

    notifier.loop()


if __name__ == '__main__':
    main()
