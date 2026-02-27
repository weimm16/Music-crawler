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

headers={'cookie':'',
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