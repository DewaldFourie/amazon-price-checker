import locale
import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


MY_EMAIL = "mayonaiseketties33@gmail.com"
MY_PASSWORD = "ocrfjymhpxtarcuv"
MONITOR_URL = "https://www.takealot.com/lg-lge27mp400-27-fhd-monitor/PLID90524470"

chrome_driver_path = r"C:\Users\Dewald\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

driver.get(MONITOR_URL)
price_element = driver.find_element(by="xpath", value='//*[@id="shopfront-app"]/div[3]/div[1]/div[2]/aside/div[1]/div'
                                                      '[1]/div[1]/span')
price = price_element.text.strip().replace("R ", "")
price_final = locale.atof(price)
print(price_final)

if price_final < 3200:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="dewald_f@yahoo.com", msg=f"Subject: LG LGE27MP400 27' FHD"
                                                                                   f" Monitor \n\n"
                                                                                   f"Current price: R{price}\n\n"
                                                                                   f"Available at: {MONITOR_URL}")

driver.quit()