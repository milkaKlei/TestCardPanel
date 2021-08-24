import time
from selenium import webdriver
desired_caps = {}
desired_caps["app"] = r"C:\Users\מלכה\Desktop\CardPanel.exe"
desired_caps["platformName"] = "Windows"
desired_caps["deviceName"] = "WindowsPC"
driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
cardPanel=driver.window_handles[0]
driver.switch_to_window(cardPanel)
def test(num):
     driver.find_element_by_name("Loop").click()
     flag = True
     preCard=""
     card=""
     counter=0
     while flag:
        preCard=driver.find_elements_by_class_name("TCard")[0].get_attribute("Name")
        driver.find_element_by_name("Next Card").click()
        time.sleep(1)
        card=driver.find_elements_by_class_name("TCard")[0].get_attribute("Name")
        counter+=1
        if card==preCard:
            flag=False
     if counter==int(num):
                 print("Succeeded")
     else:
                 print("failed")      
     driver.quit()
test(6)
   
     

 





    
   
