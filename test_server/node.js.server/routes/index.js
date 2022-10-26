var express = require('express');
var router = express.Router();

const fs = require('fs');


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


router.get('/google/:id', function(req, res){
  let tempo= new Date();
  let log = {
    Time: tempo,
    Speech: req.params.id,
  };
  var obj = {
    table: []
  };
  /*obj.table.push({Time: tempo, Speech:req.params.id});
  var json = JSON.stringify(obj);
  var callback;

  //fs.writeFileSync('jsontest.json', json);*/
  fs.readFile('jsontest.json', 'utf8', function readFileCallback(err, data){
    if (err){
      console.log(err);
    } else {
      obj = JSON.parse(data); //now it an object
      obj.table.push({Time: tempo, Speech:req.params.id}); //add some data
      let json = JSON.stringify(obj); //convert it back to json
      fs.writeFileSync('jsontest.json', json); // write it back
    }});

  /*
  let data = JSON.stringify(log);
  fs.writeFileSync('jsontest.json', data);*/

  res.send('Speech: ' + req.params.id + 'Time: ' + tempo);
});



router.get('/logs', function(req, res){
  let rawdata = fs.readFileSync('jsontest.json');
  let logs = JSON.parse(rawdata);
  res.send(logs);
});

module.exports = router;
