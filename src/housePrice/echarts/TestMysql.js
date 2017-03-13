var mysql   = require('mysql');
var connection = mysql.createConnection({
 host   : 'localhost',
 user   : 'root',
 password : 'root',
 database : 'house'
});

connection.connect();

connection.query('SELECT * from ods_house_new limit 10', function(err, rows, fields) {
 if (err) throw err;

 console.log('The solution is: ', rows[0].id);
});

connection.end();