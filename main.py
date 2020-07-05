import smtplib
smtp=smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
print('''
 _____             _     _
|_   _|__ _ __ ___| |__ (_)
  | |/ _ \ '__/ __| '_ \| |
  | |  __/ |  \__ \ | | | |
  |_|\___|_|  |___/_| |_|_|
    ''')
mail = input('你的Gmail信箱:')
pw = input('你的Gmail密碼:')
To = input('收件人的Gmail信箱:')
msg= input('請輸入你要的訊息 可以打Subject喔 用\\n隔開:')
isDDoS = 'N'
isDDoS = input('你要傳送大量郵件嗎(y/N)')

#例外處理
# try:
#     smtp.login(mail, pw)                       #登入
# except smtplib.SMTPAuthenticationError:
#     print('帳號或密碼錯誤 離開!!!')
#     exit(0)
status = smtp
if isDDoS == 'y' or 'Y' or 'Yes' or 'yes':
    times = int(input('請問你要傳多少個:'))
    isBreak = input('是否傳送失敗時停止(Y/n):')
    for i in range(0,times):
        try:
            status = smtp.sendmail(mail, To, msg)  # 加密文件
        except smtplib.SMTPSenderRefused:
            print('登入需要驗證!!!')
        if status == {}:
            print("郵件傳送成功!")
        else:
            print("郵件傳送失敗!")
            if isBreak == 'n' or 'No' or 'no':
                continue
            else:
                break
else:
    status=smtp.sendmail(mail, To, msg)       #加密文件
    if status=={}:
        print("郵件傳送成功!")
    else:
        print("郵件傳送失敗!")
smtp.quit()
