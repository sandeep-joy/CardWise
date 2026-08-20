#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request,urlopen
import ssl,json,datetime,re
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/"data"/"source_health.json"
SOURCES=[
("Chase Sapphire Preferred","https://www.chase.com/sapphire-cards/personal/preferred",["5x","3x","gas"]),
("Chase Freedom Unlimited","https://www.chase.com/personal/credit-cards/freedom/unlimited",["5%","3%","1.5%"]),
("Discover calendar","https://www.discover.com/credit-cards/cash-back/cashback-calendar.html",["5%","1,500"]),
("U.S. Bank Altitude Connect","https://cardrewards.usbank.com/CONNECT-5X_RecipeA/Connect_5X_A.html",["5X","4X","wholesale"]),
("Robinhood legal rewards terms","https://api.robinhood.com/creditcard/legal/reward-terms",["three (3)","Travel Portal"]),
("Costco payment methods","https://customerservice.costco.com/app/answers/detail/a_id/719/",["Visa","Gas"]),
("Costco Executive Membership","https://customerservice.costco.com/app/answers/detail/a_id/1205/",["2%","Gasoline"])]
ALLOWED={"www.chase.com","asset.chase.com","www.discover.com","cardrewards.usbank.com","www.usbank.com","rewards.usbank.com","api.robinhood.com","robinhood.com","customerservice.costco.com"}
def fetch(url):
 p=urlparse(url)
 if p.scheme!="https" or p.hostname not in ALLOWED: raise RuntimeError("blocked URL")
 req=Request(url,headers={"User-Agent":"Mozilla/5.0 CardWisePublicBenefits/1.0","Accept":"text/html,application/json;q=0.9,*/*;q=0.8"})
 with urlopen(req,timeout=25,context=ssl.create_default_context()) as r:
  raw=r.read(1500000).decode("utf-8","ignore");status=getattr(r,"status",200)
 return status,re.sub(r"\s+"," ",re.sub(r"<[^>]+>"," ",raw))
results=[]
for label,url,needles in SOURCES:
 try:
  status,text=fetch(url);found=[n for n in needles if n.lower() in text.lower()]
  results.append({"label":label,"url":url,"ok":status<400 and len(found)>=1,"status":status,"matched":found})
 except Exception as e: results.append({"label":label,"url":url,"ok":False,"error":type(e).__name__+": "+str(e)[:180]})
payload={"checked_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"ok":all(x["ok"] for x in results),"sources":results,"policy":"HTTPS allowlisted issuer/Costco public URLs only.","note":"Conservative source-health check; reward rates are not silently rewritten."}
OUT.write_text(json.dumps(payload,indent=2));print(json.dumps(payload,indent=2))
