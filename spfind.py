#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Mon Jun 27 15:27:43 2011

import sys, os, time
import wx
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin
from wx.lib.mixins.listctrl import ColumnSorterMixin

import tool


DIR_COL = 3

# begin wxGlade: extracode
# end wxGlade


class MyListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin, ColumnSorterMixin):
	def __init__(self, parent, id):
		wx.ListCtrl.__init__(self, parent, id, style=wx.LC_REPORT)
		ListCtrlAutoWidthMixin.__init__(self)
		ColumnSorterMixin.__init__(self, 6)
		self.itemDataMap = {}

		self.InsertColumn(0, "Name", width=220)
		self.InsertColumn(1, "Size", format=wx.LIST_FORMAT_RIGHT, width=80)
		self.InsertColumn(2, "Date Modified", format=wx.LIST_FORMAT_RIGHT, width=160)
		self.InsertColumn(3, "Directory", width=240)

	def GetListCtrl(self):
		return self

	def set_value(self, files):
		for file in files:
			name = os.path.basename(file)
			size = str(os.path.getsize(file)) + ' B'
			ctime = time.ctime(os.path.getmtime(file))
			dir = os.path.dirname(file)

			item = (name, size, ctime, dir)
			index = self.InsertStringItem(sys.maxint, item[0])
			for col, text in enumerate(item[1:]):
				self.SetStringItem(index, col+1, text)
			self.SetItemData(index, index)
			self.itemDataMap[index] = item

def find_str(mylist, str):
	ret_list = []
	for x in mylist:
		flag = True
		name = os.path.basename(x)
		for y in str.strip().split():
			s = name.find(y)
			if s == -1:
				break
		else:
			ret_list += [x]

	return ret_list


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "")
        # self.list_ctrl_1 = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.list_ctrl_1 = MyListCtrl(self, -1)

        self.__set_properties()
        self.__do_layout()
	self.files = open('files.db').readlines()
	self.files = [ x.strip() for x in self.files ]
	self.list_ctrl_1.set_value(self.files)
	self.valstr = []

        self.Bind(wx.EVT_TEXT, self.doSearch, self.text_ctrl_1)

	self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onItemSelected, self.list_ctrl_1)
	self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.onItemDeselected, self.list_ctrl_1)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onOpenItem, self.list_ctrl_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("SPFind: Simple PyFind")
        self.SetSize((680, 392))
        self.list_ctrl_1.SetMinSize((680, 355))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.text_ctrl_1, 0, wx.EXPAND, 0)
        sizer_2.Add(self.list_ctrl_1, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def onItemSelected(self, event):
	self.select = event.GetIndex()
	#print 'self.select:', self.select

    def onItemDeselected(self, event):
	#self.select = event.GetIndex
	pass

    def onOpenItem(self, event):
	#index = event.GetIndex()
	index = self.select
	name = self.list_ctrl_1.GetItem(index).GetText()
	dir = self.list_ctrl_1.GetItem(index, DIR_COL).GetText()
	print 'Selected %s' %(os.path.join(dir, name))
	file = os.path.join(dir, name)
	tool.openfile(file)

    def doSearch(self, event): # wxGlade: MyFrame.<event_handler>
	self.list_ctrl_1.DeleteAllItems()

	self.search_str = self.text_ctrl_1.GetValue()
	#print self.search_str

	file_list = find_str(self.files, self.search_str)
	self.list_ctrl_1.set_value(file_list)
	# print file_list
        # event.Skip()

#    def onOpenItem(self, event): # wxGlade: MyFrame.<event_handler>
#        print "Event handler `onOpenItem' not implemented!"
#        event.Skip()

# end of class MyFrame


if __name__ == "__main__":
    spfind = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    spfind.SetTopWindow(frame_1)
    frame_1.Show()
    spfind.MainLoop()
