from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import subprocess,os,time,json
pdf='/Users/gcrane/Library/Mobile Documents/iCloud~com~apple~iBooks/Documents/Suetonius_Loeb-rolfe.pdf'
root=Path('work/suetonius-pdf/full');root.mkdir(exist_ok=True)
env=dict(os.environ);env['OMP_THREAD_LIMIT']='1'
start=time.time()
def run(n):
 out=root/('p%04d'%n)
 if out.with_suffix('.txt').exists():return n
 subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','2200','-singlefile','-png',pdf,str(out)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,env=env)
 subprocess.run(['tesseract',str(out)+'.png',str(out),'-l','eng','--psm','3','txt','tsv'],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,env=env)
 return n
with ThreadPoolExecutor(max_workers=6) as ex:
 fs=[ex.submit(run,n) for n in range(1,1095)]
 for i,f in enumerate(as_completed(fs),1):
  n=f.result()
  if i%25==0 or i==1094:print(json.dumps({'done':i,'total':1094,'seconds':round(time.time()-start),'last_page':n}),flush=True)
