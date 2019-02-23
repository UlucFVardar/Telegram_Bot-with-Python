#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @author =__Uluç Furkan Vardar__
import requests

# --- Reportting  ------------------------------------------------------------------------------
def sendTelegramMess(header):
    def clean_header(header):
        for key in header.keys():
            header[key] = str(header[key]).replace('<','_').replace('\">','_').replace('\"','--').replace('&','(ampersand)')
        return header
    def prepare_req(header):
        chat_id = header['chat_id']
        text_send = ''
        try:
            text_send += "<b> From: "+header['from']+"</b>\n"
        except Exception as e:
            raise Exception ("[Telegram Bot ERROR]: header json doesn't contains 'from' filed. --fill with 'code name'")
        
        try:
            text_send += "----<i>"+header['text']+"</i>\n"
        except Exception as e:
            raise Exception ("[Telegram Bot ERROR]: header json doesn't contains 'text' filed. --fill with 'exception reason'")
        

        try:
            text_send += "\n\nException:\n<i>"+header['exception']+"</i>\n"
        except Exception as e:
            #print "[Telegram Bot Warning]: header json doesn't contains 'exception' filed. --fill with 'exception itself' if you want"
            pass

        try:
            text_send += "\n<b>---> Owner: "+header['Owner']+"</b>\n"
        except Exception as e:
            #print "[Telegram Bot Warning]: header json doesn't contains 'Owner' filed. --fill with 'Script Owner' if you want"
            pass
        return chat_id, text_send 
    def send(chat_id,text_send):
        uniq_ID='-----------------------' #_Telegram-Bot-ID_
        chat_id = chat_id
        telegramBotURL = 'https://api.telegram.org/'+str(uniq_ID)+'/sendmessage?chat_id='+str(chat_id)+'&parse_mode=HTML&disable_web_page_preview=true&text='+str(text_send)
        #print telegramBotURL
        source_code = requests.get(telegramBotURL)
        return source_code.json()



    header = clean_header(header)
    chat_id, text_send = prepare_req(header)
    return send(chat_id, text_send)
# ----------------------------------------------------------------------------------------------



try : 
    print  a
except Exception as e:
  sendTelegramMess (header = {
                      "chat_id": "-376756543",
                      'from' : 'Telegram Bot Message test', #bold
                      'text' : 'Test try cath içi', #italik
                      'exception' : e, #italik
                      'Owner' : 'uluc' #bold
              })
  










