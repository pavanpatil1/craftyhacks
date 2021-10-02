import pymongo
from pymongo import MongoClient
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 

class Mailhandler():

    def __init__(self):
        self.client=MongoClient('localhost', 27017)
        self.db=self.client.alumni
    
        
    def py_mail_confirm(self):

            TO = 'kedar@mitaoe.ac.in'
            FROM ='ksparsewar1023@gmail.com'
            BODY = """
                <head><META http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body>
            
            
            
            
            <div style="background-color:#f4f4f5">
            <table cellpadding="0" cellspacing="0" style="width:100%;height:100%;background-color:#f4f4f5;text-align:center">
            <tbody><tr>
            <td style="text-align:center">
            <table align="center" cellpadding="0" cellspacing="0" style="background-color:#fff;width:100%;max-width:680px;height:100%">
            <tbody><tr>
            <td>
            <table align="center" cellpadding="0" cellspacing="0" style="text-align:left;padding-bottom:88px;width:100%;padding-left:120px;padding-right:120px">
            <tbody>
            <tr>
            <td colspan="2" style="padding-top:72px;color:#000000;font-family:&#39;Postmates Std&#39;,&#39;Helvetica&#39;,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;font-size:48px;font-style:normal;font-weight:600;letter-spacing:-2.6px;line-height:52px;text-decoration:none"><center><img src="http://Capture.PNG" alt="" height="100px"></center></td>
            </tr>
            <tr>
            <td style="padding-top:48px;padding-bottom:48px">
            <table cellpadding="0" cellspacing="0" style="width:100%">
            <tbody><tr>
            <td style="width:100%;height:1px;max-height:1px;background-color:#d9dbe0"></td>
            </tr>
            </tbody></table>
            </td>
            </tr>
            <tr>
            <td style="color:#9095a2;font-family:&#39;Postmates Std&#39;,&#39;Helvetica&#39;,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;font-size:16px;font-style:normal;font-weight:400;letter-spacing:-0.18px;line-height:24px;text-decoration:none;vertical-align:top;width:100%">
            <b>Hii, Kedar Paresewar</b>  <br><br>                                  
            Woww! Thanks for Creating Account in Class Reunion! We are Welcome Here and follow below Instruction 
                                                </td>
            </tr>
            <tr>
            <td style="padding-top:24px;color:#9095a2;font-family:&#39;Postmates Std&#39;,&#39;Helvetica&#39;,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;font-size:16px;font-style:normal;font-weight:400;letter-spacing:-0.18px;line-height:24px;text-decoration:none;vertical-align:top;width:100%">
                                                Please tap the button below to Confirm your Account.
                                                </td>
            </tr>
            <tr>
            <td>
            <a  href="http://localhost:5000/sign" style="margin-top:36px;color:#ffffff;font-family:&#39;Postmates Std&#39;,&#39;Helvetica&#39;,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;font-size:12px;font-style:normal;font-weight:600;letter-spacing:0.7px;line-height:48px;text-decoration:none;vertical-align:top;width:220px;background-color:#00cc99;border-radius:28px;display:block;text-align:center;text-transform:uppercase">
                                                    Confirm Account
                                                </a>
            
            </td>
            </tr>
            </tbody></table>
            </td>
            </tr>
            </tbody></table>
        
            </td></tr></tbody></table></div></body>
        
        
            """
            SUBJECT="Class Reunion"
    
            """With this function we send out our html email"""
        
            # Create message container - the correct MIME type is multipart/alternative here!
            MESSAGE = MIMEMultipart('alternative')
            MESSAGE['subject'] = SUBJECT
            MESSAGE['To'] = TO
            MESSAGE['From'] = FROM
            # Record the MIME type text/html.
            HTML_BODY = MIMEText(BODY, 'html')
        
            # Attach parts into message container.
            # According to RFC 2046, the last part of a multipart message, in this case
            # the HTML message, is best and preferred.
            MESSAGE.attach(HTML_BODY)
        
            # The actual sending of the e-mail
            server = smtplib.SMTP('smtp.gmail.com:587')
        
            # Print debugging output when testing
            server.set_debuglevel(1)
        
            # Credentials (if needed) for sending the mail
            password = "kedar1023"
        
            server.starttls()
            server.login(FROM,password)
            server.sendmail(FROM, [TO], MESSAGE.as_string())
            server.quit()
        

            
    
    
