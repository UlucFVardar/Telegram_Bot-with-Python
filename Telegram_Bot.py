# -*- coding: utf-8 -*-
import requests

# @author =__Uluç Furkan Vardar__

'''
!To use telegram bot firstly You have to create a bot using BotFather in telegram an take the uniq Id of the bot to use!!


to take chat id first you have to send a message to your chat bot from telegram 
then 
you have to go 
https://api.telegram.org/'+str(uniq_ID)+'/getupdates
then you can see your message and information about that message and you can see chat_id (user_ID actually)
'''


uniq_ID='bot577945846:AAGi470ssz........'#_Your-ID_
chat_id='443290.....'#_YourChatID_

telegramBotURL='https://api.telegram.org/'+str(uniq_ID)+'/sendmessage?chat_id='+str(chat_id)+'&text='


text="This is the first message that I send from python to telegram"
#text="<b>"+text+"</b>"     #makes the text bold
#text='<i>'+text+'</i>''.  #makes the text italic
 #and so on 

'''
also you can modify to message that telgram API's support they are ;

<b>bold</b>, <strong>bold</strong>
<i>italic</i>, <em>italic</em>
<a href="http://www.example.com/">inline URL</a>
<a href="tg://user?id=123456789">inline mention of a user</a>
<code>inline fixed-width code</code>
<pre>pre-formatted fixed-width code block</pre>

but Tags must not be nested.
also you have use HTML parser and have to edit your URl 
with
telegramBotURL='https://api.telegram.org/'+str(uniq_ID)+'/sendmessage?chat_id='+str(chat_id)+'&parse_mode=HTML&text='



also you can find any information about telegram API from ;
   	>>>> https://core.telegram.org/bots/api#message <<<<<<
'''
source_code=requests.get(telegramBotURL+text) ## finish your first telegram bot message sended



