from selenium import webdriver
import time
import unittest
import re
import xlrd

# 打开豆瓣电影，测一下前5本电影的片名和导演名字

driver = webdriver.Chrome()
book = xlrd.open_workbook(r"C:\Users\mshacxiang\VScode_project\python_learn\web_learn\01.xlsx")
sheet = book.sheet_by_index(0)

class DouBan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        url = driver.get("https://movie.douban.com/top250")
    
    def test_a_locat_movie(self):
        dict1={}
        for i in range(1,6):
            css_movie = ".grid_view>li:nth-child("+str(i)+")>.item>.info>.hd>a>span:nth-child(1)"
            css_director = ".grid_view>li:nth-child("+str(i)+")>.item>.info>.bd>p:nth-child(1)"
            text_movie = driver.find_element_by_css_selector(css_movie).text
            text_director = driver.find_element_by_css_selector(css_director).text
            pattern = "导演:(.*?)主演"
            vaild_text = re.compile(pattern).findall(text_director)
            vaild_text = vaild_text[0].strip()
            dict1[text_movie] = vaild_text
        return dict1
        # print("dict1:",dict1)

    def test_b_excel(self):
        book = xlrd.open_workbook(r"C:\Users\mshacxiang\VScode_project\python_learn\web_learn\01.xlsx")
        sheet = book.sheet_by_index(0)
        dict = {}
        for row in range(1,sheet.nrows):
            # for col  in range(sheet.ncols):
                #输出所有的内容
                # cell = sheet.cell_value(row,col)
                # print(cell)
            movie = sheet.cell_value(row,0)
            director = sheet.cell_value(row,1)
            dict[movie]= director
        return dict
        # print("dict:",dict)

    def test_c(self):
        self.assertEqual(self.test_a_locat_movie(), self.test_b_excel())



    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        driver.close()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(DouBan("test_a_locat_movie"))
    suite.addTest(DouBan("test_b_excel"))
    suite.addTest(DouBan("test_c"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

