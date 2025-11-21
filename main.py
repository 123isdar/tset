#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ftplib import FTP_TLS
import random
from datetime import datetime
import io
import time

# ========================= إعداداتك =========================
FTP_HOST = "ftpupload.net" 
FTP_USER = "if0_39771004"   
FTP_PASS = "4137as9Dkt3hgg6" 
REMOTE_FILE = "/htdocs/test.txt"

# كم مرة تريد تكرار إضافة رقم عشوائي في كل تشغيل؟
REPEAT_COUNT = 100                   # غيّر هذا الرقم كما تشاء (10 = يضيف 10 أسطر دفعة واحدة)

# تأخير بين كل إضافة (ثواني) - اختياري
DELAY_BETWEEN_ADDS = 0.5             # 0.5 ثانية بين كل سطر (يمكنك وضع 0 إذا لا تريد تأخير)

# ========================= الكود المتكرر =========================
def add_multiple_random_numbers():
    ftp = None
    try:
        print(f"[{datetime.now()}] جاري الاتصال بـ {FTP_HOST}...")
        ftp = FTP_TLS()
        ftp.connect(FTP_HOST, 21, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.prot_p()
        print("تم الاتصال بنجاح! جاري إضافة الأرقام...")

        success_count = 0
        for i in range(1, REPEAT_COUNT + 1):
            random_number = random.randint(100000, 999999)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_line = f"[{i:02d}] {current_time} | رقم عشوائي: {random_number}\n"

            # تحويل النص إلى BytesIO (الحل السحري)
            data = io.BytesIO(new_line.encode('utf-8'))

            # إضافة السطر في نهاية الملف
            ftp.storbinary('APPE ' + REMOTE_FILE, data)
            
            print(f"تمت الإضافة {i}/{REPEAT_COUNT}: {random_number}")
            success_count += 1

            # تأخير بسيط (اختياري)
            if DELAY_BETWEEN_ADDS > 0 and i < REPEAT_COUNT:
                time.sleep(DELAY_BETWEEN_ADDS)

        print(f"تم بنجاح إضافة {success_count} أرقام عشوائية!")

    except Exception as e:
        print(f"حدث خطأ: {str(e)}")
    
    finally:
        if ftp:
            try:
                ftp.quit()
                print("تم إغلاق الاتصال.")
            except:
                pass

# ========================= تشغيل الكود =========================
if __name__ == "__main__":
    add_multiple_random_numbers()