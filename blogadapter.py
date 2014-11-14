#!/usr/bin/python
# coding=cp936
#
# Copyright (C) 2014 Wenva <lvyexuwenfa100@126.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is furnished
# to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import os,sys,re,time

class blog:
    def __init__(self, filename, title, date):
        self.filename = filename
        self.title = title
        self.date = date

list = os.listdir(".")

linklist = []
ignorelist = ['\.', 'README.md', 'blogadapter.py', 'sync.sh']

output = open('README.md', 'w')

output.write('# Pawpaw\'s Blogs\n')
output.write('This repository is used to store my blogs\n')
output.write('## Usage\n')
output.write('* crontab -e\
             ```* * * * * * * yourdir/sync.sh```\
              * blog format\
                <pre>\
                    # Title\
                    Date(xxxx-xx-xx)\
                    ...\
                </pre>\
             ')

bloglist = []
for file in list:
    match = False
    for ignore in ignorelist:
        if (re.match(ignore, file)):
            match = True
            break
    if (match == False):
        filefd = open(file, 'r')
        blogname = filefd.readline()[1:-1]
        blogdate = time.strptime(filefd.readline()[:-1], '%Y-%m-%d')
        bloglist.append(blog(str(file), blogname, blogdate))
        filefd.close()

# sorted newer to top
bloglist = sorted(bloglist, cmp = lambda x,y: cmp(x.date, y.date), reverse=True)
lastyear = 0
lastmonth = 0
for obj in bloglist:
    if (lastyear != obj.date.tm_year):
        output.write('## ' + str(obj.date.tm_year) + '\n')
        lastyear = obj.date.tm_year

    if (lastmonth != obj.date.tm_mon ):
        output.write('##### ' + str(obj.date.tm_year) + '-'  + str(obj.date.tm_mon) + '\n')
        lastmonth = obj.date.tm_mon

    output.write('###### [' + obj.title  + '][]\n')
    linklist.append('[' + obj.title + ']:' + obj.filename + '\n')

    print(obj.filename)

for link in linklist:
    output.write(link)

output.close()

