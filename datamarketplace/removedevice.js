const fetch = require('node-fetch');

const sendRequest = async () => {
  const response = await fetch('https://api.marketplace.tangle.works/delete',
    {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        apiKey: '694b54e0-a42d-*******',
        deviceId: 'WYI*****',
      })
    });
  const json = await response.json();
  console.log(json);
}

sendRequest();