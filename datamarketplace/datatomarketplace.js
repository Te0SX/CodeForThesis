const fetch = require('node-fetch');
const { publish } = require('./iota');
const { debug, serverUrl } = require('./config.json');
var jp = require('jsonpath');
const fs = require('fs')

function intervalFunc() {
  // fs.readFile('./data.json', (err, data) => { 
  //   if (err) throw err; 
  
  //   console.log(data.toString()); 
  // }) 

  var data1 = fs.readFileSync('./data.json','utf8');
  var data = JSON.parse(data1)

  var bltemperature = jp.query(data, '$..temperature_2');
  var blpressure = jp.query(data, '$..barometric_pressure_6');
  var blhumidity = jp.query(data, '$..relative_humidity_7');

  var env_data = null;
  env_data = {
      'temperature_2': bltemperature, 
      'barometric_pressure_6': blpressure, 
      'relative_humidity_7': blhumidity
    }  
    
  if (debug) {
      console.log(env_data);
  } else {
      // Publish sensor data to marketplace
      publish(env_data); // your sensor data goes here. Payload is any content in JSON format
    
    // await new Promise(resolve => setTimeout(resolve, delay));
  }
}
// queryData(60000) // query data every 60 seconds
setInterval(intervalFunc, 30000);
