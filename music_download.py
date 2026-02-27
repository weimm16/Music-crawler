import requests
import re
import execjs
import os
import tkinter as tk




# 定义文件夹路径
folder_path = 'music'

# 检查文件夹是否存在，如果不存在则创建
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 写入文件




#用户信息

headers={'cookie':'MUSIC_R_T=1418625136805; MUSIC_A_T=1418625137000; _iuqxldmzr_=32; WEVNSM=1.0.0; WM_TID=eIWQRd7XAYJFAURURAeUk5Mol3DYXyO0; ntes_utid=tid._.F8cpH2%252BktRpEFwAQUVPQwoZoxyXZWvBP._.0; NMTID=00OuIRqcJ-Y_w6OAka7onEKyPwzb2oAAAGSzgpAAg; _ntes_nnid=161b4d01ce10458ca3f97ce23aa8d4ff,1730033631643; _ntes_nuid=161b4d01ce10458ca3f97ce23aa8d4ff; WNMCID=dzpjbr.1730033633741.01.0; WM_NI=Ds1BucPnGmkf5I1KwQbOGhMjAdvFh%2F0GOREzz9zB%2FdqPbr4dfJd0O1LxoAemLltjczjA0DZ7VSmReHIl3oLFzAQ3RlcolvhBI7Y7IeyDUwiHWCDWVpDFiqd%2BcYfBvCffNnM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee9bb13ab4b0a6b8cf68a6ef8ab6c45b829b9fb1db50a29dfbb7cc6da9b685b9e72af0fea7c3b92a88adffa3f86994b2898eea6ef797ffacf65ba2918989d06283bcbaa7eb25f49981b3c872bae7b6a3ae70b390ae93b770a696acd1ce3b90a8a1a2e86790b4bc8be272aa9f00a5d93d968da3b3e8448bb4fd90cf4eba9f9fd4d168a1b1a497eb4a8be997d8cc6fbb9c9b98ec44959d8cb8d57c889aa792e721a187aaa3f549a6ba828fd037e2a3; sDeviceId=YD-cZa%2Fu3SAbOZFAkQQRVLE1z0JGSMS8mdz; __snaker__id=4QZuCkH9EL5p6cGU; ntes_kaola_ad=1; JSESSIONID-WYYY=XN9Sg4aPkWV3Droy2TrEQoK1bO8sG%5C%5CZnMwaG6Md%2BYgWzKEfOSU%2BroQX4zBPs%2BoSGuNNb24Pz4wMxNr%2BG6KqMHo0Q%2FT7PRv%2BCwX4eEz%2BHJKAeItaoscPki6p42tUjvgW%5Cf6nkf5OlCltW0SehGSQsgchwUAlXzOxxkckrHVX2Qay9ewC%3A1730090278746; gdxidpyhxdE=UBSZtIHIKMJSIUDIGYDivxKZwB%2BSPYq4GnmOnnI8zWg8DdNnq3qjgp%2BJlLjM7Ts5vh4u4dVTRxuZX%2FCVC71wbh6%2F8DdM%2FNqB%2BiGP5xpjytOLsOycyW79Bn3%5Ca1WCVj5wS3ytCXiAPqhPzApB5ShrWdj372PIZ2Rh1wH8MQ8BotLsEkat%3A1730089673560; playerid=64169634; NTES_YD_SESS=3lzoFnpaB8A1Qzp.Q7I2gibOQoT446ZUJNUgr59KrGQWCIEACNjlM81j3.Slao.PGOnSzpHUT_oVwMrPmh3pR6pc4hyODSLK20KHUppSYsFp2rd4PIYmsyWpsYRSBgKjUzF5zaPMJWB_WfLenDA_KGapm6uRVW7TUKsIzBBm.vnd09FQVfHqzsAx0HfD.zGN2ne3brVLLmcet.EibZHfdxhEAqWgwdrQq9._kU20WX9a_; S_INFO=1730089153|0|0&60##|18856301295; P_INFO=18856301295|1730089153|1|music|00&99|null&null&null#anh&341800#10#0|&0|null|18856301295; __remember_me=true; MUSIC_U=0008B2AE203608B9D9772ABAED095494885D7CB1E878C5D1B0E2B6A758580CAC12D1A6C61FC39EC8E6444C187211B756B62FC049105AF9E5D7DFE3C683E7DF69E36FE1E6211AF4344F79338E95B068E6B512EF903C87AAFB51F46D55B16940101FA9D4A2408DE7B86FCBA1337227894432F5E9055690A1C64CD916D1C47F3404E60BB57943D1BADBFD08C44C2FC8BBFA796D84729A7ECA3FCADB7F741BF50201C7D6AF0C93F6DCCDAF68EDCFCE9CAAB335988C1E30186A267A60B35EA2DAB98C5C9EFA997CE37F253F9A73437DD618D219D8C4C059575A396B1ABD5E12D64FA38C9A99FED65DBA531A8D330B3B860AAD5F4CD6593E9B906FF25A41A7A32585AC5A27B1FB616CE638C31B40827F496DCE22F15059142FF16179F09CD4D7103F6FCD58D4652BFED135DE4E9F08E3CF0050D2A7B399755A3B43C427B08113D5700F68DC1B44524C96AEB23FF9F3DCE236DC8A7F4698F5B30BD91B80075F34132F06FF; __csrf=c9cb821408fca78c44bc0478ad7ebd9b',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
}
link='https://music.163.com/discover/toplist?id=3778678'
html=requests.get(url=link,headers=headers).text
#print(html)
info=re.findall('<a href="/song\?id=(\d+)">(.*?)</a>',html)




root = tk.Tk()
root.title("热门歌曲下载")
root.geometry('500x600')

# 创建一个输入框
input_var = tk.StringVar()
entry = tk.Entry(root, textvariable=input_var, font=('Arial', 12), width=50)
entry.pack(pady=10)

# 创建一个按钮






def add_song():
    song_title = input_var.get()  # 获取用户输入










    
    
    
    if song_title:  # 确保输入不为空
        text_box.config(state=tk.NORMAL)  # 使文本框可编辑

        for music_id,title in info:
               
                if input_var.get() == music_id or input_var.get() == 'all' or input_var.get() == 'ALL':
                        print('1.0', f'歌曲名称: {title}  提取中......\n')
                        text_box.insert('1.0', f'歌曲名称: {title}  提取中......\n')
                        
                        js_file= open('网易云.js',encoding='utf-8').read()
                        js_code=execjs.compile(js_file)
                        #前端中的参数,ids为歌曲的特征码
                        i6c={
                            "ids": f"[{music_id}]",
                            "level": "standard",
                            "encodeType": "aac",
                            "csrf_token": "0b23182fe396ac88acbb1203ed773f20"
                        }
                        result=js_code.call('GetData',i6c)

                        #需要爬取的url
                        url='https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=0b23182fe396ac88acbb1203ed773f20'
                        #js逆向出加密的内容
                        data={'params':result['encText'],
                        'encSecKey':result['encSecKey']}
                        #发送请求
                        
                        
                    
                        try:
                            response = requests.post(url=url,data=data,headers=headers)
                        #获取json数据
                        
                            json_data=response.json()
                            #从字典中获取url
                            music_url=json_data['data'][0]['url']
                            if music_url != None:
                                
                                content=requests.get(url=music_url,headers=headers).content
                                with open(f'music\\{title}.mp3',mode='wb') as f:
                                    f.write(content)
                                    
                                    root.after(5)
                                    print('提取完成')
                                    text_box.insert('1.0', f'提取完成\n')
                            
                            else:
                                print('url不合法')
                                text_box.insert('1.0', f'url不合法\n')
                                
                            
                            
                        except :
                         print('响应超时')
                         text_box.insert('1.0', f'响应超时\n')
                
                root.update_idletasks()  # 更新界面
                
                if input_var.get() == music_id:      
                        break 
        if input_var.get() != music_id:        
            print('编号不存在')
            text_box.insert('1.0', f'编号不存在\n')
            
            
                   
                        
                        
                        
        input_var.set('')  # 清空输入框

add_button = tk.Button(root, text="请输入对应编号", command=add_song, font=('Arial', 12))
add_button.pack(pady=5)

# 创建 Text 组件
text_box = tk.Text(root, bg='white', font=('Arial', 12), width=75, height=35)
text_box.pack()

# 显示示例歌曲
for music_id, title in info:
    text_box.insert(tk.END, f'编号: {music_id} 歌曲名称: {title}\n')
text_box.config(state=tk.DISABLED)
# 运行主循环
root.mainloop()

"""

for music_id,title in info:
   if input_var.get() =music_id
    
        print(title,':',music_id)
        js_file= open('网易云.js',encoding='utf-8').read()
        js_code=execjs.compile(js_file)
        #前端中的参数,ids为歌曲的特征码
        i6c={
            "ids": f"[{music_id}]",
            "level": "standard",
            "encodeType": "aac",
            "csrf_token": "0b23182fe396ac88acbb1203ed773f20"
        }
        result=js_code.call('GetData',i6c)

        #需要爬取的url
        url='https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=0b23182fe396ac88acbb1203ed773f20'
        #js逆向出加密的内容
        data={'params':result['encText'],
        'encSecKey':result['encSecKey']}
        #发送请求
        
        
    
        try:
            response = requests.post(url=url,data=data,headers=headers)
        #获取json数据
        
            json_data=response.json()
            #从字典中获取url
            music_url=json_data['data'][0]['url']
            if music_url != None:
                print('提取成功')
                content=requests.get(url=music_url,headers=headers).content
                with open(f'music\\{title}.mp3',mode='wb') as f:
                    f.write(content)
            else:
                print('url不合法')

        except :
        print('响应超时') 

    else:
        print('编号不存在')"""