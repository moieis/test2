
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pywebio import config
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from anticaptchaofficial.recaptchav2proxyless import *
import telebot






 
print('dfdfdfdfggggggggggggggggggdkkdjfffffffffffffffffffffffff')
        



bot = telebot.TeleBot("7199127665:AAHflk6KytAKmxYBnPMssCNkhJO7h9mRRYM")
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, " مرحبا بك اسمي موي بوت !!\n قم بارسال رابط حساب الملف الشخصي من التيك تاك لاقوم بسحب البيانات لك \n⚠️ الرجاء عدم الاسائة والسعي للصلاح فلنا ولكم لقاء في يوما تشخص فيه الابصار .....  \n \n\n Hoi, my name is MoiBot :) !!\n*Send me the link of the profile account from tiktak to scrap the data for you. \n⚠️ Please do not offend and strive for goodness, We and you will meet on a day when the eyes will be blinded by the horror of the scene. .....")
    print(message)


print('hi')

def me(message):
    return True


@bot.message_handler(func=me)
def send_welme(message):
    print(message.text[0:4], message)
    if message.text[0:18] in ['http',' htt','https://www.tiktok'] :
        bot.reply_to(message, "⌛⏳")
        
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(executable_path=r'/app/.chrome-for-testing/chromedriver-linux64/chromedriver', chrome_options=chrome_options)
        bot.reply_to(message, "⏳⌛")
        
        
        # 
        
        
        
        
        
        
        url="https://shreateh.net/tiktok-applications/tiktok-osint.html"
        driver.get(url)
        time.sleep(3)
        bot.reply_to(message, "⌛⏳")
        driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/div[1]/div[2]/div[2]/button[1]').click()
        
        
        
        
        sitekey = driver.find_element(By.CLASS_NAME, 'g-recaptcha').get_attribute('outerHTML')
        sitekey_clean = sitekey.split('" data-callback')[0].split('data-sitekey="')[1].split('"')[0]
        print(sitekey_clean)
        solver = recaptchaV2Proxyless()
        solver.set_verbose(1)
        solver.set_key('01c2cd874b3584d75d8364c7cb3dd5ff')
        solver.set_website_url(url)
        solver.set_website_key(sitekey_clean)
        
        g_response = solver.solve_and_return_solution()
        if g_response!= 0:
            print("g_response"+g_response)
            bot.reply_to(message, "HERE WE GO !✅︎")

            
        else:
            print("task finished with error"+solver.error_code)
    
        driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')
        
        driver.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""", g_response)
        driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')
        
        profile=driver.find_element(By.ID,'khalil_vid')
        profile.send_keys('https://www.tiktok.com/@omarsbshlen?is_from_webapp=1&sender_device=pc')
        
        time.sleep(3)
        bot.reply_to(message, "⏳")
        
        boton = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/main/div/div[2]/p[6]/input')
        boton.screenshot('foo.png')
        boton.click()
        bot.reply_to(message, "CREATED BY MOIBOT TELG ®FREE ;) ⏳")
        time.sleep(5)
        try:
            
            reso = driver.find_element(By.XPATH,'//*[@id="kresult"]/div').text
            bot.reply_to(message, "⌛ DONE NXSAN ...... Row Data")
            bot.reply_to(message, reso.spilt(' '))
            driver.close()
            
        except:
            reso = driver.find_element(By.XPATH,'//*[@id="kresult"]').text
            bot.reply_to(message, "⌛ DONE NXSAN ...... Row Data")
            bot.reply_to(message, reso.spilt(' '))
            driver.close()
         
         
            
        
            
    elif len(message.text) == 1:
        bot.reply_to(message, "😝")
    elif len(message.text) == 2:
        bot.reply_to(message, "😝😝")
    elif len(message.text) < 4 or len(message.text) < 3 or len(message.text) < 2:
        bot.reply_to(message, "😆😆😆😆😆")
    
    else:
        bot.reply_to(message, "❌الرجاء ارسال رابط الملف الشخصي يجب ان يبدأ  [https://www.tiktok]❌\n\n\n❌ please enter valid link Must start with [https://www.tiktok]❌")



bot.polling()
