#!/usr/bin/env python

import wx

#----------------------------------------------------------------------------

pageTexts = [ "Yet",
              "Another",
              "Way",
              "To",
              "Select",
              "Pages"
              ]


class TestCB(wx.Choicebook):
    def __init__(self, parent, id, log):
        wx.Choicebook.__init__(self, parent, id)
        self.log = log

        for count, txt in enumerate(pageTexts, start=1):
            win = wx.Panel(self)
            st = (
                wx.StaticText(
                    win,
                    -1,
                    "wx.Choicebook is yet another way to switch between 'page' windows",
                    (10, 10),
                )
                if count == 1
                else wx.StaticText(win, -1, "Page: %d" % count, (10, 10))
            )

            self.AddPage(win, txt)

        self.Bind(wx.EVT_CHOICEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_CHOICEBOOK_PAGE_CHANGING, self.OnPageChanging)


    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        self.log.write('OnPageChanged,  old:%d, new:%d, sel:%d\n' % (old, new, sel))
        event.Skip()

    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        self.log.write('OnPageChanging, old:%d, new:%d, sel:%d\n' % (old, new, sel))
        event.Skip()

#----------------------------------------------------------------------------

def runTest(frame, nb, log):
    return TestCB(nb, -1, log)

#----------------------------------------------------------------------------


overview = """\
<html><body>
<h2>wx.Choicebook</h2>
<p>

This class is a control similar to a notebook control, but uses a
wx.Choice to manage the selection of the pages.

"""



if __name__ == '__main__':
    import sys,os
    import run
    run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])



