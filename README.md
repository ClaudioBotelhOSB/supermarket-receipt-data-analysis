# Supermarket Receipt Data Analysis

An application to extract data from a supermaket receipt image, analyse and manipulate the data amd create an intuitive Google Sheets.
All data will be categorized to the user track where exactly his money is being spent. Also, the user will be able to monitor market price variation and the price between different markets.

**Development steps:**
  * Extract data from a supermaket receipt image. :heavy_check_mark:
    * Image processing, thresholding and text detect/highlight. :heavy_check_mark:
    * Write a TXT and a CSV file. :heavy_check_mark:
    * _Libs: OpenCV and Pytesseract._
  * Analyse and manipulate the data.
    * Get only the main information.
    * Libs: Pandas.
  * Send the data to Google Sheets
    * Create a Database Sheets to visualize all data easily.
    * Libs: Google Scripts.
  
<br><br>
<table style="width:100%">
  <tr>
    <th>Original Receipt Image</th>
    <th>Highlighted Receipt Image</th> 
  </tr>
  <tr>
    <td><img src="https://github.com/ClaudioBotelhOSB/supermarket-receipt-data-analysis/blob/main/receipt.jpg" width="240" title="Original Receipt Image"></th>
    <td><img src="https://github.com/ClaudioBotelhOSB/supermarket-receipt-data-analysis/blob/main/receipt_highlighted.png" width="240" title="Highlighted Receipt Image"></th>
  </tr>
</table>


_Currently in development._
