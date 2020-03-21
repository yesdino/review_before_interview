[toc]

---

#### easyxf
```
sheet.write(0, 0, xlwt.easyxf('font: bold 1')) # bold
sheet.write(0, 0, xlwt.easyxf('font: bold 1, color: blue, underline single')) 
```

#### 简单例子
```python
import xlwt
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')
worksheet.write(0, 0, label = 'Row 0, Column 0 Value')
workbook.save('Excel_Workbook.xls')
```

#### 一个单元格格式
```python
import xlwt
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')
font = xlwt.Font()              # Create the Font
font.name = 'Times New Roman'   
font.bold = True                #粗体
font.underline = True           #下划线
font.italic = True              #斜体
font.height = 720               #高度
style = xlwt.XFStyle()          # Create the Style
style.font = font               # Apply the Font to the Style
worksheet.write(0, 0, label = 'Unformatted value')
worksheet.write(1, 0, label = 'Formatted value', style) # Apply theStyle to the Cell
workbook.save('Excel_Workbook.xls')
```

#### font object 的属性
```
font.bold = True            # May be: True, False
font.italic = True          # May be: True, False
font.struck_out = True      # May be: True, False
font.underline = xlwt.Font.UNDERLINE_SINGLE         # May be:UNDERLINE_NONE, UNDERLINE_SINGLE, UNDERLINE_SINGLE_ACC,UNDERLINE_DOUBLE, UNDERLINE_DOUBLE_ACC
font.escapement = xlwt.Font.ESCAPEMENT_SUPERSCRIPT  # May be:ESCAPEMENT_NONE, ESCAPEMENT_SUPERSCRIPT, ESCAPEMENT_SUBSCRIPT
font.family = xlwt.Font.FAMILY_ROMAN                # May be: FAMILY_NONE,FAMILY_ROMAN, FAMILY_SWISS, FAMILY_MODERN, FAMILY_SCRIPT,FAMILY_DECORATIVE
font.charset = xlwt.Font.CHARSET_ANSI_LATIN         # May be:CHARSET_ANSI_LATIN, CHARSET_SYS_DEFAULT, CHARSET_SYMBOL,CHARSET_APPLE_ROMAN, CHARSET_ANSI_JAP_SHIFT_JIS,CHARSET_ANSI_KOR_HANGUL, CHARSET_ANSI_KOR_JOHAB,CHARSET_ANSI_CHINESE_GBK, CHARSET_ANSI_CHINESE_BIG5,CHARSET_ANSI_GREEK, CHARSET_ANSI_TURKISH, CHARSET_ANSI_VIETNAMESE,CHARSET_ANSI_HEBREW, CHARSET_ANSI_ARABIC, CHARSET_ANSI_BALTIC,CHARSET_ANSI_CYRILLIC, CHARSET_ANSI_THAI, CHARSET_ANSI_LATIN_II,CHARSET_OEM_LATIN_I
font.colour_index = ?
font.get_biff_record = ?
font.height = 0x00C8    # C8 in Hex (in decimal) = 10 points inheight.
font.name = ?
font.outline = ?
font.shadow = ?
```
#### 单元格宽度
```python
import xltw
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
worksheet.write(0, 0, 'My Cell Contents')
worksheet.col(0).width = 3333               #3333 = 1" (one inch).
workbook.save('Excel_Workbook.xls')
```
#### 日期格式
```python
import xlwt
import datetime
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
style = xlwt.XFStyle()
style.num_format_str = 'M/D/YY' # Other options: D-MMM-YY, D-MMM,MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss,[h]:mm:ss, mm:ss.0
worksheet.write(0, 0, datetime.datetime.now(), style)
workbook.save('Excel_Workbook.xls')
```
#### 公式
```python
import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
worksheet.write(0, 0, 5) # Outputs 5
worksheet.write(0, 1, 2) # Outputs 2
worksheet.write(1, 0, xlwt.Formula('A1*B1')) # Should output "10"(A1[5] * A2[2])
worksheet.write(1, 1, xlwt.Formula('SUM(A1,B1)')) # Should output"7" (A1[5] + A2[2])
workbook.save('Excel_Workbook.xls')
```
#### 超链接格式
```python
import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
worksheet.write(0, 0,xlwt.Formula('HYPERLINK("http://www.google.com";"Google")')) #Outputs the text "Google" linking to http://www.google.com
workbook.save('Excel_Workbook.xls')
```
#### 合并列和行
```python
import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
worksheet.write_merge(0, 0, 0, 3, 'First Merge') # Merges row 0'scolumns 0 through 3.
font = xlwt.Font()          
font.bold = True 
style = xlwt.XFStyle() 
style.font = font 
worksheet.write_merge(1, 2, 0, 3, 'Second Merge', style) # Mergesrow 1 through 2's columns 0 through 3.
workbook.save('Excel_Workbook.xls')
```
#### 对齐
```python
import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
alignment = xlwt.Alignment()                # Create Alignment
alignment.horz = xlwt.Alignment.HORZ_CENTER # May be: HORZ_GENERAL,HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED,HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.vert = xlwt.Alignment.VERT_CENTER # May be: VERT_TOP,VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
style = xlwt.XFStyle() 
style.alignment = alignment                 # Add Alignment to Style
worksheet.write(0, 0, 'Cell Contents', style)
workbook.save('Excel_Workbook.xls')
```
#### 边框
```python
# Please note: While I was able to find these constants within thesource code, on my system (using LibreOffice,) I was only presentedwith a solid line, varying from thin to thick; no dotted or dashedlines.
import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
borders = xlwt.Borders()            # Create Borders
borders.left = xlwt.Borders.DASHED  # May be: NO_LINE, THIN, MEDIUM,DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED,THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED,MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through0x0D.
borders.right = xlwt.Borders.DASHED
borders.top = xlwt.Borders.DASHED
borders.bottom = xlwt.Borders.DASHED
borders.left_colour = 0x40
borders.right_colour = 0x40
borders.top_colour = 0x40
borders.bottom_colour = 0x40
style = xlwt.XFStyle()          # Create Style
style.borders = borders         # Add Borders to Style
worksheet.write(0, 0, 'Cell Contents', style)
workbook.save('Excel_Workbook.xls')
```
#### 背景颜色
```python
import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
pattern = xlwt.Pattern()                    # Create the Pattern
pattern.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN,SOLID_PATTERN, or 0x00 through 0x12
pattern.pattern_fore_colour = 5             # May be: 8 through 63. 0 = Black,1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7= Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = DarkYellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = LightGray, 23 = Dark Gray, the list goes on...
style = xlwt.XFS
```


