#!/usr/bin/env python

import sys
import os

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

    wm = pyinotify.WatchManager()
    mask = pyinotify.IN_MODIFY

    extensions = ['py']

    class ActionProcesser(pyinotify.ProcessEvent):
        def process_IN_MODIFY(self, event, ext='py'):
            if all(not event.pathname.endswith(ext) for ext in extensions):
                return
            #print event
            if call(command, shell=True):
                failed.show()
            else:
                passed.show()

    notifier = pyinotify.Notifier(wm, ActionProcesser())
    wdd = wm.add_watch(os.path.join(os.getcwd(), 'tests'), mask, rec=True)

    notifier.loop()


if __name__ == '__main__':
    main()
