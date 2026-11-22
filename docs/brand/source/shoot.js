const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();
const map={icon:[1,'app-icon-1024.png'],feature:[1,'play-feature-1024x500.png'],shot1:[1,'screen-1-photo.png'],shot2:[1,'screen-2-check.png'],shot3:[1,'screen-3-letter.png'],shot4:[1,'screen-4-usage.png'],fb:[2,'facebook-card.png'],tester:[1,'facebook-testers.png'],flyer:[2,'flyer-a5.png']};
for(const s of [1,2]){const p=await b.newPage({deviceScaleFactor:s,viewport:{width:1300,height:1000}});
await p.goto('file://'+process.cwd()+'/assets.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(1200);
for(const [id,[sc,f]] of Object.entries(map)) if(sc===s) await p.locator('#'+id).screenshot({path:'out/'+f});
await p.close();}
await b.close();})();
