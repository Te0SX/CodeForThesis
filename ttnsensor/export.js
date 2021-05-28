var fsp = require('fs').promises
var data = FileSystem.readTextFromFileSync(FileSystem.dataDirectory + "/data.json");

var json_parsed = JSON.parse(data)
for (var prop in json_parsed) {
    console.log(json_parsed[prop].info.num_events);
}
fsp.writeFile("fileparse.js", json_parsed)
