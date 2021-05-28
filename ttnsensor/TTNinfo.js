var ttn = require("ttn")

var appID = "rak7205expapplblbl"
var accessKey = "ttn-account-v2.X95-eX********"

ttn.data(appID, accessKey)
  .then(function (client) {
    client.on("uplink", function (devID, payload) {
      console.log("Received uplink from ", devID)
      console.log(payload)
    })
  })
  .catch(function (error) {
    console.error("Error", error)
    process.exit(1)
  })
