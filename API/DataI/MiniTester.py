#
# cells1 = [CellModel('السعر', enums.CellType.string.value),
#         CellModel(10, enums.CellType.numeric.value),
#         CellModel(20, enums.CellType.numeric.value),
#         CellModel(20, enums.CellType.numeric.value),
#         CellModel(20, enums.CellType.numeric.value),
#         CellModel(15, enums.CellType.numeric.value),
#         CellModel(15, enums.CellType.numeric.value),
#         CellModel(10, enums.CellType.numeric.value),
#         CellModel(10, enums.CellType.numeric.value)
#          ]
#
# cells2 = [CellModel('Col2', enums.CellType.string.value),
#         CellModel(2, enums.CellType.numeric.value),
#         CellModel(2, enums.CellType.numeric.value),
#         CellModel(2, enums.CellType.numeric.value),
#         CellModel(2, enums.CellType.numeric.value),
#         CellModel(2, enums.CellType.numeric.value),
#         CellModel(2, enums.CellType.numeric.value),
#         CellModel(2, enums.CellType.numeric.value),
#         CellModel(2, enums.CellType.numeric.value)
#          ]
#
# col1 = ColumnModel(cells1, 'السعر', 0, False)
# col2 = ColumnModel(cells2, 'Col2', 1, False)
#
# col = '0' / col1
#
# cell1 = CellModel(7, enums.CellType.numeric.value)
# cell2 = CellModel(2, enums.CellType.numeric.value)
#
#
#
# for cell in col.cells:
#         print(cell)

# cell1 = CellModel(10, enums.CellType.numeric.value)
# cell2 = CellModel(-5, enums.CellType.numeric.value)
#
# print(cell1 + cell2)
# print(cell2 + cell1)
#
#
# import datetime
# import re
#
# from dateutil.parser import parse
#
# from DataI import enums
# from DataI.Models.ColumnModel import CellModel, ColumnModel
#
# date1 = '22/1/2000'
# date2 = '2000-01-22 00:00:00'
#
#
# try:
#     dateObj1 = parse(date1, fuzzy=False)
#     print(dateObj1)
#     print(date2[:4])
# except ValueError:
#     print('not date')

crap = '''<?xml version=\"1.0\" encoding=\"iso-8859-1\"?><!-- Generator: Adobe Illustrator 19.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  --><svg version=\"1.1\" id=\"Capa_1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\" viewBox=\"0 0 512.013 512.013\" style=\"enable-background:new 0 0 512.013 512.013;\" xml:space=\"preserve\"><g><g><circle cx=\"42.68\" cy=\"224.006\" r=\"42.667\"/></g></g><g><g><path d=\"M341.346,202.673c-5.888,0-10.667,4.779-10.667,10.667s4.779,10.667,10.667,10.667c87.509,0,149.333,80.043,149.333,96c0,5.888,4.779,10.667,10.667,10.667c5.888,0,10.667-4.779,10.667-10.667C512.013,286.94,436.322,202.673,341.346,202.673z\"/></g></g><g><g><path d=\"M501.346,309.34H405.09c-14.251,0-26.56-9.173-30.677-22.805l-23.552-77.973l-21.333-42.667c-1.792-3.605-5.483-5.888-9.515-5.888h-32c-2.837,0-5.547,1.131-7.552,3.115l-39.531,39.552H74.68c-5.888,0-10.667,4.779-10.667,10.667v21.333c0,5.205,3.776,9.664,8.917,10.517c39.083,6.528,105.621,22.549,120.896,38.272l0.683,1.323c20.16,39.467,45.269,88.555,93.504,88.555h149.333c42.56,0,74.667-22.933,74.667-53.333C512.013,314.118,507.234,309.34,501.346,309.34z\"/></g></g><g><g><path d=\"M63.224,188.529L41.89,145.862c-2.517-5.035-8.576-7.232-13.781-4.971l-21.653,9.323c-5.077,2.197-7.659,7.915-5.909,13.163l10.667,32c1.899,5.589,7.957,8.597,13.504,6.741c4.331-1.429,7.04-5.376,7.211-9.685l9.557,0.384l2.645,5.269c1.877,3.733,5.653,5.888,9.536,5.888c1.6,0,3.221-0.363,4.779-1.131C63.714,200.198,65.847,193.798,63.224,188.529z\"/></g></g><g><g><path d=\"M58.125,246.47c-5.248-2.581-11.669-0.491-14.315,4.779l-1.344,2.645c-0.981-4.885-5.291-8.555-10.453-8.555c-5.888,0-10.667,4.779-10.667,10.667v21.333c0,5.888,4.779,10.667,10.667,10.667H42.68c4.032,0,7.723-2.283,9.536-5.888l10.667-21.333C65.506,255.516,63.394,249.094,58.125,246.47z\"/></g></g><g><g><path d=\"M309.346,96.006c-5.888,0-10.667,4.779-10.667,10.667v10.667c0,5.888,4.779,10.667,10.667,10.667s10.667-4.779,10.667-10.667v-10.667C320.013,100.785,315.234,96.006,309.346,96.006z\"/></g></g><g><g><path d=\"M501.346,117.34h-192c-5.888,0-10.667,4.779-10.667,10.667s4.779,10.667,10.667,10.667h192c5.888,0,10.667-4.779,10.667-10.667S507.234,117.34,501.346,117.34z\"/></g></g><g><g><path d=\"M309.346,117.34h-192c-5.888,0-10.667,4.779-10.667,10.667s4.779,10.667,10.667,10.667h192c5.888,0,10.667-4.779,10.667-10.667S315.234,117.34,309.346,117.34z\"/></g></g><g><g><path d=\"M352.013,352.006c-5.888,0-10.667,4.779-10.667,10.667v42.667c0,5.888,4.779,10.667,10.667,10.667c5.888,0,10.667-4.779,10.667-10.667v-42.667C362.68,356.785,357.901,352.006,352.013,352.006z\"/></g></g><g><g><path d=\"M437.346,352.006c-5.888,0-10.667,4.779-10.667,10.667v42.667c0,5.888,4.779,10.667,10.667,10.667c5.888,0,10.667-4.779,10.667-10.667v-42.667C448.013,356.785,443.234,352.006,437.346,352.006z\"/></g></g><g><g><path d=\"M506.552,374.705c-5.141-2.88-11.648-1.045-14.528,4.096c-5.056,9.024-25.664,14.656-33.344,15.872H245.346c-5.888,0-10.667,4.779-10.667,10.667c0,5.888,4.779,10.667,10.667,10.667l214.805-0.107c3.947-0.555,38.912-5.995,50.496-26.688C513.527,384.07,511.693,377.585,506.552,374.705z\"/></g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g></svg>'''


crap = crap.replace('\n', '')
crap = crap.replace('\t', '')
crap = crap.encode('latin1').decode('unicode-escape').encode('latin1').decode('utf-8')

print(crap)













