import requests
from bs4 import BeautifulSoup
from pathlib import Path
def download_file(url,local_filename):
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()

url="https://sou-yun.cn/eBookIndex.aspx?id=2088"
book_name="唐音癸签-明-胡震亨"

def download_book(url,book_name):
    Path("./download/%s"%book_name).mkdir(parents=True, exist_ok=True)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text,'html.parser')
    links=soup.find_all("div",class_="inline1",style="width: 340px;")
    for link in links:
        name,read,links=(link.find_all("a"))
        book_url=links.attrs["href"]
        target_file="./download/%s/%s_%s.pdf"%(book_name,name.text,book_name)
        print("download %s to %s"%(book_url,target_file))
        download_file(book_url,target_file)


# download_book(url,book_name)        
download_book("https://sou-yun.cn/eBookIndex.aspx?id=8543","历代诗话-清-吴景旭")

download_book("https://sou-yun.cn/eBookIndex.aspx?id=1447","渔洋诗话-清-王士禛")
