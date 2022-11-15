import express from 'express';
import fs from 'node:fs/promises';

var newsList

async function getData(){
  function getFullDateObj(date) {
    if (date < 10)
        return `0${date}`;
    else
        return date
  }
  const today = new Date();
  const todayDate = `${today.getFullYear()}-${getFullDateObj(today.getMonth()+1)}-${getFullDateObj(today.getDate())}`
  
  try {
    const res = await fs.readFile(`../newsanalysis/json_files/last${todayDate}.json`, { encoding: 'utf8' });
    const data = JSON.parse(res)
    return data;
  } catch (err) {
    console.error(err);
  }
}

import { CronJob } from 'cron'
console.log('[CRON] Started daily json fetch job.');
const daily = new CronJob('0 30 0 * * *', function() {
	getData().then((rtn) => {
    newsList = rtn
    console.log('[CRON] Latest news json file is now ready to used.');
  });
}, null, true, 'Europe/Istanbul');
const job = new CronJob('0 30 0 * * *', function() {
	getData().then((rtn) => {
    newsList = rtn
    console.log('[CRON] Latest news json file is now ready to used.');
  });
}, null, true, 'Europe/Istanbul');
daily.start();
job.start();

(async() => {
  newsList = await getData();
  console.log('Checked if there is a valid json file.');
})()


const app = express();
import cors from 'cors';
app.use(cors());
import bodyParser from 'body-parser';
app.use(bodyParser.urlencoded({extended:true}));
app.use(bodyParser.json())

// GET Call for all users
app.get("/api", (req, res) => {
  return res.status(200).send({
    success: "true",
    message: "news",
    news: newsList,
  });
});

app.listen(8000, () => {
    console.log("server listening on port 8000 with HTTPS!!!");
});