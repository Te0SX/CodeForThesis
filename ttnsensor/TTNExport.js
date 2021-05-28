var ttn = require("ttn")
var appID = "rak7205expapplblbl"
var accessKey = "ttn-account-v2.***********"
var fsp = require('fs').promises

ttn.data(appID, accessKey)
  .then(function (client) {
    client.on("uplink", function (devID, payload) {
      data = JSON.stringify(payload)
      fsp.writeFile("data.json", data)
      fsp.writeFile("/Users/tdvr/Documents/Coding/Projects/datamarketplace/RAK5205evnsensor/data.json", data)
    })
  })
  .catch(function (error) {
    console.error("Error", error)
    process.exit(1)
  })

  