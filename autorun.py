#!/usr/bin/env python

import sys
import os
import pyinotify

def main():

    if len(sys.argv)==1:
        print "Please pass a command to excute as a parameter"
        print "For example autorun.py 'ruby foo.rb'"
        sys.exit()

    commandToRun = sys.argv[1]

    watchManager = pyinotify.WatchManager()
    mask = pyinotify.IN_MODIFY

    extensions = ['py']

    class ActionProcesser(pyinotify.ProcessEvent):
        def process_IN_MODIFY(self, event, ext='py'):
            if all(not event.pathname.endswith(ext) for ext in extensions):
                return
            print event
            os.system(commandToRun)

    notifier = pyinotify.Notifier(watchManager, ActionProcesser())
    wdd = watchManager.add_watch(os.path.join(os.getcwd(), 'tests'), mask, rec=True)

    notifier.loop()


if __name__ == '__main__':
    main()
