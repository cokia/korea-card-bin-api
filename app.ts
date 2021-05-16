import express, { Application } from 'express';
import cors from 'cors';
import fs from 'fs'
import util from 'util';
import bindata from './bindata.json'

// interface ICardObject {
//   'BIN': number, 'ISSUER': string, 'CARDNAME': string, 'CARDTYPE': string, 'CARDOWNERTYPE': number
// }

class App {
  public application: Application;

  constructor() {
    this.application = express();
  }
}

const app = new App().application;
app.use(cors());
app.all('/*', function(req, res, next) {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'X-Requested-With');
  next();
});

app.listen(3001,async () => {
  console.info('✅ Start korea-card-bin-api server✅');
});

//read data when server start
const data = JSON.parse(JSON.stringify(bindata))

app.get('/', function(req, res) {
  res.redirect('https://github.com/cokia/korea-card-bin-api');
});

app.get('/api/:binNumber', async function(req,res) {
  //@ts-ignore
const result = (data.filter(x => x["BIN"] === parseInt(req.params.binNumber)))[0];

if (result == undefined){
  res.status(404).send({})
}
res.status(200).send(result);
});


