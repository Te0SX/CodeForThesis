const fetch = require('node-fetch');

const sendRequest = async () => {
  const response = await fetch('https://api.marketplace.tangle.works/newDevice',
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        apiKey: '694b54e0-a42d-*******',
        id: 'RAK5205evnsen2',
        device: {
          owner: 'tv',
          sensorId: 'RAK5205evnsen2',
          type: 'Environmental Sensor',
          company: 'Private',
          price: '100',
          date: '12 December, 2019',
          inactive: false,
          dataTypes: [
            { id: 'temperature_2', name: 'Temperature', unit: 'C' },
            { id: 'barometric_pressure_6', name: 'Pressure', unit: 'hPa' },
            { id: 'relative_humidity_7', name: 'Humidity', unit: '%rH' },
          ],
          location:{
            city: 'Kiria,Drama',
            country: 'Greece'
          },
          lat: 41.0991,
          lon: 24.2841
        }
      })
    });
  const json = await response.json();
  console.log(json);
}

sendRequest();