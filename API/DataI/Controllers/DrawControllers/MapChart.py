import drawSvg as draw
from numpy import double, os

from xml.dom import minidom

from DataI import enums
from DataI.Controllers.DrawControllers.InfChart import InfChart
from DataI.Models.ColumnModel import ColumnModel
from DataI.Models.TableModel import TableModel


class MapChart():
    def __init__(self, dataSource: TableModel, XColumn: ColumnModel, width: double, height: double, nameFile: str):
        self.metaData = list()
        self.listOfPercentageValue =dict()
        self.widthView = 1000
        self.heightView = 600
        self.dataSourceTableWithoutXcolumn = dataSource
        self.xColumn = XColumn
        self.keyColumn = self.findKeyColumn()

        print("xColumn:",XColumn.name,XColumn.id)
        print("keycolumn:",self.keyColumn.name)
        if self.keyColumn != self.xColumn:
          self.colorList = self.dataSourceTableWithoutXcolumn.rowsColors
          self.listOfLength = list()
          self.d = draw.Drawing(self.widthView , self.heightView)
          self.total = self.sumColumn(self.xColumn)
          self.drawlayOut()
          self.drawHuman()
        else:
          self.d.append(draw.Text(text="Error: you have to select keyCountries in columns", fontSize=60, x=50, y=self.heightView / 2))
        self.d.setPixelScale(min(width,height)/600)  # Set number of pixels per geometry unit
        self.d.saveSvg('dr.svg')
        self.SVG = self.d.asSvg()

    def drawlayOut(self):
        self.d.append(draw.Rectangle(0, 0, self.widthView , self.heightView, fill='#ffffff'))

    def drawHuman(self):
      ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
      doc = minidom.parse(str(ROOT_DIR)+"/m.svg")
      path_id = [path.getAttribute('id') for path
                 in doc.getElementsByTagName('path')]
      path_data = [path.getAttribute('d') for path
                   in doc.getElementsByTagName('path')]
      doc.unlink()
      for path, id in zip(path_data, path_id):
        # print(id,"  ",self.getPercentageOfCountryKey(str(id)),"::: ",self.CorrectPercentageOfValue(self.getPercentageOfCountryKey(str(id))))
        self.d.append(draw.Path(stroke_width=0,id=id, stroke="white", fill="blue",
                                fill_opacity=self.getPercentageOfCountryKey(str(id))/80,d=path
                                , transform="translate(-25,-700) scale(0.8 0.8)" ))
        self.d.append(draw.Path(stroke_width=1, id=id, stroke="white", fill="gray",
                                fill_opacity=0.2, d=path
                                , transform="translate(-25,-700) scale(0.8 0.8)"))

    def findKeyColumn(self)->ColumnModel:
      for column in self.dataSourceTableWithoutXcolumn.columns:
        if column.name == 'geoId' or column.name == 'GeoId' or column.name == 'GEOId' :
          self.dataSourceTableWithoutXcolumn.columns.pop(column.id)
          return column
      return self.xColumn
    def getPercentageOfCountryKey(self,key:str)->double:
      if (self.findIndexForCountryBykey(key) == -1):
        return double(0)
      else:
        return self.percentageOfValue(double(self.xColumn.cells[self.findIndexForCountryBykey(key)].value))


    def percentageOfValue(self, value: double) -> double:
      return double((abs(value) / self.total) * 100)

    def CorrectPercentageOfValue(self, value: double) -> int:
        return int((int(abs(value)*100))/ 100)

    def findIndexForCountryBykey(self,key:str)->int:
      i=-1
      for cell in self.keyColumn.cells:
        i += 1
        if key == cell.value:
          return i
      return -1

    def sumColumn(self, column: ColumnModel) -> double:
      Max = 0
      for cell in self.xColumn.cells:
        if (cell.type == enums.CellType.numeric.value):
          if (double(cell.value) > Max):
            Max = double(cell.value)
      return Max




# /usr/bin/python3.8 /home/kareem/University/Project1/web/API/DataI/Controllers/DrawControllers/testingUnit.py
# AF    0.6358249772105743 :::  0
# AO    0.01823154056517776 :::  0
# AL    0.15724703737465814 :::  0
# AE    0.9594348222424794 :::  0
# AR    5.154968094804011 :::  5
# AM    0.9457611668185961 :::  0
# AU    0.1526891522333637 :::  0
# AT    0.2529626253418414 :::  0
# AZ    1.2670920692798542 :::  1
# BI    0.0 :::  0
# BE    0.18687329079307202 :::  0
# BJ    0.027347310847766634 :::  0
# BF    0.006836827711941659 :::  0
# BD    8.391066545123063 :::  8
# BG    0.3600729261622607 :::  0
# BA    0.2506836827711942 :::  0
# BY    0.7474931631722881 :::  0
# BZ    0.00911577028258888 :::  0
# BO    2.4931631722880585 :::  2
# BR    77.1330902461258 :::  77
# BN    0.0 :::  0
# BT    0.0 :::  0
# BW    0.11850501367365542 :::  0
# CF    0.300820419325433 :::  0
# CA    0.6517775752051048 :::  0
# CH    0.14129443938012762 :::  0
# CL    7.734731084776664 :::  7
# CN    0.011394712853236098 :::  0
# CI    0.6494986326344576 :::  0
# CM    0.0 :::  0
# CD    0.22561531449407476 :::  0
# CG    0.0 :::  0
# CO    6.387876025524157 :::  6
# CR    0.4329990884229718 :::  0
# CU    0.00227894257064722 :::  0
# CZ    0.33956244302643573 :::  0
# DE    1.0619872379216042 :::  1
# DJ    0.05925250683682771 :::  0
# DK    0.038742023701002735 :::  0
# DO    1.7137648131267094 :::  1
# DZ    0.7657247037374658 :::  0
# EC    1.7479489516864173 :::  1
# EG    3.548313582497721 :::  3
# ER    0.027347310847766634 :::  0
# EE    0.00455788514129444 :::  0
# ET    0.0 :::  0
# FI    0.011394712853236098 :::  0
# FJ    0.0 :::  0
# GA    0.0 :::  0
# GB    0.0 :::  0
# GE    0.0 :::  0
# GH    0.8887876025524157 :::  0
# GN    0.09115770282588878 :::  0
# GM    0.0 :::  0
# GW    0.09115770282588878 :::  0
# GQ    0.0 :::  0
# GR    0.0 :::  0
# GL    0.0 :::  0
# GT    1.56563354603464 :::  1
# GY    0.022789425706472195 :::  0
# HN    1.6864175022789425 :::  1
# HR    0.11850501367365542 :::  0
# HT    0.09571558796718323 :::  0
# HU    0.022789425706472195 :::  0
# ID    2.946672743846855 :::  2
# IN    42.50911577028259 :::  42
# IE    0.025068368277119415 :::  0
# IR    5.599361896080219 :::  5
# IQ    4.462169553327256 :::  4
# IS    0.00455788514129444 :::  0
# IL    1.8299908842297172 :::  1
# IT    0.32360984503190515 :::  0
# JM    0.00911577028258888 :::  0
# JO    0.00911577028258888 :::  0
# JP    0.29626253418413856 :::  0
# KZ    43.86052871467639 :::  43
# KE    0.40109389243391064 :::  0
# KG    1.0004557885141294 :::  1
# KH    0.0 :::  0
# KR    0.11394712853236097 :::  0
# KW    1.5291704649042843 :::  1
# LA    0.0 :::  0
# LB    0.07520510483135825 :::  0
# LR    0.022789425706472195 :::  0
# LY    0.14129443938012762 :::  0
# LK    0.011394712853236098 :::  0
# LS    0.0 :::  0
# LT    0.00227894257064722 :::  0
# LU    0.09799453053783046 :::  0
# LV    0.00227894257064722 :::  0
# MA    0.5537830446672743 :::  0
# MD    0.5834092980856883 :::  0
# MG    0.1731996353691887 :::  0
# MX    12.379216043755697 :::  12
# MK    0.2871467639015497 :::  0
# ML    0.01823154056517776 :::  0
# MM    0.0 :::  0
# ME    0.10711030082041934 :::  0
# MN    0.0 :::  0
# MZ    0.013673655423883317 :::  0
# MR    0.0 :::  0
# MW    0.09343664539653601 :::  0
# MY    0.00455788514129444 :::  0
# NA    0.0 :::  0
# NE    0.0 :::  0
# NG    1.2784867821330903 :::  1
# NI    0.7953509571558796 :::  0
# NL    0.11394712853236097 :::  0
# NO    0.022789425706472195 :::  0
# NP    0.7201458523245214 :::  0
# NZ    0.0 :::  0
# OM    2.3017319963536917 :::  2
# PK    9.418869644484959 :::  9
# PA    1.7433910665451229 :::  1
# PE    6.4904284412032816 :::  6
# PH    2.452142206016408 :::  2
# PG    0.0 :::  0
# PL    0.5446672743846855 :::  0
# KP    0.0 :::  0
# PT    0.5218778486782133 :::  0
# PY    0.06836827711941659 :::  0
# PS    0.7338195077484048 :::  0
# QA    2.2379216043755696 :::  2
# RO    0.8842297174111212 :::  0
# RU    15.252962625341842 :::  15
# RW    0.05469462169553327 :::  0
# EH    0.39197812215132183 :::  0
# SA    9.997721057429352 :::  9
# SD    0.0 :::  0
# SS    0.0 :::  0
# SN    0.2164995442114859 :::  0
# SL    0.027347310847766634 :::  0
# SV    0.6039197812215132 :::  0
# RS    0.6289881494986326 :::  0
# SR    0.03646308113035552 :::  0
# SK    0.00455788514129444 :::  0
# SI    0.034184138559708296 :::  0
# SE    1.7866909753874203 :::  1
# SZ    0.038742023701002735 :::  0
# SY    0.022789425706472195 :::  0
# TD    0.0 :::  0
# TG    0.01595259799453054 :::  0
# TH    0.00455788514129444 :::  0
# TJ    0.12306289881494985 :::  0
# TM    0.0 :::  0
# TL    0.0 :::  0
# TN    0.00455788514129444 :::  0
# TR    2.946672743846855 :::  2
# TW    0.0 :::  0
# TZ    0.0 :::  0
# UG    0.043299908842297175 :::  0
# UA    3.122151321786691 :::  3
# UY    0.00911577028258888 :::  0
# US    100.0 :::  100
# UZ    0.7497721057429353 :::  0
# VE    0.6882406563354603 :::  0
# VN    0.0 :::  0
# VU    0.0 :::  0
# YE    0.06836827711941659 :::  0
# ZA    15.827256153144942 :::  15
# ZM    0.05925250683682771 :::  0
# ZW    0.038742023701002735 :::  0
# SO    0.04557885141294439 :::  0
# GF    0.0 :::  0
# FR    1.2329079307201458 :::  1
# ES    0.8842297174111212 :::  0
# AW    0.0 :::  0
# AI    0.0 :::  0
# AD    0.0 :::  0
# AG    0.0 :::  0
# BS    0.0 :::  0
# BM    0.0 :::  0
# BB    0.0 :::  0
# KM    0.07064721969006381 :::  0
# CV    0.14129443938012762 :::  0
# KY    0.00227894257064722 :::  0
# DM    0.0 :::  0
# FK    0.0 :::  0
# FO    0.0 :::  0
# GD    0.0 :::  0
# HK    0.0 :::  0
# KN    0.0 :::  0
# LC    0.0 :::  0
# LI    0.0 :::  0
# MV    0.056973564266180485 :::  0
# MT    0.0 :::  0
# MS    0.0 :::  0
# MU    0.0 :::  0
# NC    0.0 :::  0
# NR    0.0 :::  0
# PN    0.0 :::  0
# PR    0.48997265268915224 :::  0
# SG    0.5606198723792161 :::  0
# SB    0.0 :::  0
# ST    0.00227894257064722 :::  0
# SX    0.0 :::  0
# SC    0.0 :::  0
# TC    0.0 :::  0
# TT    0.00911577028258888 :::  0
# VC    0.0 :::  0
# VG    0.0 :::  0
# VI    0.0 :::  0
# CY    0.00455788514129444 :::  0
# RE    0.0 :::  0
# YT    0.0 :::  0
# MQ    0.0 :::  0
# GP    0.0 :::  0
# CW    0.00227894257064722 :::  0
# IC    0.0 :::  0
#
# Process finished with exit code 0
