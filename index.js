function updateClock() {
    var now = new Date();
    var hours = now.getHours().toString().padStart(2, '0');
    var minutes = now.getMinutes().toString().padStart(2, '0');
    var seconds = now.getSeconds().toString().padStart(2, '0');
    var time = hours + ':' + minutes + ':' + seconds;
  
    document.getElementById('clock').textContent = time;
  }
  
  setInterval(updateClock, 1000);

  function getLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showLocation);
    } else {
      var locationElement = document.getElementById('location');
      locationElement.innerHTML = 'Geolocalización no es compatible con este navegador.';
    }
  }
  
  function showDate() {
    var currentDate = new Date();
    var day = currentDate.toLocaleDateString(undefined, { weekday: 'long' });
    var date = currentDate.toLocaleDateString();
  
    var dateElement = document.getElementById('date');
    dateElement.innerHTML = day + '<br>' + date;
  }
  
  showDate();

  // Importar el módulo de MySQL
const mysql = require('mysql');

// Configurar los detalles de la conexión a la base de datos
const connection = mysql.createConnection({
  host: 'http://db-mysql-sfo3-77846-do-user-14160211-0.b.db.ondigitalocean.com',
  user: 'doadmin',
  password: 'AVNS_7sCTBTkvkfjOZZs8oB1',
  database: 'CubitDB'
});

// Establecer la conexión a la base de datos
connection.connect();

// Ejecutar una consulta SELECT
connection.query('SELECT * FROM tabla', (error, results, fields) => {
  if (error) {
    console.error('Error al ejecutar la consulta: ' + error.stack);
    return;
  }

  // Procesar los resultados de la consulta
  console.log('Resultados: ', results);
});

// Cerrar la conexión a la base de datos
connection.end();

