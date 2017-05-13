#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from sgmllib import SGMLParser
import os, sys, urllib, httplib, re, urllib2, sets, socket, subprocess, ConfigParser
from termcolor import colored

xss = (
	"<SCrIpT>alert('XSS')</ScRiPt>",
	"%22%3Cscript%3Ealert%28%27XSS%27%29%3C%2Fscript%3E",
	"<IMG SRC=javascript:alert('XSS')>",
)
