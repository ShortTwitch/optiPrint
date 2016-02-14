var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/file_upload', function (req, res) {
  req.pipe(req.busboy);
  req.busboy.on('file', function (fieldname, file, filename) {
    console.log("FieldName: " + fieldname);
    console.log("File: " + file);
    console.log("Filename: " + filename);
    res.end("File Received.");
  });
});

module.exports = router;
